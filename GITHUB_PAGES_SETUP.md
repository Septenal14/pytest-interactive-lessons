# GitHub Pages Setup Guide

## Current Status
- ✅ Local repository created
- ✅ Files ready (index.html, README.md)
- ✅ Git commit done
- ⏳ Need to create GitHub repository
- ⏳ Need to push code
- ⏳ Need to enable GitHub Pages

---

## Step-by-Step Instructions

### 1. Create GitHub Repository

Go to: https://github.com/new

**Settings:**
- Repository name: `pytest-interactive-lessons`
- Description: "Interactive Pytest Lesson 01 with Mermaid diagrams and quiz"
- Visibility: **Public** (required for free GitHub Pages)
- ❌ Do NOT initialize with README, .gitignore, or license (we already have these)

Click **Create repository**

---

### 2. Push Code to GitHub

After creating the repository, run in terminal:

```bash
cd /Users/admin/Desktop/pytest-interactive-lessons

# Verify remote is set correctly
git remote -v

# Push to GitHub
git push -u origin main
```

**If you get authentication error:**
- Use GitHub Desktop app, OR
- Generate Personal Access Token: https://github.com/settings/tokens
- Use token as password when prompted

---

### 3. Enable GitHub Pages

**Option A: Auto-detection (usually works automatically)**
- GitHub detects `index.html` in root
- Pages may be enabled automatically
- Check: https://github.com/Septenal14/pytest-interactive-lessons/settings/pages

**Option B: Manual setup (if needed)**
1. Go to repository Settings
2. Scroll to "Pages" in left sidebar
3. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: **main**
   - Folder: **/ (root)**
4. Click **Save**

---

### 4. Wait for Deployment (1-2 minutes)

GitHub Actions will build and deploy the site.

**Check deployment status:**
- Go to: https://github.com/Septenal14/pytest-interactive-lessons/actions
- Wait for green checkmark ✅

---

### 5. Verify Deployment

**Run verification script:**
```bash
cd /Users/admin/Desktop/pytest-interactive-lessons
./verify-deployment.sh
```

**Manual verification:**
1. Open: https://septenal14.github.io/pytest-interactive-lessons/
2. Check:
   - ✅ Page loads correctly
   - ✅ Mermaid diagram renders (pytest execution flow)
   - ✅ Quiz is interactive (click answers)
   - ✅ Code blocks are formatted
   - ✅ No 404 errors

---

## Final URL

```
https://septenal14.github.io/pytest-interactive-lessons/
```

**Use this URL in Skill Space** to embed the interactive lesson.

---

## Troubleshooting

**Problem: 404 Not Found**
- Wait 2-3 minutes after enabling Pages
- Check Actions tab for build errors
- Verify `index.html` is in repository root

**Problem: Mermaid diagram not rendering**
- Check browser console for errors (F12)
- Verify internet connection (Mermaid loads from CDN)
- Try hard refresh (Cmd+Shift+R on Mac)

**Problem: Quiz not working**
- Check browser console for JavaScript errors
- Verify `checkAnswer()` function is defined in `<script>` tag

**Problem: Push authentication fails**
- Use HTTPS: `git remote set-url origin https://github.com/Septenal14/pytest-interactive-lessons.git`
- Generate token: https://github.com/settings/tokens (select `repo` scope)
- Use token as password when `git push` prompts

---

## Files in This Repository

```
pytest-interactive-lessons/
├── index.html                    # Main interactive lesson
├── README.md                     # Repository description
├── verify-deployment.sh          # Deployment verification script
└── GITHUB_PAGES_SETUP.md        # This guide
```

---

## Next Steps After Deployment

1. ✅ Copy final URL: `https://septenal14.github.io/pytest-interactive-lessons/`
2. ✅ Paste into Skill Space lesson materials (as iframe or external link)
3. ✅ Test from student perspective
4. ✅ Monitor for any issues

---

## Updates and Maintenance

**To update the lesson:**

```bash
cd /Users/admin/Desktop/pytest-interactive-lessons

# Make changes to index.html

git add index.html
git commit -m "Update lesson content"
git push

# Wait 1-2 minutes for automatic redeployment
```

GitHub Pages will automatically rebuild on every push to `main` branch.

---

**Created:** 2025-10-08
**Repository:** https://github.com/Septenal14/pytest-interactive-lessons
**Live Site:** https://septenal14.github.io/pytest-interactive-lessons/
