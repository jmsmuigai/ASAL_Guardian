# 🌍 ASAL-Guardian: Multi-Agent Drought Early Warning System

**Competition:** [Agents Intensive - Capstone Project](https://kaggle.com/competitions/agents-intensive-capstone-project)  
**Track:** Agents for Good  
**Repository:** https://github.com/jmsmuigai/ASAL_Guardian

---

## 📋 Overview

ASAL-Guardian is an AI-powered multi-agent system designed to monitor drought conditions in Garissa County, Kenya, and automatically generate early warnings and response artifacts. The system uses three specialized AI agents working in sequence to transform drought response from reactive to proactive, reducing response time from weeks to minutes.

**Impact:** Potentially saving lives and livestock in pastoralist communities through early intervention.

---

## 🏗️ Architecture

The system implements a sequential multi-agent workflow:

```
Field Data → Sentinel Agent → Guardian Agent → Responder Agent → Alerts & Briefs
```

**Sentinel Agent** (Gemini 2.5 Flash) - Fast data ingestion and structuring  
**Guardian Agent** (Gemini 2.5 Pro) - Expert analysis against NDMA thresholds  
**Responder Agent** (Gemini 2.5 Pro) - Bilingual communication generation

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google API Key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

```bash
git clone https://github.com/jmsmuigai/ASAL_Guardian.git
cd ASAL_Guardian
./setup.sh
echo "GOOGLE_API_KEY=your_key_here" > .env
```

### Running

```bash
# Command line
./run.sh

# Web interface
./run_web.sh
# Then open http://localhost:8080
```

---

## 🔧 Technical Implementation

### Key Features Demonstrated

✅ **Multi-Agent System** - Three sequential agents with specialized roles  
✅ **Context Engineering** - NDMA-specific drought thresholds embedded in agent logic  
✅ **Tools** - Ready for API integration (VCI data, market prices)  
✅ **Agent Deployment** - Cloud Run deployment configuration included  

### Code Quality

- Comprehensive comments explaining implementation, design, and behaviors
- Clean architecture with separation of concerns
- Error handling at every level
- Production-ready deployment configuration

---

## 📊 Hackathon Requirements

### Required Features (3+ Required)
- ✅ Multi-agent system (Sequential agents)
- ✅ Context engineering (NDMA thresholds)
- ✅ Tools (API integration ready)
- ✅ Agent deployment (Cloud Run)

### Bonus Points
- ✅ Effective Use of Gemini (2.5 models with fallback)
- ✅ Agent Deployment (Cloud Run configuration)
- ✅ YouTube Video (Submission video)

---

## 📁 Project Structure

```
ASAL_Guardian/
├── main.py              # Core multi-agent system
├── app.py               # Flask web application
├── diagnostic.py         # Model availability checker
├── requirements.txt     # Dependencies
├── Procfile            # Cloud Run deployment
├── README.md           # This file
└── FINAL_SUBMISSION.md # Complete Kaggle submission content
```

---

## 🎯 Value Proposition

**Problem:** Drought response systems have a latency gap—data collected monthly, fund mobilization takes weeks.

**Solution:** ASAL-Guardian automates the pipeline:
- Real-time monitoring (when APIs connected)
- Instant analysis against NDMA thresholds
- Automatic generation of SMS alerts and official briefs
- Reduces response time from weeks to minutes

**Impact:** Transforms drought response from reactive to proactive.

---

## 📝 Submission

**Competition:** Agents Intensive - Capstone Project  
**Deadline:** December 1, 2025, 11:59 AM Pacific Time  
**Track:** Agents for Good

For complete submission content, see `FINAL_SUBMISSION.md`

---

## 🔐 Security

- API keys stored in `.env` (never committed to git)
- Environment variable management via `python-dotenv`
- No hardcoded secrets

---

## 🙏 Acknowledgments

- National Drought Management Authority (NDMA) for threshold definitions
- Google Gemini team for AI models
- The pastoralist communities of Garissa County, Kenya
- Kaggle and Google for organizing the Agents Intensive course

---

**Built with ❤️ for the Agents for Good track**
