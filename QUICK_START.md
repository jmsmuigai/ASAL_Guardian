# 🚀 Quick Start Guide (Like You're 10 Years Old!)

Hey! Want to run this cool AI system that helps people in Kenya? Let's do it step by step!

## Step 1: Get Your Magic Key 🔑

You need a special key from Google to talk to the AI. It's like a password that lets you use their smart computers.

1. Go to: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key (it looks like: `AIzaSy...`)

## Step 2: Tell Your Computer About the Key 💻

Open your terminal (the black window where you type commands) and type:

```bash
export GOOGLE_API_KEY='paste_your_key_here'
```

**Important:** Replace `paste_your_key_here` with your actual key!

## Step 3: Install Everything (Automatic!) 📦

Just run this one command:

```bash
./setup.sh
```

This script is like a robot helper that:
- Checks if you have Python (the programming language)
- Creates a special "box" (virtual environment) for our project
- Downloads all the tools we need

Wait for it to finish! It might take 1-2 minutes.

## Step 4: Test It! 🧪

Let's make sure everything works:

```bash
./run.sh
```

This will:
1. Turn on the AI agents
2. Make them check some fake data about drought
3. Show you what they found

You should see messages like:
- ✅ [SYSTEM] Found API Key...
- 📡 [Sentinel] Fetching live data...
- 🧠 [Guardian is thinking...]
- 📱 SMS Alert: ...

## Step 5: Use the Web Interface! 🌐

Want a pretty website instead of the terminal? Run:

```bash
./run_web.sh
```

Then open your web browser and go to: `http://localhost:8080`

You'll see a nice page with a button. Click "Run Agent Workflow" and watch the magic happen!

## Troubleshooting (When Things Go Wrong) 🔧

### "Command not found: ./setup.sh"
- Make sure you're in the right folder: `cd /Users/james/Desktop/ASAL_Guardian`
- Make it executable: `chmod +x setup.sh`

### "GOOGLE_API_KEY not set"
- You forgot Step 2! Go back and set your key.
- Or add it to your `~/.zshrc` file so it's always there:
  ```bash
  echo 'export GOOGLE_API_KEY="your_key_here"' >> ~/.zshrc
  source ~/.zshrc
  ```

### "404 model not found"
- Run the diagnostic: `python diagnostic.py` (with venv activated)
- It will show you which models work with your key
- The code will automatically use the best available model

### "Permission denied"
- Make scripts executable: `chmod +x *.sh`

## What's Next? 🎯

Once everything works:
1. ✅ You've completed the setup!
2. 📝 Read the full README.md for more details
3. ☁️ Deploy to Google Cloud Run (see README.md)
4. 🎥 Create your submission video!

## Remember! 💡

- Always activate the virtual environment first: `source venv/bin/activate`
- Keep your API key secret! Don't share it or put it in code.
- Have fun! This is a real system that could help real people! 🌍

