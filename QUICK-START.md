# ⚡ البدء السريع - Quick Start

<div dir="rtl">

## 🚀 خطوات سريعة للبدء

### 1️⃣ رفع على GitHub

افتح PowerShell في **هذا المجلد** واكتب:

```powershell
# تهيئة Git
git init

# إضافة الملفات
git add .

# عمل Commit
git commit -m "Initial Minecraft server setup"

# تغيير إلى main
git branch -M main

# ربط بـ GitHub (غيّر YOUR_USERNAME باسمك)
git remote add origin https://github.com/YOUR_USERNAME/minecraft-server.git

# رفع الملفات
git push -u origin main
```

> 💡 **ملاحظة:** لو مش عامل repository، اعمله من [github.com/new](https://github.com/new)

---

### 2️⃣ تشغيل السيرفر

1. روح على repository في GitHub
2. اضغط على **Actions**
3. اختر **Minecraft Forge Server**
4. اضغط **Run workflow**
5. اضغط الزر الأخضر **Run workflow**

---

### 3️⃣ الحصول على IP

1. روح على [playit.gg](https://playit.gg) وسجّل حساب
2. روح [playit.gg/account/agents](https://playit.gg/account/agents)
3. انسخ الـ **Address**

---

### 4️⃣ الاتصال

1. افتح Minecraft بـ **Forge 1.20.1**
2. Multiplayer → Add Server
3. الصق الـ IP من playit.gg
4. Join Server!

---

## 📖 محتاج تفاصيل أكتر؟

شوف **[GUIDE-AR.md](GUIDE-AR.md)** للدليل الشامل!

---

## ⚙️ الإعدادات السريعة

### تغيير الصعوبة:
افتح `server.properties` وغيّر:
```properties
difficulty=hard
```

### تغيير عدد اللاعبين:
```properties
max-players=50
```

### إضافة Mods:
1. أنشئ مجلد `mods/`
2. حط ملفات `.jar` الخاصة بالـ Mods
3. ارفعها على GitHub
4. شغّل السيرفر من جديد!

---

## 🆘 مشاكل شائعة

### مش لاقي IP في playit.gg؟
- انتظر 1-2 دقيقة بعد تشغيل السيرفر
- اعمل refresh للصفحة

### السيرفر مش شغّال؟
- راجع الـ logs في Actions
- تأكد إن الـ workflow اشتغل صح

### مش قادر أتصل؟
- تأكد إنك شغّال **Forge 1.20.1** (نفس إصدار السيرفر)
- انسخ كامل الـ Address بما فيه الـ Port

---

<div align="center">

**🎮 استمتع باللعب!**

</div>

</div>
