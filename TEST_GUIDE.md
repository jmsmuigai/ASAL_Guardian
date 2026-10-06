# 🧪 Testing Guide: How to Test Your Agents

## Step-by-Step Testing Instructions

### Step 1: Open Your Terminal

Open Terminal (on Mac: Press `Cmd + Space`, type "Terminal", press Enter)

---

### Step 2: Navigate to Your Project

Type this command and press Enter:

```bash
cd /Users/james/Desktop/ASAL_Guardian
```

**What should happen:**
- Your terminal prompt changes to show you're in the ASAL_Guardian folder
- No error messages

---

### Step 3: Activate the Virtual Environment

Type this command and press Enter:

```bash
source venv/bin/activate
```

**What should happen:**
- You see `(venv)` appear at the start of your terminal prompt
- It looks like: `(venv) james@MacBook ASAL_Guardian %`

**If you see an error:**
- Make sure you're in the right directory (Step 2)
- The venv folder should exist (it was created during setup)

---

### Step 4: Set Your API Key

**First, get your API key:**
1. Go to: https://makersuite.google.com/app/apikey
2. Copy your API key (it looks like: `AIzaSy...`)

**Then, in your terminal, type:**

```bash
export GOOGLE_API_KEY='paste_your_key_here'
```

**Important:** Replace `paste_your_key_here` with your actual API key!

**Example:**
```bash
export GOOGLE_API_KEY='your_new_key_here'
```

**What should happen:**
- No error message
- The command completes silently

**To verify it's set:**
```bash
echo $GOOGLE_API_KEY
```
You should see your key (or the first part of it)

---

### Step 5: Run the Diagnostic (Optional but Recommended)

This checks if your API key works and shows available models:

```bash
python diagnostic.py
```

**What should happen:**
- You see "✅ [SYSTEM] Google AI API Key configured."
- A list of available models appears
- Models like "models/gemini-1.5-flash" or "models/gemini-2.5-flash" are listed

**If you see errors:**
- Check that your API key is correct
- Make sure you have internet connection
- Try the key again in Google AI Studio to verify it works

---

### Step 6: Test the Main Agent System

Now let's test the actual agents! Type:

```bash
python main.py
```

**What should happen:**

1. **System Initialization:**
   ```
   ✅ [SYSTEM] Found API Key starting with: AIzaSy...
   ✅ [SYSTEM] Google AI API Key configured.
   ```

2. **Agent Initialization:**
   ```
   ============================================================
   🚀 INITIATING ASAL-GUARDIAN MULTI-AGENT WORKFLOW...
   ============================================================
      - Initializing Sentinel with model models/gemini-...
      - Initializing Guardian with model models/gemini-...
      - Initializing Responder with model models/gemini-...
   ✅ [SYSTEM] All agents initialized.
   ```

3. **Sentinel Agent Working:**
   ```
   📡 [Sentinel] Fetching live data from simulated field reports...
   ✅ [Sentinel] Raw data received.
   🧠 [Sentinel is thinking...]
   ✅ [Sentinel responded.]
   ```

4. **Guardian Agent Working:**
   ```
   🧠 [Guardian is thinking...]
   ✅ [Guardian responded.]
   ```

5. **Responder Agent Working:**
   ```
   🧠 [Responder is thinking...]
   ✅ [Responder responded.]
   ```

6. **Final Results:**
   ```
   --- SENTINEL OUTPUT (Structured Data) ---
   [JSON data with VCI, water distance, prices]
   
   --- GUARDIAN OUTPUT (Analysis) ---
   [Analysis showing drought phase, economic status]
   
   --- RESPONDER OUTPUT (Action Artifacts) ---
   📱 SMS Alert:
   [Bilingual SMS alert]
   
   📝 Governor's Brief:
   [Formal brief for the governor]
   
   ✅ WORKFLOW COMPLETE. System shutting down.
   ```

**Total time:** About 30-60 seconds (the agents need time to think!)

---

## ✅ Success Indicators

You'll know it's working if you see:

- ✅ All three agents initialize successfully
- ✅ Each agent shows "is thinking..." then "responded"
- ✅ You see structured output from each agent
- ✅ Final SMS alert and Governor's brief are generated
- ✅ No error messages (except maybe warnings about model fallback)

---

## ❌ Common Problems & Solutions

### Problem 1: "GOOGLE_API_KEY environment variable not found"

**Solution:**
- Make sure you ran: `export GOOGLE_API_KEY='your_key'`
- Make sure you're in the same terminal session
- Try setting it again

### Problem 2: "404 model not found"

**Solution:**
- This is normal! The system will automatically use a fallback model
- You'll see a warning like "⚠️ Warning: Preferred models not found. Using fallback: ..."
- The system will still work with the fallback model

### Problem 3: "Connection error" or "Network error"

**Solution:**
- Check your internet connection
- Make sure you're not behind a firewall blocking Google APIs
- Try again in a few minutes

### Problem 4: "Module not found" errors

**Solution:**
- Make sure you activated the virtual environment: `source venv/bin/activate`
- You should see `(venv)` in your prompt
- If still not working, run: `pip install -r requirements.txt`

### Problem 5: "Permission denied" when running scripts

**Solution:**
- Make scripts executable: `chmod +x run.sh`
- Or use: `python main.py` directly

---

## 🎯 Quick Test Command (All-in-One)

If you want to do everything in one go, here's a complete command sequence:

```bash
cd /Users/james/Desktop/ASAL_Guardian && \
source venv/bin/activate && \
export GOOGLE_API_KEY='your_key_here' && \
python main.py
```

(Replace `your_key_here` with your actual API key!)

---

## 📊 What Each Agent Does

**Sentinel Agent:**
- Takes messy field report data
- Structures it into clean JSON
- Extracts: VCI, water distance, goat prices, maize prices

**Guardian Agent:**
- Receives structured data from Sentinel
- Compares against NDMA drought thresholds
- Determines: drought phase (ALARM/ALERT/NORMAL) and economic status

**Responder Agent:**
- Receives analysis from Guardian
- Generates: SMS alert (bilingual) and Governor's brief
- Creates actionable communication artifacts

---

## 🎉 Next Steps After Testing

Once your test works:

1. ✅ **Test the web interface:**
   ```bash
   python app.py
   ```
   Then open: http://localhost:8080

2. ✅ **Push to GitHub:**
   ```bash
   ./push_to_github.sh
   ```

3. ✅ **Create your video:**
   ```bash
   python generate_video.py
   ```

4. ✅ **Submit to Kaggle!**

---

## 💡 Pro Tips

- **Keep the terminal open** - Don't close it between commands
- **Check the output carefully** - The agents show what they're doing
- **First run is slower** - Models need to load, be patient!
- **Save your API key** - You'll need it every time (or add it to ~/.zshrc)

---

**Need more help?** Check `QUICK_START.md` or `README.md`!

