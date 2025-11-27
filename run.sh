#!/bin/bash

# Quick run script for ASAL-Guardian
# Automatically activates venv and runs the main workflow

cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run ./setup.sh first"
    exit 1
fi

source venv/bin/activate

if [ -z "$GOOGLE_API_KEY" ]; then
    echo "⚠️  WARNING: GOOGLE_API_KEY not set"
    echo "Please set it with: export GOOGLE_API_KEY='your_key_here'"
    exit 1
fi

python main.py

