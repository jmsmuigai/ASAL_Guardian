"""
ASAL-Guardian Video Generation Script
Creates a submission video using screen recordings and AI-generated content.
"""
import os
import subprocess
import json
import time
from pathlib import Path

def check_dependencies():
    """Check if required tools are installed."""
    tools = {
        'ffmpeg': 'ffmpeg',
        'python': 'python3'
    }
    missing = []
    for tool, cmd in tools.items():
        try:
            subprocess.run([cmd, '--version'], capture_output=True, check=True)
            print(f"✅ {tool} is installed")
        except (subprocess.CalledProcessError, FileNotFoundError):
            missing.append(tool)
            print(f"❌ {tool} is NOT installed")
    
    if missing:
        print(f"\n⚠️  Missing tools: {', '.join(missing)}")
        print("Install ffmpeg: brew install ffmpeg (on macOS)")
        return False
    return True

def create_video_script():
    """Generate a video script using Gemini."""
    import google.generativeai as genai
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ GOOGLE_API_KEY not set")
        return None
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    
    prompt = """
    Create a compelling 2.5-minute video script for ASAL-Guardian, a multi-agent AI system 
    that monitors drought conditions in Kenya's Garissa County. The script should include:
    
    1. Problem Statement (0:00-0:30): The drought crisis in Garissa, latency in response
    2. Why Agents (0:30-1:00): How multi-agent systems uniquely solve this
    3. Architecture (1:00-1:30): Three agents (Sentinel, Guardian, Responder) working together
    4. Demo (1:30-2:00): Show the system in action
    5. The Build (2:00-2:30): Technologies used (Gemini, Flask, Cloud Run)
    
    Format as JSON with timestamps and narration text. Keep it under 3 minutes total.
    """
    
    try:
        response = model.generate_content(prompt)
        script_text = response.text
        
        # Try to extract JSON if wrapped in markdown
        if '```json' in script_text:
            script_text = script_text.split('```json')[1].split('```')[0]
        elif '```' in script_text:
            script_text = script_text.split('```')[1].split('```')[0]
        
        script = json.loads(script_text)
        return script
    except Exception as e:
        print(f"❌ Error generating script: {e}")
        # Return a default script
        return {
            "title": "ASAL-Guardian: AI-Powered Drought Early Warning System",
            "sections": [
                {
                    "timestamp": "0:00-0:30",
                    "title": "Problem Statement",
                    "narration": "In Kenya's Garissa County, drought response is too slow. Data is collected monthly, but fund mobilization takes weeks. Every day of delay costs lives and livestock."
                },
                {
                    "timestamp": "0:30-1:00",
                    "title": "Why Agents?",
                    "narration": "Multi-agent systems uniquely solve this. Three specialized AI agents work together: Sentinel monitors data, Guardian analyzes threats, Responder generates alerts instantly."
                },
                {
                    "timestamp": "1:00-1:30",
                    "title": "Architecture",
                    "narration": "Our architecture uses three Gemini-powered agents in sequence. Sentinel structures field data, Guardian evaluates against NDMA thresholds, and Responder creates SMS alerts and official briefs."
                },
                {
                    "timestamp": "1:30-2:00",
                    "title": "Demo",
                    "narration": "Watch as the system processes real-time data, detects an ALARM phase, and automatically generates bilingual SMS alerts and a governor's brief in seconds."
                },
                {
                    "timestamp": "2:00-2:30",
                    "title": "The Build",
                    "narration": "Built with Google Gemini models, Flask for the web interface, and deployed on Google Cloud Run. Open source and ready to scale across all ASAL regions."
                }
            ]
        }

def generate_narration_audio(script, output_dir):
    """Generate narration using text-to-speech."""
    print("\n📢 Generating narration audio...")
    
    # Check if gTTS is available
    try:
        from gtts import gTTS
        use_gtts = True
    except ImportError:
        print("⚠️  gTTS not installed. Install with: pip install gtts")
        print("   For now, you'll need to record narration manually or use another TTS service.")
        use_gtts = False
    
    audio_files = []
    if use_gtts:
        for i, section in enumerate(script['sections']):
            audio_file = output_dir / f"narration_{i}.mp3"
            try:
                tts = gTTS(text=section['narration'], lang='en', slow=False)
                tts.save(str(audio_file))
                audio_files.append(audio_file)
                print(f"✅ Generated: {audio_file.name}")
            except Exception as e:
                print(f"❌ Error generating audio {i}: {e}")
                audio_files.append(None)
    else:
        print("📝 Please record narration manually for each section:")
        for i, section in enumerate(script['sections']):
            print(f"\n{i+1}. {section['title']} ({section['timestamp']})")
            print(f"   Text: {section['narration']}")
            audio_file = output_dir / f"narration_{i}.mp3"
            audio_files.append(audio_file)
    
    return audio_files

def create_video_from_screenshots(output_dir):
    """Create video segments from screenshots or screen recordings."""
    print("\n🎬 Creating video segments...")
    
    # Instructions for manual video creation
    instructions = """
    VIDEO CREATION INSTRUCTIONS:
    ============================
    
    To create the submission video, you have two options:
    
    OPTION 1: Screen Recording (Recommended)
    ----------------------------------------
    1. Open your terminal and run: ./run_web.sh
    2. Open http://localhost:8080 in your browser
    3. Use QuickTime Player (macOS) or OBS Studio to record:
       - 0:00-0:30: Show the problem (use images of Garissa drought)
       - 0:30-1:00: Explain the architecture (show diagram)
       - 1:00-1:30: Show code structure (screen recording)
       - 1:30-2:00: Demo the web interface (click "Run Agent Workflow")
       - 2:00-2:30: Show deployment/technologies
    
    4. Save as: demo_segment.mp4
    
    OPTION 2: Use AI-Generated Images + Screen Recording
    ---------------------------------------------------
    1. Generate images using Gemini (see generate_images.py)
    2. Record screen demo of the system
    3. Combine using ffmpeg (see combine_video.py)
    
    The script will help you combine everything once you have the segments.
    """
    
    print(instructions)
    
    # Check for existing video files
    video_files = list(output_dir.glob("*.mp4"))
    if video_files:
        print(f"\n✅ Found video files: {[f.name for f in video_files]}")
        return video_files
    else:
        print("\n⚠️  No video files found. Please create them using the instructions above.")
        return []

def combine_video_segments(video_files, audio_files, script, output_file):
    """Combine video segments with narration."""
    print(f"\n🎞️  Combining video segments into final video: {output_file}")
    
    if not video_files:
        print("❌ No video files to combine. Please create video segments first.")
        return False
    
    # Create a simple ffmpeg command to combine
    # This is a basic version - you may need to adjust based on your video files
    
    try:
        # For now, just copy the first video file as placeholder
        # In production, you'd use ffmpeg to properly combine segments
        if len(video_files) == 1:
            cmd = [
                'ffmpeg', '-i', str(video_files[0]),
                '-c', 'copy',
                str(output_file)
            ]
        else:
            # Create concat file for multiple segments
            concat_file = output_file.parent / 'concat_list.txt'
            with open(concat_file, 'w') as f:
                for vf in video_files:
                    f.write(f"file '{vf.absolute()}'\n")
            
            cmd = [
                'ffmpeg', '-f', 'concat', '-safe', '0',
                '-i', str(concat_file),
                '-c', 'copy',
                str(output_file)
            ]
        
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"✅ Video created: {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error combining video: {e}")
        print("   You may need to manually edit the video using a tool like iMovie or Final Cut Pro")
        return False
    except FileNotFoundError:
        print("❌ ffmpeg not found. Please install it: brew install ffmpeg")
        return False

def main():
    """Main video generation workflow."""
    print("="*60)
    print("🎥 ASAL-Guardian Video Generation")
    print("="*60)
    
    # Create output directory
    output_dir = Path("video_assets")
    output_dir.mkdir(exist_ok=True)
    
    # Check dependencies
    if not check_dependencies():
        print("\n⚠️  Some dependencies are missing. Please install them first.")
        return
    
    # Generate script
    print("\n📝 Generating video script...")
    script = create_video_script()
    if script:
        script_file = output_dir / "video_script.json"
        with open(script_file, 'w') as f:
            json.dump(script, f, indent=2)
        print(f"✅ Script saved: {script_file}")
        print("\n📄 Script Preview:")
        print(json.dumps(script, indent=2))
    
    # Generate narration
    audio_files = generate_narration_audio(script, output_dir)
    
    # Create video segments
    video_files = create_video_from_screenshots(output_dir)
    
    # Combine everything
    if video_files:
        output_file = Path("ASAL_Guardian_Submission_Video.mp4")
        combine_video_segments(video_files, audio_files, script, output_file)
        print(f"\n✅ Final video should be at: {output_file}")
        print("\n📋 Next Steps:")
        print("1. Review the video")
        print("2. Upload to YouTube")
        print("3. Add the YouTube URL to your Kaggle submission")
    else:
        print("\n📋 Next Steps:")
        print("1. Create video segments (see instructions above)")
        print("2. Run this script again to combine them")
        print("3. Upload to YouTube")
        print("4. Add YouTube URL to Kaggle submission")

if __name__ == "__main__":
    main()

