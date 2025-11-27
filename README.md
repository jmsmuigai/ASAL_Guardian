# 🌍 ASAL-Guardian: Multi-Agent Drought Early Warning System

**Competition:** [Agents Intensive - Capstone Project](https://kaggle.com/competitions/agents-intensive-capstone-project)  
**Track:** Agents for Good  
**Problem:** Reducing latency between early warning signals and humanitarian intervention in Kenya's Arid and Semi-Arid Lands (ASALs)  
**Repository:** https://github.com/jmsmuigai/ASAL_Guardian

## 📋 Overview

ASAL-Guardian is an AI-powered multi-agent system designed to monitor drought conditions in Garissa County, Kenya, and automatically generate early warnings and response artifacts. The system uses three specialized AI agents working in sequence:

1. **Sentinel Agent** - Monitors and structures field data (VCI, water distance, market prices)
2. **Guardian Agent** - Analyzes data against NDMA (National Drought Management Authority) thresholds
3. **Responder Agent** - Generates SMS alerts and official briefs for government action

## 🏗️ Architecture

```
┌─────────────────┐
│  Field Data     │
│  (VCI, Prices)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Sentinel Agent  │ ← Gemini 1.5/2.5 Flash (Fast data processing)
│ (Data Ingestion)│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Guardian Agent  │ ← Gemini 1.5/2.5 Pro (Complex reasoning)
│ (Analysis)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Responder Agent │ ← Gemini 1.5/2.5 Pro (Communication)
│ (Action)        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ SMS Alerts &    │
│ Governor Briefs │
└─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google API Key (get one from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Installation (Automated)

**Option 1: Use the setup script (Recommended)**

```bash
chmod +x setup.sh
./setup.sh
```

**Option 2: Manual installation**

```bash
# Install dependencies
pip3 install -r requirements.txt

# Set your API key
export GOOGLE_API_KEY='your_api_key_here'
```

### Running the System

**1. Check available models (Diagnostic)**
```bash
python3 diagnostic.py
```

**2. Run the agent workflow (Command Line)**
```bash
python3 main.py
```

**3. Start the web interface (Flask)**
```bash
python3 app.py
```
Then open your browser to `http://localhost:8080`

## ☁️ Deployment to Google Cloud Run

### Prerequisites
- Google Cloud account
- `gcloud` CLI installed and authenticated

### Deploy Command

```bash
# Set your project
gcloud config set project YOUR_PROJECT_ID

# Deploy to Cloud Run
gcloud run deploy asal-guardian \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY=your_api_key_here
```

After deployment, you'll receive a URL like: `https://asal-guardian-uc.a.run.app`

## 🔧 Technical Details

### Models Used

The system uses Google Gemini models with automatic fallback:
- **Primary:** Gemini 2.5 Flash/Pro (latest)
- **Fallback:** Gemini 1.5 Flash/Pro (if 2.5 unavailable)

### Key Features Demonstrated

✅ **Multi-Agent System** - Three specialized agents working in sequence  
✅ **Model Fallback Logic** - Graceful degradation if newer models unavailable  
✅ **Context Engineering** - NDMA-specific drought thresholds and indicators  
✅ **Tool Integration** - Ready for API integration (VCI data, market prices)  
✅ **Web Interface** - Flask-based UI for easy interaction  
✅ **Cloud Deployment** - Deployable to Google Cloud Run  

### NDMA Drought Thresholds

The Guardian Agent evaluates data against these official thresholds:

**Vegetation Condition Index (VCI):**
- Normal: VCI > 35
- Alert: VCI 20-35
- Alarm: VCI < 20
- Emergency: VCI < 10

**Terms of Trade (ToT):**
- Stable: ToT > 50 kg maize per goat
- Stressed: ToT 30-50
- Crisis: ToT < 30

**Water Distance:**
- Alarm triggered if > 10km to water source

## 📁 Project Structure

```
ASAL_Guardian/
├── main.py                  # Core agent system and orchestration
├── app.py                   # Flask web application
├── diagnostic.py            # Model availability checker
├── generate_video.py        # Video generation script
├── generate_images.py       # Image generation for video
├── requirements.txt         # Python dependencies
├── Procfile                 # Cloud Run deployment config
├── setup.sh                 # Automated setup script
├── run.sh                   # Quick command-line runner
├── run_web.sh               # Quick web interface runner
├── README.md                # This file
├── QUICK_START.md           # Beginner-friendly guide
├── SUBMISSION_GUIDE.md      # Step-by-step submission instructions
├── IMPLEMENTATION_STATUS.md # Implementation details
└── .gcloudignore           # Files to exclude from deployment
```

## 🎯 Value Proposition

**Problem:** Current drought response systems have a latency gap - data is collected monthly, but fund mobilization is bureaucratic and slow.

**Solution:** ASAL-Guardian automates the entire pipeline:
- Real-time monitoring (when connected to live APIs)
- Instant analysis against NDMA thresholds
- Automatic generation of SMS alerts and official briefs
- Reduces response time from weeks to minutes

**Impact:** Transforms drought response from **Reactive** to **Proactive**, potentially saving lives and livestock in pastoralist communities.

## 🔐 Security Notes

⚠️ **IMPORTANT:** Never commit API keys to version control. Always use environment variables or secure secret management in production.

## 🎥 Video Submission

A demonstration video is available on YouTube. The video includes:
- Problem statement and context
- Architecture overview
- Live system demonstration
- Technical implementation details

**Video Requirements Met:**
- ✅ Under 3 minutes
- ✅ Problem Statement
- ✅ Why Agents?
- ✅ Architecture description
- ✅ Live demo
- ✅ Build process

## 📊 Hackathon Requirements

### Required Features (At Least 3)
- ✅ **Multi-agent system** - Three sequential agents (Sentinel, Guardian, Responder)
- ✅ **Tools** - Ready for API integration (VCI data, market prices)
- ✅ **Context engineering** - NDMA-specific drought thresholds coded into agent logic
- ✅ **Agent deployment** - Cloud Run deployment ready

### Bonus Points
- ✅ **Effective Use of Gemini** - Using Gemini 1.5/2.5 models with fallback logic
- ✅ **Agent Deployment** - Cloud Run deployment configuration included
- ✅ **YouTube Video** - Submission video created and uploaded

## 📝 Submission Information

**Competition:** Agents Intensive - Capstone Project  
**Submission Deadline:** December 1, 2025, 11:59 AM Pacific Time  
**Track:** Agents for Good  
**GitHub Repository:** https://github.com/jmsmuigai/ASAL_Guardian

For detailed submission instructions, see [SUBMISSION_GUIDE.md](SUBMISSION_GUIDE.md)

## 🔧 Key Technical Concepts Demonstrated

1. **Multi-Agent System** - Sequential agent workflow with specialized roles
2. **Model Selection** - Smart fallback logic for model availability
3. **Error Handling** - Graceful degradation and comprehensive error messages
4. **Web Integration** - Flask-based REST API and web interface
5. **Cloud Deployment** - Serverless architecture on Google Cloud Run
6. **Context Engineering** - Domain-specific knowledge (NDMA thresholds) embedded in agent prompts
7. **Documentation** - Comprehensive guides for setup, usage, and submission

## 📝 License

This project is submitted for the "Agents for Good" track of the Agents Intensive - Capstone Project competition.

## 🙏 Acknowledgments

- National Drought Management Authority (NDMA) for threshold definitions
- Google Gemini team for the AI models and Agent Development Kit
- The pastoralist communities of Garissa County, Kenya
- Kaggle and Google for organizing the Agents Intensive course

## 📧 Contact

For questions or contributions, please refer to the hackathon submission guidelines or open an issue on GitHub.

---

**Built with ❤️ for the Agents for Good track**

**Competition:** [Agents Intensive - Capstone Project](https://kaggle.com/competitions/agents-intensive-capstone-project)

