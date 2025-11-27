#!/bin/bash

# ASAL-Guardian Auto-Setup Script
# This script installs dependencies and checks your environment

echo "🌍 ASAL-Guardian Setup Script"
echo "=============================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip."
    exit 1
fi

echo "✅ pip3 found"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies. Please check your internet connection."
    exit 1
fi

echo "✅ Dependencies installed successfully!"
echo ""

# Check for API key
if [ -z "$GOOGLE_API_KEY" ]; then
    echo "⚠️  WARNING: GOOGLE_API_KEY environment variable is not set."
    echo ""
    echo "To set it, run:"
    echo "  export GOOGLE_API_KEY='your_api_key_here'"
    echo ""
    echo "Or add it to your ~/.zshrc or ~/.bashrc file:"
    echo "  echo 'export GOOGLE_API_KEY=\"your_api_key_here\"' >> ~/.zshrc"
    echo "  source ~/.zshrc"
    echo ""
else
    echo "✅ GOOGLE_API_KEY is set (starting with: ${GOOGLE_API_KEY:0:8}...)"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Make sure GOOGLE_API_KEY is set: export GOOGLE_API_KEY='your_key_here'"
echo "3. Run: python diagnostic.py  (to check available models)"
echo "4. Run: python main.py  (to test the agent system)"
echo "5. Run: python app.py  (to start the web server)"
echo ""
echo "Note: Always activate the virtual environment first with: source venv/bin/activate"
echo ""

