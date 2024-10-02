from flask import Flask, request, jsonify
from transformers import pipeline

from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load your Hugging Face model
# Replace 'distilbert-base-uncased-finetuned-mrpc' with your model name
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-mrpc")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    # Process the message with Hugging Face
    response = classifier(user_message)
    # Note: `response` might need further processing depending on the task and model

    # Send the response back to the frontend 
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
app = Flask(__name__)

# Load your Hugging Face model
# Replace 'distilbert-base-uncased-finetuned-mrpc' with your model name
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-mrpc")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    # Process the message with Hugging Face
    response = classifier(user_message)
    # Note: `response` might need further processing depending on the task and model

    # Send the response back to the frontend 
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load your Hugging Face model
# Replace 'distilbert-base-uncased-finetuned-mrpc' with your model name
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-mrpc")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    # Process the message with Hugging Face
    response = classifier(user_message)
    # Note: `response` might need further processing depending on the task and model

    # Send the response back to the frontend 
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
