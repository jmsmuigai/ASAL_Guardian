#!/bin/bash

# ASAL-Guardian Submission Preparation Script
# This script prepares everything for submission

echo "🚀 ASAL-Guardian Submission Preparation"
echo "======================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if we're in the right directory
if [ ! -f "main.py" ]; then
    echo -e "${RED}❌ Error: main.py not found. Are you in the ASAL_Guardian directory?${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Found project files${NC}"
echo ""

# Check for API key
if [ -z "$GOOGLE_API_KEY" ]; then
    echo -e "${YELLOW}⚠️  WARNING: GOOGLE_API_KEY not set${NC}"
    echo "   The system will work, but you need to set it for testing."
    echo "   Set it with: export GOOGLE_API_KEY='your_key_here'"
    echo ""
else
    echo -e "${GREEN}✅ GOOGLE_API_KEY is set${NC}"
    echo ""
fi

# Check git status
if [ -d ".git" ]; then
    echo "📦 Checking Git status..."
    git status --short
    
    # Check if there are uncommitted changes
    if [ -n "$(git status --porcelain)" ]; then
        echo ""
        echo -e "${YELLOW}⚠️  You have uncommitted changes${NC}"
        read -p "Do you want to commit them now? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            git add .
            git commit -m "Prepare for submission: Final updates and documentation"
            echo -e "${GREEN}✅ Changes committed${NC}"
        fi
    else
        echo -e "${GREEN}✅ All changes committed${NC}"
    fi
    
    # Check remote
    if git remote | grep -q "origin"; then
        echo -e "${GREEN}✅ Git remote configured${NC}"
        REMOTE_URL=$(git remote get-url origin)
        echo "   Remote: $REMOTE_URL"
    else
        echo -e "${YELLOW}⚠️  No git remote configured${NC}"
        echo "   To add remote: git remote add origin https://github.com/jmsmuigai/ASAL_Guardian.git"
    fi
else
    echo -e "${YELLOW}⚠️  Not a git repository${NC}"
    echo "   Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit: ASAL-Guardian multi-agent system"
    echo -e "${GREEN}✅ Git repository initialized${NC}"
fi

echo ""
echo "📋 Submission Checklist:"
echo "========================"
echo ""

# Check items
CHECKS=(
    "main.py exists"
    "app.py exists"
    "README.md exists"
    "requirements.txt exists"
    "SUBMISSION_GUIDE.md exists"
)

ALL_GOOD=true

for check in "${CHECKS[@]}"; do
    if [ -f "${check%% *}" ] || [ -f "${check}" ]; then
        echo -e "${GREEN}✅ $check${NC}"
    else
        echo -e "${RED}❌ $check${NC}"
        ALL_GOOD=false
    fi
done

echo ""
echo "🔍 Additional Checks:"
echo "====================="

# Check for API keys in code
if grep -r "AIza" --include="*.py" --include="*.sh" . 2>/dev/null | grep -v ".git" | grep -v "venv"; then
    echo -e "${RED}❌ WARNING: Potential API keys found in code!${NC}"
    echo "   Please remove any hardcoded API keys"
    ALL_GOOD=false
else
    echo -e "${GREEN}✅ No API keys found in code${NC}"
fi

# Check if .gitignore exists
if [ -f ".gitignore" ]; then
    echo -e "${GREEN}✅ .gitignore exists${NC}"
else
    echo -e "${YELLOW}⚠️  .gitignore not found (recommended)${NC}"
fi

echo ""
echo "📝 Next Steps:"
echo "=============="
echo ""
echo "1. Test the system:"
echo "   source venv/bin/activate"
echo "   python main.py"
echo ""
echo "2. Push to GitHub:"
echo "   git push -u origin main"
echo ""
echo "3. Create video (see SUBMISSION_GUIDE.md)"
echo ""
echo "4. Submit to Kaggle:"
echo "   https://www.kaggle.com/competitions/agents-intensive-capstone-project"
echo ""

if [ "$ALL_GOOD" = true ]; then
    echo -e "${GREEN}✅ All checks passed! You're ready to submit!${NC}"
else
    echo -e "${YELLOW}⚠️  Some checks failed. Please review before submitting.${NC}"
fi

echo ""
echo "📖 For detailed instructions, see SUBMISSION_GUIDE.md"
echo ""

