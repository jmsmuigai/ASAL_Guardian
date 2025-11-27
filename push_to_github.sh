#!/bin/bash

# Automated GitHub Push Script for ASAL-Guardian
# This script pushes your code to GitHub

echo "🚀 Pushing ASAL-Guardian to GitHub"
echo "=================================="
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing git repository..."
    git init
    echo "✅ Git initialized"
fi

# Add all files
echo "📝 Adding files to git..."
git add .

# Check if there are changes to commit
if [ -z "$(git status --porcelain)" ]; then
    echo "✅ No changes to commit"
else
    echo "💾 Committing changes..."
    git commit -m "ASAL-Guardian: Multi-agent drought early warning system

- Three sequential AI agents (Sentinel, Guardian, Responder)
- Flask web interface
- Cloud Run deployment ready
- Comprehensive documentation
- Video generation scripts
- Submission ready for Agents for Good track"
    echo "✅ Changes committed"
fi

# Check if remote exists
if git remote | grep -q "origin"; then
    echo "✅ Remote 'origin' already configured"
    REMOTE_URL=$(git remote get-url origin)
    echo "   URL: $REMOTE_URL"
else
    echo "🔗 Adding GitHub remote..."
    git remote add origin https://github.com/jmsmuigai/ASAL_Guardian.git
    echo "✅ Remote added"
fi

# Set main branch
git branch -M main

# Push to GitHub
echo ""
echo "📤 Pushing to GitHub..."
echo "   (You may be prompted for GitHub credentials)"
echo ""

if git push -u origin main; then
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo ""
    echo "🌐 Your repository is now at:"
    echo "   https://github.com/jmsmuigai/ASAL_Guardian"
    echo ""
    echo "📋 Next steps:"
    echo "   1. Make sure the repository is PUBLIC on GitHub"
    echo "   2. Create your submission video"
    echo "   3. Submit to Kaggle (see SUBMISSION_GUIDE.md)"
    echo ""
else
    echo ""
    echo "❌ Push failed. Common reasons:"
    echo "   - Not logged into GitHub"
    echo "   - Repository doesn't exist on GitHub"
    echo "   - Authentication issues"
    echo ""
    echo "💡 Solutions:"
    echo "   1. Create the repository on GitHub first:"
    echo "      https://github.com/new"
    echo "      Name: ASAL_Guardian"
    echo "      Make it PUBLIC"
    echo ""
    echo "   2. Or use a personal access token:"
    echo "      git remote set-url origin https://YOUR_TOKEN@github.com/jmsmuigai/ASAL_Guardian.git"
    echo ""
fi

