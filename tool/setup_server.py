import os
import requests
import sys
import subprocess
from base64 import b64encode
from nacl import encoding, public

# Configuration
API_URL = "https://api.github.com"
CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_input(prompt):
    return input(f"{prompt}: ").strip()

def encrypt_secret(public_key, secret_value):
    """Encrypt a Unicode string using the public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")

def main():
    print("🚀 Minecraft Server Rescue Tool 🚀")
    print("-----------------------------------")
    print("This tool will set up a NEW GitHub repository with all necessary secrets.")
    print("All you need is a GitHub Personal Access Token (Classic).")
    print("\n")

    # 1. Get Credentials
    token = get_input("🔑 Enter your GitHub Token")
    repo_name = get_input("📦 Enter New Repository Name (e.g., my-minecraft-server)")
    mega_email = get_input("📧 Enter Mega Email")
    mega_password = get_input("🔒 Enter Mega Password")

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # 2. Get User Info
    print("\n[1/5] Verifying Token...")
    user_resp = requests.get(f"{API_URL}/user", headers=headers)
    if user_resp.status_code != 200:
        print(f"❌ Invalid Token! Status: {user_resp.status_code}")
        print(user_resp.json())
        sys.exit(1)
    
    username = user_resp.json()['login']
    print(f"✅ Logged in as: {username}")

    # 3. Create Repository
    print(f"\n[2/5] Creating Repository '{repo_name}'...")
    repo_data = {
        "name": repo_name,
        "private": False, # Public for 16GB RAM
        "description": "Minecraft Forge Server created by Rescue Tool"
    }
    create_resp = requests.post(f"{API_URL}/user/repos", json=repo_data, headers=headers)
    
    if create_resp.status_code == 422:
         print(f"⚠️ Repository '{repo_name}' already exists! Continuing...")
    elif create_resp.status_code != 201:
        print(f"❌ Failed to create repo! Status: {create_resp.status_code}")
        print(create_resp.json())
        sys.exit(1)
    else:
        print("✅ Repository created successfully!")

    # 4. Get Public Key for Secrets
    print("\n[3/5] Fetching Encryption Key...")
    key_resp = requests.get(f"{API_URL}/repos/{username}/{repo_name}/actions/secrets/public-key", headers=headers)
    if key_resp.status_code != 200:
        print("❌ Failed to get public key!")
        print(key_resp.json())
        # Try to continue strictly for dev purposes, but likely will fail secret upload
    else:
        key_data = key_resp.json()
        key_id = key_data['key_id']
        key = key_data['key']

        # 5. Upload Secrets
        print("\n[4/5] Uploading Secrets (Mega Credentials)...")
        secrets = {
            "MEGA_EMAIL": mega_email,
            "MEGA_PASSWORD": mega_password
        }

        for secret_name, secret_value in secrets.items():
            encrypted_value = encrypt_secret(key, secret_value)
            secret_data = {
                "encrypted_value": encrypted_value,
                "key_id": key_id
            }
            put_resp = requests.put(
                f"{API_URL}/repos/{username}/{repo_name}/actions/secrets/{secret_name}",
                json=secret_data,
                headers=headers
            )
            if put_resp.status_code not in [201, 204]:
                print(f"❌ Failed to upload secret {secret_name}")
            else:
                print(f"✅ Secret {secret_name} uploaded.")

    # 6. Push Files
    print("\n[5/5] Pushing Files to GitHub...")
    os.chdir(CURRENT_DIR)
    
    # Reset git to ensure clean push to new repo
    if os.path.exists(".git"):
         print("Cleaning up old git configuration...")
         # Remove .git folder (Windows command)
         subprocess.run("rmdir /s /q .git", shell=True) 
    
    subprocess.run("git init", shell=True)
    
    # Configure generic identity to avoid "Please tell me who you are" error
    subprocess.run('git config user.email "rescue@tool.local"', shell=True)
    subprocess.run('git config user.name "Rescue Tool"', shell=True)
    
    subprocess.run("git add .", shell=True)
    subprocess.run('git commit -m "Initial commit by Rescue Tool"', shell=True)
    subprocess.run("git branch -M main", shell=True)
    
    remote_url = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"
    subprocess.run(f"git remote add origin {remote_url}", shell=True)
    
    push_result = subprocess.run("git push -u origin main", shell=True)
    
    if push_result.returncode == 0:
        print("\n🎉🎉🎉 SUCCESS! 🎉🎉🎉")
        print(f"Your server is ready at: https://github.com/{username}/{repo_name}")
        print("Go to Actions tab to start your server!")
    else:
        print("\n❌ Failed to push files. Check your output above.")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
