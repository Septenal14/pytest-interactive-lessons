#!/bin/bash

# GitHub Pages Quick Deployment Script
# This script helps with the initial push to GitHub

set -e  # Exit on error

echo "🚀 GitHub Pages Deployment Helper"
echo "=================================="
echo ""

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "❌ Error: index.html not found. Are you in the right directory?"
    exit 1
fi

echo "📋 Current status:"
echo "  - Repository: pytest-interactive-lessons"
echo "  - Branch: main"
echo "  - Files ready: index.html, README.md"
echo ""

# Check git status
echo "📊 Git status:"
git status --short
echo ""

# Check remote
echo "🔗 Remote URL:"
git remote -v | grep origin | head -n 1
echo ""

# Prompt for action
echo "⚠️  IMPORTANT: Before running this script, make sure you've:"
echo "   1. Created the repository on GitHub: https://github.com/new"
echo "   2. Repository name: pytest-interactive-lessons"
echo "   3. Set to Public (required for free GitHub Pages)"
echo "   4. Did NOT initialize with README"
echo ""

read -p "Have you created the repository on GitHub? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "📝 Next steps:"
    echo "   1. Go to https://github.com/new"
    echo "   2. Create repository 'pytest-interactive-lessons' (Public)"
    echo "   3. Run this script again"
    exit 0
fi

echo ""
echo "🔄 Attempting to push to GitHub..."
echo ""

# Try to push
if git push -u origin main; then
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo ""
    echo "📍 Next steps:"
    echo "   1. Go to https://github.com/Septenal14/pytest-interactive-lessons/settings/pages"
    echo "   2. Enable GitHub Pages:"
    echo "      - Source: Deploy from a branch"
    echo "      - Branch: main / (root)"
    echo "      - Click Save"
    echo "   3. Wait 1-2 minutes for deployment"
    echo "   4. Run: ./verify-deployment.sh"
    echo ""
    echo "🌐 Your site will be available at:"
    echo "   https://septenal14.github.io/pytest-interactive-lessons/"
    echo ""
else
    echo ""
    echo "❌ Push failed. Common issues:"
    echo ""
    echo "1. Authentication required:"
    echo "   - Generate token: https://github.com/settings/tokens"
    echo "   - Select 'repo' scope"
    echo "   - Use token as password when prompted"
    echo ""
    echo "2. Repository doesn't exist:"
    echo "   - Make sure you created it on GitHub"
    echo "   - Name must be exactly: pytest-interactive-lessons"
    echo ""
    echo "3. SSH key not configured:"
    echo "   - Switch to HTTPS: git remote set-url origin https://github.com/Septenal14/pytest-interactive-lessons.git"
    echo "   - Run this script again"
    echo ""
fi
