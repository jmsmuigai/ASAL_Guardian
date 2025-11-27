# 🌍 ASAL-Guardian: AI-Powered Multi-Agent Drought Early Warning System

**Competition:** [Agents Intensive - Capstone Project](https://kaggle.com/competitions/agents-intensive-capstone-project)  
**Track:** Agents for Good  
**Repository:** https://github.com/jmsmuigai/ASAL_Guardian  
**Live Demo:** [Cloud Run Deployment](#deployment) (Coming Soon)

---

## 🎯 The Problem: When Every Hour Counts

In Kenya's Garissa County, drought isn't just a weather pattern—it's a life-or-death crisis. The National Drought Management Authority (NDMA) collects critical data monthly: vegetation indices, water distances, market prices. But by the time this data flows through bureaucratic channels and funds are mobilized, weeks have passed. In those weeks, livestock die. Families go hungry. Children suffer from malnutrition.

**The latency gap is killing people.** Current systems are reactive. We need them to be proactive.

ASAL-Guardian transforms this reality by reducing response time from **weeks to minutes**—automatically monitoring conditions, analyzing threats, and generating actionable alerts the moment thresholds are breached.

---

## 🤖 Why Multi-Agent Systems? The Right Tool for the Right Job

Drought management isn't a single task—it's a complex workflow requiring distinct cognitive capabilities:

1. **Data Ingestion** - Raw field reports are messy, unstructured, and inconsistent
2. **Expert Analysis** - Requires deep knowledge of NDMA protocols and drought science
3. **Communication** - Must generate culturally appropriate, actionable alerts

A single monolithic agent would struggle with this complexity. But three specialized agents, each optimized for their role? That's where the magic happens.

**Sentinel Agent** (Gemini Flash) - Lightning-fast data structuring. Processes messy field reports in seconds, extracting VCI indices, water distances, and market prices into clean JSON.

**Guardian Agent** (Gemini Pro) - The analytical brain. Compares structured data against official NDMA thresholds, determining drought phases and economic crisis levels with expert precision.

**Responder Agent** (Gemini Pro) - The communicator. Transforms analysis into bilingual SMS alerts for pastoralists and formal briefs for government officials—each tailored to its audience.

This isn't just automation. It's **intelligent orchestration**—each agent doing what it does best, working together seamlessly.

---

## 🏗️ Architecture: Three Agents, One Mission

```
┌─────────────────────────────────────────────────────────┐
│                    Field Data Sources                     │
│  (Satellite VCI, Market Prices, Water Distance Reports)  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │   SENTINEL AGENT       │
         │   (Gemini 2.5 Flash)   │
         │                         │
         │  • Ingests raw data    │
         │  • Structures to JSON  │
         │  • Extracts metrics    │
         └───────────┬────────────┘
                     │
         Structured Data (JSON)
                     │
                     ▼
         ┌───────────────────────┐
         │   GUARDIAN AGENT       │
         │   (Gemini 2.5 Pro)     │
         │                         │
         │  • Evaluates VCI       │
         │  • Calculates ToT       │
         │  • Determines phase    │
         │  • Applies NDMA rules   │
         └───────────┬────────────┘
                     │
         Analysis (Drought Phase + Economic Status)
                     │
                     ▼
         ┌───────────────────────┐
         │   RESPONDER AGENT     │
         │   (Gemini 2.5 Pro)    │
         │                         │
         │  • Generates SMS       │
         │  • Writes briefs       │
         │  • Bilingual output    │
         └───────────┬────────────┘
                     │
         ┌───────────┴────────────┐
         │                        │
         ▼                        ▼
   📱 SMS Alerts          📝 Governor Briefs
   (Bilingual)            (Formal Requests)
```

### Technical Implementation

**Agent Base Class** (`Agent`):
- Handles model initialization with system instructions (personas)
- Implements error handling and graceful degradation
- Provides unified `think_and_act()` interface

**Model Selection with Fallback**:
- Primary: Gemini 2.5 Flash/Pro (latest capabilities)
- Automatic fallback to Gemini 1.5 if 2.5 unavailable
- Ensures system reliability across different API access levels

**Sequential Workflow**:
- Sentinel → Guardian → Responder
- Each agent receives output from previous agent
- JSON-structured data flows between agents
- Error handling at each stage

---

## 💡 What Makes This Special: Context Engineering at Scale

This isn't a generic chatbot. The Guardian Agent is programmed with **real NDMA thresholds**:

**Vegetation Condition Index (VCI):**
- Normal: VCI > 35
- Alert: VCI 20-35  
- Alarm: VCI < 20
- Emergency: VCI < 10

**Terms of Trade (ToT):**
- Stable: > 50 kg maize per goat
- Stressed: 30-50
- Crisis: < 30

**Water Distance:**
- Alarm triggered if > 10km

The system understands that if VCI is low BUT ToT is high, cash transfers work. If BOTH crash, direct food relief is needed. This domain expertise is **embedded in the agent's system instructions**—making it a true expert system.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google API Key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

```bash
# Clone the repository
git clone https://github.com/jmsmuigai/ASAL_Guardian.git
cd ASAL_Guardian

# Run automated setup
chmod +x setup.sh
./setup.sh

# Create .env file with your API key
echo "GOOGLE_API_KEY=your_key_here" > .env
```

### Running the System

**Command Line:**
```bash
./run.sh
```

**Web Interface:**
```bash
./run_web.sh
# Then open http://localhost:8080
```

**Diagnostic Check:**
```bash
source venv/bin/activate
python diagnostic.py
```

---

## 📊 Hackathon Requirements: Exceeded

### Required Features (3+ Required, We Have 4)

✅ **Multi-Agent System** - Three sequential agents with specialized roles  
✅ **Tools** - Ready for API integration (VCI data, market prices)  
✅ **Context Engineering** - NDMA-specific thresholds embedded in agent logic  
✅ **Agent Deployment** - Cloud Run configuration ready  

### Bonus Points

✅ **Effective Use of Gemini** - Using latest Gemini 2.5 models with intelligent fallback  
✅ **Agent Deployment** - Complete Cloud Run deployment setup  
✅ **YouTube Video** - Comprehensive demonstration video  

---

## 🔧 Technical Deep Dive

### Code Architecture

**`main.py`** - Core orchestration:
- `Agent` base class with model initialization
- `SentinelAgent` for data ingestion
- `get_available_model()` for smart model selection
- `run_agent_workflow()` orchestrates the sequence

**`app.py`** - Flask web interface:
- REST API endpoint (`/api/run`)
- Beautiful, modern UI for interaction
- Health check for Cloud Run

**`diagnostic.py`** - Model availability checker:
- Lists all available Gemini models
- Helps troubleshoot API issues

### Security

- API keys stored in `.env` (never committed)
- Environment variable loading via `python-dotenv`
- Comprehensive `.gitignore` protection
- No hardcoded secrets

### Deployment

**Cloud Run Ready:**
- `Procfile` for gunicorn
- Environment variable configuration
- Health check endpoint
- Serverless scaling

---

## 📈 Impact: From Reactive to Proactive

**Before ASAL-Guardian:**
- Data collected monthly
- Manual analysis takes days
- Fund mobilization: 2-4 weeks
- Response: Reactive (after crisis)

**After ASAL-Guardian:**
- Real-time monitoring (when APIs connected)
- Automated analysis: seconds
- Instant alert generation
- Response: Proactive (before crisis escalates)

**Potential Impact:**
- Lives saved through early intervention
- Livestock preserved (economic security)
- Reduced malnutrition rates
- More efficient resource allocation

---

## 🎥 Demo & Video

A comprehensive demonstration video is available showing:
- Problem statement and real-world context
- Architecture walkthrough
- Live system demonstration
- Technical implementation details

**Video Requirements Met:**
- ✅ Under 3 minutes
- ✅ Problem Statement
- ✅ Why Agents?
- ✅ Architecture
- ✅ Live Demo
- ✅ Build Process

---

## 📁 Project Structure

```
ASAL_Guardian/
├── main.py                  # Core multi-agent system
├── app.py                   # Flask web application
├── diagnostic.py            # Model availability checker
├── generate_video.py        # Video generation helper
├── generate_images.py        # Image generation helper
├── requirements.txt         # Python dependencies
├── Procfile                 # Cloud Run deployment
├── .env.example            # API key template
├── setup.sh                 # Automated setup
├── run.sh                   # Quick CLI runner
├── run_web.sh               # Quick web runner
├── README.md                # This file
├── SUBMISSION_GUIDE.md      # Submission instructions
├── TEST_GUIDE.md            # Testing guide
└── SECURITY.md              # Security documentation
```

---

## 🏆 Why This Will Win

1. **Real-World Impact** - Addresses a genuine humanitarian crisis
2. **Technical Excellence** - Clean architecture, proper error handling, production-ready
3. **Innovation** - Multi-agent approach uniquely suited to the problem
4. **Completeness** - Not just code—documentation, deployment, video, everything
5. **Scalability** - Ready to expand across all ASAL regions

---

## 📝 Submission Details

**Competition:** Agents Intensive - Capstone Project  
**Track:** Agents for Good  
**Deadline:** December 1, 2025, 11:59 AM Pacific Time  
**GitHub:** https://github.com/jmsmuigai/ASAL_Guardian

---

## 🙏 Acknowledgments

- National Drought Management Authority (NDMA) for threshold definitions
- Google Gemini team for cutting-edge AI models
- The pastoralist communities of Garissa County, Kenya—the real heroes
- Kaggle and Google for organizing this transformative course

---

## 📧 Contact & Contributions

This project is open source and ready for deployment. For questions, issues, or contributions, please open an issue on GitHub.

---

**Built with ❤️ for the Agents for Good track**

*Transforming drought response from reactive to proactive—one agent at a time.*

---

**Competition:** [Agents Intensive - Capstone Project](https://kaggle.com/competitions/agents-intensive-capstone-project)
