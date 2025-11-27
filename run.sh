#!/bin/bash

# Quick run script for ASAL-Guardian
# Automatically activates venv and runs the main workflow

cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run ./setup.sh first"
    exit 1
fi

source venv/bin/activate

# Load .env file if it exists (API key will be loaded automatically)
if [ -f .env ]; then
    echo "✅ Loading API key from .env file..."
    export $(cat .env | grep -v '^#' | xargs)
elif [ -z "$GOOGLE_API_KEY" ]; then
    echo "⚠️  WARNING: GOOGLE_API_KEY not set"
    echo "Please either:"
    echo "  1. Create a .env file with: GOOGLE_API_KEY=your_key_here"
    echo "  2. Or export it: export GOOGLE_API_KEY='your_key_here'"
    exit 1
fi

python main.py

