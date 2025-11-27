# 📝 Kaggle Submission Writeup

## Title (80 characters max)
**ASAL-Guardian: AI-Powered Drought Early Warning for Kenya's ASAL Regions**

## Subtitle (140 characters max)
**Multi-agent AI system reducing drought response latency from weeks to minutes, transforming humanitarian aid from reactive to proactive**

---

## Project Description (1500 words max)

### Problem Statement

In Kenya's Garissa County, drought isn't just a weather pattern—it's a life-or-death crisis affecting over 800,000 people. The National Drought Management Authority (NDMA) collects critical data monthly: Vegetation Condition Index (VCI) from satellite imagery, water source distances from field reports, and market prices from local traders. This data flows through bureaucratic channels, committees meet, budgets are approved, and funds are mobilized. By the time humanitarian aid reaches pastoralist communities, **weeks have passed**.

In those weeks, livestock die. Families go hungry. Children suffer from malnutrition. The current system is **reactive**—it responds to crises after they've escalated. We need a system that's **proactive**—one that detects threats early and triggers response instantly.

The problem isn't lack of data. The problem is **latency**—the gap between early warning signals and humanitarian intervention. ASAL-Guardian closes that gap.

### Why Agents?

Drought management isn't a single task—it's a complex workflow requiring distinct cognitive capabilities that a monolithic system can't handle effectively:

1. **Data Ingestion & Structuring** - Raw field reports are messy, unstructured, and inconsistent. They need intelligent parsing to extract VCI indices, water distances, and market prices.

2. **Expert Analysis** - Requires deep knowledge of NDMA protocols, drought science, and economic indicators. The system must evaluate multiple variables (VCI, water distance, Terms of Trade) against official thresholds.

3. **Contextual Communication** - Must generate culturally appropriate, actionable alerts. SMS messages for pastoralists need to be bilingual (English/Swahili) and concise. Government briefs need formal language and urgency.

A single agent trying to do all three would be a jack-of-all-trades, master of none. But **three specialized agents**, each optimized for their role? That's where multi-agent systems shine.

**Sentinel Agent** uses Gemini 2.5 Flash for lightning-fast data processing. It ingests messy field reports and structures them into clean JSON in seconds. It doesn't make decisions—it just reports facts.

**Guardian Agent** uses Gemini 2.5 Pro for complex reasoning. It's programmed with real NDMA thresholds and drought science. It evaluates structured data, calculates drought phases (Normal/Alert/Alarm/Emergency), determines economic status (Stable/Stressed/Crisis), and provides expert reasoning.

**Responder Agent** uses Gemini 2.5 Pro for communication. It transforms Guardian's analysis into actionable artifacts: bilingual SMS alerts for pastoralists and formal briefs for government officials. Each output is tailored to its audience.

This sequential workflow—Sentinel → Guardian → Responder—ensures each agent does what it does best. The result? **Intelligent orchestration** that's faster, more accurate, and more reliable than any single-agent approach.

### What You Created

**Architecture Overview:**

The system is built as a modular Python application with three core components:

1. **Agent Orchestration Layer** (`main.py`):
   - Base `Agent` class handles model initialization with system instructions (personas)
   - `SentinelAgent` specializes in data ingestion and structuring
   - `Guardian` agent performs expert analysis
   - `Responder` agent generates communication artifacts
   - `get_available_model()` implements intelligent model selection with fallback
   - `run_agent_workflow()` orchestrates the sequential flow

2. **Web Interface** (`app.py`):
   - Flask-based REST API with `/api/run` endpoint
   - Modern, responsive web UI for interactive testing
   - Health check endpoint for Cloud Run deployment

3. **Deployment Infrastructure**:
   - `Procfile` for Google Cloud Run
   - Environment variable management via `.env` files
   - Comprehensive error handling and logging

**Technical Highlights:**

**Model Selection with Fallback:**
The system intelligently selects the best available Gemini model:
- Primary: Gemini 2.5 Flash/Pro (latest capabilities)
- Automatic fallback to Gemini 1.5 if 2.5 unavailable
- Ensures reliability across different API access levels

**Context Engineering:**
The Guardian Agent is programmed with real NDMA thresholds:
- VCI thresholds: Normal (>35), Alert (20-35), Alarm (<20), Emergency (<10)
- Terms of Trade: Stable (>50), Stressed (30-50), Crisis (<30)
- Water Distance: Alarm if >10km

This domain expertise is embedded in the agent's system instructions, making it a true expert system—not a generic chatbot.

**Error Handling:**
- Graceful degradation if models unavailable
- Comprehensive error messages
- Safe API key management (never committed to git)

**Security:**
- API keys stored in `.env` files (gitignored)
- Environment variable loading via `python-dotenv`
- No hardcoded secrets

### Demo

The system works as follows:

1. **Sentinel Agent** receives a field report:
   ```
   Field Report - Garissa County - October 2025
   Vegetation Index (3-month) is currently at 18.5.
   Pastoralists reporting trekking 12km to water sources.
   Goat prices have dropped to 2500 KES.
   Maize prices are stable at 100 KES per kg.
   ```

2. **Sentinel** structures it into JSON:
   ```json
   {
     "VCI": 18.5,
     "WaterDistance_km": 12,
     "TermsOfTrade_GoatToMaize_kg": 25
   }
   ```

3. **Guardian Agent** analyzes against NDMA thresholds:
   - VCI 18.5 < 20 → ALARM phase
   - Water Distance 12km > 10km → ALARM confirmed
   - ToT 25 < 30 → CRISIS economic status
   
   Output: `{"drought_phase": "ALARM", "economic_status": "CRISIS", "reasoning": "..."}`

4. **Responder Agent** generates artifacts:
   - **SMS Alert:** "NDMA ALERT: Kukosa maji kwa umakini. VCI 18.5. Tafadhali wasiliana na ofisi ya kaunti. / Drought alert: Water scarcity critical. VCI 18.5. Contact county office."
   - **Governor's Brief:** "Garissa County is in ALARM drought phase with VCI at 18.5 and water distances exceeding 12km. Economic status is CRISIS with Terms of Trade at 25 kg maize per goat. Urgent activation of County Drought Contingency Fund required."

**Live Demo Available:**
- Web interface: Run `./run_web.sh` and visit `http://localhost:8080`
- Command line: Run `./run.sh` for terminal output
- GitHub: https://github.com/jmsmuigai/ASAL_Guardian

### The Build

**Technologies Used:**

1. **Google Gemini Models:**
   - Gemini 2.5 Flash for fast data processing (Sentinel)
   - Gemini 2.5 Pro for complex reasoning (Guardian, Responder)
   - Automatic fallback to Gemini 1.5 for compatibility

2. **Python Ecosystem:**
   - `google-generativeai` for Gemini API integration
   - `flask` for web interface
   - `gunicorn` for production deployment
   - `python-dotenv` for environment management

3. **Infrastructure:**
   - Google Cloud Run for serverless deployment
   - Virtual environment for dependency isolation
   - Git for version control

**Development Process:**

1. **Problem Research:** Studied NDMA drought management protocols, Garissa County context, and humanitarian response workflows.

2. **Architecture Design:** Designed three-agent sequential workflow based on distinct cognitive requirements.

3. **Implementation:**
   - Built base `Agent` class with model initialization
   - Implemented specialized agents with domain-specific instructions
   - Added model fallback logic for reliability
   - Created Flask web interface for testing

4. **Testing & Refinement:**
   - Tested with real NDMA threshold scenarios
   - Validated output quality and accuracy
   - Refined agent instructions based on results

5. **Deployment Preparation:**
   - Configured Cloud Run deployment
   - Implemented secure API key management
   - Created comprehensive documentation

**Key Design Decisions:**

- **Sequential vs Parallel:** Chose sequential workflow because Guardian needs Sentinel's structured data, and Responder needs Guardian's analysis. Parallel processing would break dependencies.

- **Model Selection:** Used Flash for Sentinel (speed) and Pro for Guardian/Responder (reasoning). This optimizes cost and performance.

- **Context Engineering:** Embedded NDMA thresholds directly in agent instructions rather than external config files. This ensures the knowledge is always available and reduces complexity.

### If I Had More Time, This Is What I'd Do

1. **Real-Time Data Integration:**
   - Connect to actual VCI satellite APIs (NASA MODIS, USGS)
   - Integrate with market price APIs
   - Set up automated data ingestion pipelines

2. **Advanced Features:**
   - Historical trend analysis (detect accelerating deterioration)
   - Multi-county monitoring (scale across all ASAL regions)
   - Predictive modeling (forecast drought progression)

3. **Communication Channels:**
   - Direct SMS integration (Twilio, WhatsApp API)
   - Email alerts to government officials
   - Dashboard for real-time monitoring

4. **Production Hardening:**
   - Database integration (Cloud SQL) for session storage
   - Comprehensive logging and observability
   - A/B testing for alert effectiveness
   - User feedback loops

5. **Impact Measurement:**
   - Track response times before/after deployment
   - Measure reduction in livestock mortality
   - Monitor malnutrition rates
   - Calculate economic impact

**The Vision:** Scale ASAL-Guardian across all 23 ASAL counties in Kenya, then expand to other drought-prone regions in the Horn of Africa. Transform humanitarian response from reactive to proactive, saving lives and livelihoods through early intervention.

---

## Submission Form Fields

### Title
ASAL-Guardian: AI-Powered Drought Early Warning for Kenya's ASAL Regions

### Subtitle
Multi-agent AI system reducing drought response latency from weeks to minutes

### Card and Thumbnail Image
Use a screenshot of the web interface showing the three agents, or create a professional infographic showing the architecture.

### Submission Track
**Agents for Good**

### Media Gallery
[YouTube Video URL - Add your video here]

### Project Description
[Copy the full description above - 1500 words]

### Attachments
**GitHub Repository:** https://github.com/jmsmuigai/ASAL_Guardian

---

**Word Count:** ~1,200 words (well under 1,500 limit)

