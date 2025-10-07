# Quick Start Guide - GitHub Pages Deployment

## Status: Ready to Deploy

All files are prepared and committed locally. You just need to:
1. Create the GitHub repository
2. Push the code
3. Enable GitHub Pages

---

## 3-Step Deployment

### Step 1: Create Repository on GitHub (2 minutes)

1. Open: https://github.com/new
2. Settings:
   - **Repository name:** `pytest-interactive-lessons`
   - **Visibility:** Public (required for free Pages)
   - **Do NOT check:** Initialize with README
3. Click **"Create repository"**

### Step 2: Push Code (1 minute)

Open terminal and run:

```bash
cd /Users/admin/Desktop/pytest-interactive-lessons
./deploy.sh
```

**Or manually:**

```bash
cd /Users/admin/Desktop/pytest-interactive-lessons
git push -u origin main
```

If authentication is needed:
- Generate token: https://github.com/settings/tokens
- Select `repo` scope
- Use token as password

### Step 3: Enable GitHub Pages (1 minute)

1. Go to: https://github.com/Septenal14/pytest-interactive-lessons/settings/pages
2. Under "Build and deployment":
   - **Source:** Deploy from a branch
   - **Branch:** main
   - **Folder:** / (root)
3. Click **Save**
4. Wait 1-2 minutes for deployment

---

## Verify Deployment

After 1-2 minutes, run:

```bash
cd /Users/admin/Desktop/pytest-interactive-lessons
./verify-deployment.sh
```

Or manually open:
```
https://septenal14.github.io/pytest-interactive-lessons/
```

**Check:**
- ✅ Page loads
- ✅ Mermaid diagram renders
- ✅ Quiz is interactive
- ✅ No errors in console (F12)

---

## Final URL for Skill Space

```
https://septenal14.github.io/pytest-interactive-lessons/
```

Copy this URL and add it to your Skill Space lesson materials.

---

## Files in This Repository

```
pytest-interactive-lessons/
├── index.html                          # Main interactive lesson
├── README.md                           # Repository description
│
├── deploy.sh                           # Interactive deployment helper
├── verify-deployment.sh                # Verify site is live
│
├── QUICKSTART.md                       # This file (3-step guide)
├── GITHUB_PAGES_SETUP.md              # Detailed setup instructions
├── DEPLOYMENT_CHECKLIST.md            # Full deployment checklist
│
├── pytest_lesson_01_timestamps.md     # Lesson 01 content breakdown
├── pytest_lesson_02_timestamps.md     # Lesson 02 content breakdown
├── pytest_lesson_03_timestamps.md     # Lesson 03 content breakdown
├── pytest_lesson_04_timestamps.md     # Lesson 04 content breakdown
├── pytest_lesson_05_timestamps.md     # Lesson 05 content breakdown
│
└── quizzes/                            # Quiz data files
    ├── pytest_lesson_01_quiz.json
    ├── pytest_lesson_02_quiz.json
    ├── pytest_lesson_03_quiz.json
    ├── pytest_lesson_04_quiz.json
    └── pytest_lesson_05_quiz.json
```

---

## Troubleshooting

**Problem:** Authentication error when pushing

**Solution:**
```bash
# Switch to HTTPS
git remote set-url origin https://github.com/Septenal14/pytest-interactive-lessons.git

# Generate token at: https://github.com/settings/tokens
# Then push again
git push -u origin main
```

---

**Problem:** Site shows 404

**Solution:**
- Wait 2-3 minutes for first deployment
- Check Settings → Pages is enabled
- Verify Actions tab for build status

---

**Problem:** Mermaid diagram not rendering

**Solution:**
- Hard refresh: Cmd+Shift+R (Mac) or Ctrl+F5 (Windows)
- Check internet connection (Mermaid loads from CDN)
- Open console (F12) to check for errors

---

## Need Help?

📖 Detailed guides:
- `GITHUB_PAGES_SETUP.md` - Full setup instructions
- `DEPLOYMENT_CHECKLIST.md` - Step-by-step checklist

🔧 Tools:
- `./deploy.sh` - Interactive deployment helper
- `./verify-deployment.sh` - Automated verification

---

**Total Time:** ~5 minutes
**Difficulty:** Easy (just follow 3 steps)
**Result:** Live interactive lesson on GitHub Pages

Good luck! 🚀
