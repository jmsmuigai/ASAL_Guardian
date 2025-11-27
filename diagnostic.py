import google.generativeai as genai
import os

print("--- DIAGNOSTIC START: Querying Available Models ---")

try:
    # Ensure API Key is set
    api_key = os.environ["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    print("✅ [SYSTEM] Google AI API Key configured.")

    available_models = []
    print("\n🔍 Searching for models that support 'generateContent'...")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print("-" * 30)
            print(f"✅ Found Usable Model: {m.name}")
            print(f"    Display Name: {m.display_name}")
            print(f"    Version: {m.version}")
            available_models.append(m.name)
            
    if not available_models:
        print("\n❌ ERROR: No content generation models found for your API key.")
        print("   Troubleshooting:")
        print("   1. Check if the API Key is correct and has 'Generative Language API' enabled.")
        print("   2. Check the region/project associated with your key.")
        print("   3. Ensure you have accepted the terms of service in Google AI Studio.")
    else:
        print("-" * 30)
        print(f"\n✅ DIAGNOSTIC COMPLETE. Found {len(available_models)} usable models.")
        print("   Use one of the 'Found Usable Model' strings in your code.")

except KeyError:
    print("❌ CRITICAL ERROR: GOOGLE_API_KEY environment variable not found.")
    print("   Please set the key using: export GOOGLE_API_KEY='your_key_here'")
except Exception as e:
    print(f"\n❌ CONNECTION ERROR: An error occurred while trying to list models.")
    print(f"   Error details: {e}")
    print("\n   Troubleshooting:")
    print("   - Check your internet connection and firewall settings.")
    print("   - Verify that the API key is valid and not expired.")

print("\n--- DIAGNOSTIC END ---")
