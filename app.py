from flask import Flask, request, jsonify, render_template
import requests
import json
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

class LLMAssistant:
    def __init__(self):
        self.base_url = "http://localhost:11434/api"
        self.models = {
            "deepseek": "deepseek-r1:latest",
            "qwen": "qwen2.5:7b"
        }
        self.conversation_history = []
        
    def generate_response(self, prompt, model="deepseek"):
        if model not in self.models:
            logger.error(f"Invalid model selection: {model}")
            return {"error": "Invalid model selection"}
            
        # Prepare the conversation context
        context = "\n".join(self.conversation_history[-5:])
        
        # Prepare the request to Ollama
        data = {
            "model": self.models[model],
            "prompt": f"{context}\nHuman: {prompt}\nAssistant:",
            "stream": False
        }
        
        try:
            logger.info(f"Sending request to Ollama API for model {self.models[model]}")
            logger.debug(f"Request data: {json.dumps(data, indent=2)}")
            
            response = requests.post(f"{self.base_url}/generate", json=data)
            logger.debug(f"Response status code: {response.status_code}")
            logger.debug(f"Response content: {response.text[:500]}")  # Log first 500 chars of response
            
            response.raise_for_status()
            result = response.json()
            
            # Store the exchange in conversation history
            self.conversation_history.append(f"Human: {prompt}")
            self.conversation_history.append(f"Assistant: {result['response']}")
            
            return {"response": result['response']}
            
        except requests.exceptions.ConnectionError as e:
            error_msg = f"Connection error - Is Ollama running? Error: {str(e)}"
            logger.error(error_msg)
            return {"error": error_msg}
        except requests.exceptions.RequestException as e:
            error_msg = f"Error communicating with Ollama: {str(e)}"
            logger.error(error_msg)
            return {"error": error_msg}
        except json.JSONDecodeError as e:
            error_msg = f"Error parsing Ollama response: {str(e)}"
            logger.error(error_msg)
            return {"error": error_msg}
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            logger.error(error_msg)
            return {"error": error_msg}

assistant = LLMAssistant()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        logger.info(f"Received chat request: {data}")
        
        prompt = data.get('prompt')
        model = data.get('model', 'deepseek')
        
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400
            
        response = assistant.generate_response(prompt, model)
        return jsonify(response)
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/clear', methods=['POST'])
def clear_history():
    assistant.conversation_history = []
    return jsonify({"status": "success"})

if __name__ == '__main__':
    logger.info("Starting Flask application...")
    app.run(debug=True)