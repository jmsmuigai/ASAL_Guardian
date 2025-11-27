"""
ASAL-Guardian Flask Web Application
Deployable to Google Cloud Run for the "Agents for Good" hackathon submission.
"""
from flask import Flask, jsonify, render_template_string
import os
from dotenv import load_dotenv
from main import run_agent_workflow

# Load environment variables from .env file if it exists
load_dotenv()

app = Flask(__name__)

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ASAL-Guardian: Drought Early Warning System</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }
        .header h1 { font-size: 2.5em; margin-bottom: 10px; }
        .header p { font-size: 1.2em; opacity: 0.9; }
        .content {
            padding: 40px;
        }
        .button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 40px;
            font-size: 1.1em;
            border-radius: 50px;
            cursor: pointer;
            transition: transform 0.2s;
            margin: 20px 0;
        }
        .button:hover { transform: scale(1.05); }
        .button:active { transform: scale(0.95); }
        .results {
            margin-top: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            display: none;
        }
        .agent-box {
            margin: 20px 0;
            padding: 20px;
            background: white;
            border-left: 4px solid #667eea;
            border-radius: 5px;
        }
        .agent-box h3 { color: #667eea; margin-bottom: 10px; }
        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌍 ASAL-Guardian</h1>
            <p>Multi-Agent Drought Early Warning System for Garissa County, Kenya</p>
        </div>
        <div class="content">
            <h2>About This System</h2>
            <p>ASAL-Guardian uses three AI agents working together to monitor drought conditions and generate early warnings:</p>
            <ul style="margin: 20px 0; padding-left: 30px;">
                <li><strong>Sentinel Agent:</strong> Monitors and structures field data (VCI, water distance, market prices)</li>
                <li><strong>Guardian Agent:</strong> Analyzes data against NDMA drought thresholds</li>
                <li><strong>Responder Agent:</strong> Generates SMS alerts and official briefs for action</li>
            </ul>
            
            <button class="button" onclick="runWorkflow()">🚀 Run Agent Workflow</button>
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p>Agents are working... This may take 30-60 seconds.</p>
            </div>
            
            <div class="results" id="results">
                <h2>Workflow Results</h2>
                <div id="output"></div>
            </div>
        </div>
    </div>
    
    <script>
        async function runWorkflow() {
            const loading = document.getElementById('loading');
            const results = document.getElementById('results');
            const output = document.getElementById('output');
            const button = event.target;
            
            loading.style.display = 'block';
            results.style.display = 'none';
            button.disabled = true;
            button.textContent = '⏳ Processing...';
            
            try {
                const response = await fetch('/api/run');
                const data = await response.json();
                
                loading.style.display = 'none';
                results.style.display = 'block';
                
                output.innerHTML = `
                    <div class="agent-box">
                        <h3>📡 Sentinel Agent Output</h3>
                        <pre style="white-space: pre-wrap; font-family: monospace;">${data.sentinel_output || 'No data'}</pre>
                    </div>
                    <div class="agent-box">
                        <h3>🛡️ Guardian Agent Analysis</h3>
                        <pre style="white-space: pre-wrap; font-family: monospace;">${data.guardian_output || 'No data'}</pre>
                    </div>
                    <div class="agent-box">
                        <h3>📢 Responder Agent Actions</h3>
                        <pre style="white-space: pre-wrap; font-family: monospace;">${data.responder_output || 'No data'}</pre>
                    </div>
                `;
            } catch (error) {
                loading.style.display = 'none';
                output.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
                results.style.display = 'block';
            } finally {
                button.disabled = false;
                button.textContent = '🚀 Run Agent Workflow';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Main web interface."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/run', methods=['GET', 'POST'])
def api_run():
    """API endpoint to trigger the agent workflow."""
    try:
        result = run_agent_workflow()
        return jsonify({
            "status": "success",
            "sentinel_output": result.get("sentinel_output", ""),
            "guardian_output": result.get("guardian_output", ""),
            "responder_output": result.get("responder_output", "")
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint for Cloud Run."""
    return jsonify({"status": "healthy", "service": "ASAL-Guardian"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)

