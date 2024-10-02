from flask import Flask, request, jsonify
from transformers import pipeline
import torch
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator

app = Flask(__name__)

# Load your Hugging Face model 
# (replace 'distilbert-base-uncased-finetuned-mrpc' with your model name)
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-mrpc")

# Define the tokenizer (you can customize this)
tokenizer = get_tokenizer('basic_english')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    # Preprocess using PyTorch Text
    tokens = tokenizer(user_message)
    preprocessed_message = ' '.join(tokens)

    # Process the message with Hugging Face
    response = classifier(preprocessed_message)

    # Send the response back to the frontend
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
