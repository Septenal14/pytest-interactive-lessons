#!/bin/bash

# GitHub Pages Deployment Verification Script
# Run this after enabling GitHub Pages

URL="https://septenal14.github.io/pytest-interactive-lessons/"

echo "🔍 Verifying GitHub Pages deployment..."
echo "URL: $URL"
echo ""

# Check if site is accessible
echo "1. Checking if site is live..."
if curl -s -o /dev/null -w "%{http_code}" "$URL" | grep -q "200"; then
    echo "✅ Site is accessible (HTTP 200)"
else
    echo "❌ Site is not accessible yet (wait 1-2 minutes after enabling Pages)"
    exit 1
fi

echo ""
echo "2. Checking for key elements..."

# Download the page
PAGE_CONTENT=$(curl -s "$URL")

# Check for Mermaid.js
if echo "$PAGE_CONTENT" | grep -q "mermaid.min.js"; then
    echo "✅ Mermaid.js is loaded"
else
    echo "❌ Mermaid.js not found"
fi

# Check for quiz functionality
if echo "$PAGE_CONTENT" | grep -q "checkAnswer"; then
    echo "✅ Quiz functionality present"
else
    echo "❌ Quiz functionality not found"
fi

# Check for main content sections
if echo "$PAGE_CONTENT" | grep -q "Введение в Pytest"; then
    echo "✅ Main content loaded"
else
    echo "❌ Main content not found"
fi

echo ""
echo "3. Final URL for Skill Space:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "$URL"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 Next steps:"
echo "1. Open URL in browser to visually verify"
echo "2. Test the quiz interaction"
echo "3. Verify Mermaid diagram renders correctly"
echo "4. Copy URL to Skill Space materials"
