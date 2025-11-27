"""
Generate images for video using Gemini 2.5 Flash Image (Nano Banana)
"""
import os
import google.generativeai as genai
from pathlib import Path

def generate_video_images():
    """Generate images for the submission video."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ GOOGLE_API_KEY not set")
        return
    
    genai.configure(api_key=api_key)
    
    # Create output directory
    output_dir = Path("video_assets/images")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Image prompts for different sections
    image_prompts = [
        {
            "filename": "garissa_drought.jpg",
            "prompt": "Aerial view of arid landscape in Garissa County, Kenya. Dry cracked earth, sparse vegetation, acacia trees, pastoralist community in background. Cinematic, golden hour lighting, showing the severity of drought conditions."
        },
        {
            "filename": "architecture_diagram.jpg",
            "prompt": "Modern technical diagram showing three AI agents connected: Sentinel Agent (data monitoring), Guardian Agent (analysis), Responder Agent (alerts). Clean, professional infographic style, blue and green color scheme, futuristic but accessible."
        },
        {
            "filename": "system_demo.jpg",
            "prompt": "Screenshot-style image of a web dashboard showing drought monitoring data: VCI index at 18.5, water distance 12km, alert status ALARM. Clean UI design, data visualization, professional software interface."
        },
        {
            "filename": "pastoralist_community.jpg",
            "prompt": "Somali pastoralist elder named Ahmed, standing in Garissa County, wearing traditional checkered shuka, looking at a mobile phone with concern, then relief. Cinematic, photorealistic, 8k resolution, golden hour lighting."
        }
    ]
    
    print("🎨 Generating images for video...")
    print("Note: Gemini 2.5 Flash Image may not be available via API yet.")
    print("You may need to use Google AI Studio or Vertex AI for image generation.\n")
    
    # Try to generate images
    # Note: Image generation via API may require Vertex AI or specific model access
    try:
        # Check available models
        models = list(genai.list_models())
        image_models = [m for m in models if 'image' in m.name.lower() or 'imagen' in m.name.lower()]
        
        if image_models:
            print(f"✅ Found image generation models: {[m.name for m in image_models]}")
            # Use the first available image model
            model = genai.GenerativeModel(image_models[0].name)
        else:
            print("⚠️  No image generation models found via API.")
            print("   Alternative: Use Google AI Studio (https://aistudio.google.com/)")
            print("   or create images manually using the prompts below.\n")
            
            # Print prompts for manual use
            print("IMAGE PROMPTS FOR MANUAL GENERATION:")
            print("="*60)
            for img in image_prompts:
                print(f"\n📸 {img['filename']}")
                print(f"   Prompt: {img['prompt']}")
            
            return
        
        # Generate images
        for img in image_prompts:
            try:
                print(f"Generating: {img['filename']}...")
                response = model.generate_content(img['prompt'])
                
                # Save image if response contains image data
                if hasattr(response, 'images') and response.images:
                    image_path = output_dir / img['filename']
                    with open(image_path, 'wb') as f:
                        f.write(response.images[0])
                    print(f"✅ Saved: {image_path}")
                else:
                    print(f"⚠️  Could not generate {img['filename']} - response format unexpected")
            except Exception as e:
                print(f"❌ Error generating {img['filename']}: {e}")
                print(f"   Prompt saved for manual generation: {img['prompt']}")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n📋 MANUAL IMAGE GENERATION:")
        print("1. Go to https://aistudio.google.com/")
        print("2. Use the prompts above to generate images")
        print("3. Save them to video_assets/images/")
        print("\nOr use these prompts with other AI image generators (DALL-E, Midjourney, etc.)")

if __name__ == "__main__":
    generate_video_images()

