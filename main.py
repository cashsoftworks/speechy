from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from datetime import date

# Returns the current local date
today = date.today()

app = Flask(__name__)

# Set your Google Gemini API key
key = "GEMINI-API-KEY"  # Replace with your own key from Google
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Conversation log to store all interactions
conversation_log = []

@app.route('/')
def index():
    # Render the enhanced HTML template
    return render_template('index.html')

@app.route('/api/respond', methods=['POST'])
def respond():
    # Extract the user's speech input from the request
    data = request.json
    text = data['text']

    # Append the latest user input to the conversation log
    conversation_log.append({'user': text})
    rel = """YOURNAMEHERE - Your creator"""
    # Create a summary of the conversation so far
    summary = "\n".join([f"User: {entry['user']}\nAI: {entry.get('ai', '')}" for entry in conversation_log if 'ai' in entry])

    # Send the summary and user input to the AI model
    prompt = f"Please make short human-like responses based on this conversation so far: \n{summary}\n Here are some relationships of you: {rel}\nIt is currently {today} (yyyy-mm-dd). Do not use emojis or markdowns. Now, the user says: {text}"
    
    # Generate a response from the Gemini model
    response = model.generate_content(prompt)
    
    # Store the AI's response in the conversation log
    conversation_log[-1]['ai'] = response.text

    # Return the AI response as JSON
    return jsonify({'response': response.text})

if __name__ == '__main__':
    # Run the Flask app on the specified host and port
    app.run(host='0.0.0.0', port=1024)
