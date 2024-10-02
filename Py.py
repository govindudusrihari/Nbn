from flask import Flask, request, jsonify

# Example Flask route 
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat_handler():
    try:
        user_message = request.get_json()['message']  # Receive user input
        if not user_message:
            return jsonify({'error': 'Missing message'}), 400
        
        # ... 
        # Process user input, using Gemini or other model

        response =  # Your bot's response 
        return jsonify({'response': response}), 200  #  Send to the front-end

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
