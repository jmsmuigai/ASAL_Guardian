import google.generativeai as genai
import json
import os
import time

# --- Configuration ---
# Ensure API Key is set in your environment variables
try:
    api_key = os.environ["GOOGLE_API_KEY"]
    print(f"✅ [SYSTEM] Found API Key starting with: {api_key[:8]}...")
    genai.configure(api_key=api_key)
    print("✅ [SYSTEM] Google AI API Key configured.")
except KeyError:
    print("❌ CRITICAL ERROR: GOOGLE_API_KEY environment variable not found.")
    print("   Please set the key using: export GOOGLE_API_KEY='your_key_here'")
    exit() # Exit if the key is not found

class Agent:
    """
    Base class for ASAL-Guardian Agents.
    Handles model initialization and safe content generation.
    """
    def __init__(self, name, model_name, instructions):
        self.name = name
        self.model_name = model_name
        self.instructions = instructions
        print(f"   - Initializing {self.name} with model {self.model_name}...")
        try:
            self.model = genai.GenerativeModel(
                model_name=self.model_name,
                system_instruction=self.instructions
            )
        except Exception as e:
            print(f"❌ CRITICAL: Failed to initialize {self.name}. Error: {e}")
            self.model = None

    def think_and_act(self, input_data):
        """
        Sends data to the model and retrieves the response.
        """
        if not self.model:
            return f"Error: {self.name} model is not initialized."
            
        print(f"\n🧠 [{self.name} is thinking...]")
        time.sleep(1) # Cinematic pause
        try:
            response = self.model.generate_content(input_data)
            print(f"✅ [{self.name} responded.]")
            return response.text
        except Exception as e:
            print(f"❌ [{self.name} Error]: {e}")
            return f"Error processing request: {e}"

# --- AGENT 1: THE SENTINEL ---
# Role: Fetches and cleans data.
sentinel_instructions = """
You are the Sentinel. Your job is to ingest raw data and structure it.
You do not make decisions. You only report facts formatted as a single, clean JSON object.
Focus on: VCI (Vegetation Condition Index), Water Distance, and Terms of Trade.
The input will be a messy field report. Extract the key numbers.
"""

class SentinelAgent(Agent):
    def fetch_live_data(self):
        # SIMULATION: In a real app, this would query live APIs or scrape websites.
        print("\n📡 [Sentinel] Fetching live data from simulated field reports...")
        time.sleep(1.5)
        raw_data = """
        Field Report - Garissa County - October 2025
        Vegetation Index (3-month) is currently at 18.5.
        Pastoralists reporting trekking 12km to water sources, up from 8km last month.
        Goat prices have dropped to 2500 KES at the local market.
        Maize prices are stable at 100 KES per kg.
        """
        print("✅ [Sentinel] Raw data received.")
        return self.think_and_act(f"Extract the key metrics from this report and format as JSON: {raw_data}")


# --- AGENT 2: THE GUARDIAN ---
# Role: The Brain. Compares data to NDMA Thresholds.
guardian_instructions = """
You are the Guardian, an expert drought analyst for the NDMA.
You will receive JSON data from the Sentinel agent. You must evaluate it against these thresholds:
1. DROUGHT PHASE:
   - 'ALARM' if VCI < 20 OR Water Distance > 10km.
   - 'ALERT' if VCI is 20-35.
   - 'NORMAL' if VCI > 35.
2. ECONOMIC STATUS:
   - Calculate Terms of Trade (ToT) = Goat Price / Maize Price.
   - If ToT < 30, the status is 'CRISIS'.
   - If ToT is 30-50, the status is 'STRESSED'.
   - If ToT > 50, the status is 'STABLE'.

Output a structured JSON analysis with three keys: 'drought_phase', 'economic_status', and 'reasoning'.
The reasoning should be a short, clear sentence explaining your conclusion.
"""

# --- AGENT 3: THE RESPONDER ---
# Role: Action. Writes the artifacts.
responder_instructions = """
You are the Responder. You are a communications expert for a humanitarian agency.
You will receive a JSON analysis from the Guardian agent. Based on this analysis, generate two communication artifacts inside a single JSON object:
1. 'sms_alert': A short, bilingual (English and Swahili) SMS alert for pastoralists. It must be under 160 characters. Start with "NDMA ALERT:".
2. 'governor_brief': A formal, single-paragraph brief for the County Governor. It should state the drought phase, the economic impact, and urgently request the activation of the County Drought Contingency Fund.
"""

def get_available_model(preferred_models):
    """
    Try to find an available model from a list of preferred models.
    Falls back gracefully if newer models aren't available.
    """
    try:
        available_models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)
        
        for preferred in preferred_models:
            if preferred in available_models:
                return preferred
        
        # Fallback to first available model
        if available_models:
            print(f"⚠️  Warning: Preferred models not found. Using fallback: {available_models[0]}")
            return available_models[0]
        else:
            raise Exception("No available models found")
    except Exception as e:
        print(f"⚠️  Warning: Could not list models. Using first preferred: {preferred_models[0]}")
        return preferred_models[0]

def run_agent_workflow():
    """
    This is the main orchestration loop that ties the agents together.
    """
    print("\n" + "="*60)
    print("🚀 INITIATING ASAL-GUARDIAN MULTI-AGENT WORKFLOW...")
    print("="*60)

    # 1. Initialize Agents with fallback logic
    # Try newer models first, fall back to 1.5 if needed
    sentinel_model = get_available_model([
        "models/gemini-2.5-flash",
        "models/gemini-1.5-flash",
        "models/gemini-1.5-pro"
    ])
    
    guardian_model = get_available_model([
        "models/gemini-2.5-pro",
        "models/gemini-1.5-pro",
        "models/gemini-1.5-flash"
    ])
    
    responder_model = get_available_model([
        "models/gemini-2.5-pro",
        "models/gemini-1.5-pro",
        "models/gemini-1.5-flash"
    ])
    
    sentinel = SentinelAgent("Sentinel", sentinel_model, sentinel_instructions)
    guardian = Agent("Guardian", guardian_model, guardian_instructions)
    responder = Agent("Responder", responder_model, responder_instructions)
    
    print("\n✅ [SYSTEM] All agents initialized.")
    print("="*60)

    # 2. Execution Flow
    # Step A: Sentinel gets and structures the data
    structured_data_json = sentinel.fetch_live_data()
    print("\n--- SENTINEL OUTPUT (Structured Data) ---")
    print(structured_data_json)
    print("----------------------------------------")


    # Step B: Guardian analyzes the data
    analysis_json = guardian.think_and_act(structured_data_json)
    print("\n--- GUARDIAN OUTPUT (Analysis) ---")
    print(analysis_json)
    print("------------------------------------")

    # Step C: Responder takes action
    actions_json = responder.think_and_act(analysis_json)
    print("\n--- RESPONDER OUTPUT (Action Artifacts) ---")
    # Try to parse and print nicely
    try:
        actions = json.loads(actions_json.replace("```json", "").replace("```", ""))
        print("\n📱 SMS Alert:")
        print(actions.get('sms_alert', 'Not generated'))
        print("\n📝 Governor's Brief:")
        print(actions.get('governor_brief', 'Not generated'))
    except (json.JSONDecodeError, AttributeError):
        print(actions_json) # Print raw if not valid JSON
    print("------------------------------------------")
    
    print("\n" + "="*60)
    print("✅ WORKFLOW COMPLETE. System shutting down.")
    print("="*60)
    
    # For Flask integration as described in the document
    return {
        "sentinel_output": structured_data_json,
        "guardian_output": analysis_json,
        "responder_output": actions_json
    }


if __name__ == "__main__":
    run_agent_workflow()
