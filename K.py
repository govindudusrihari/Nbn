# ... (Your existing Python code) ...

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_data = request.json
        user_message = user_data.get('message')

        # Check if user typed "hi"
        if user_message.lower() == 'hi':
            bot_response = 'Breathe in, breathe out.'
        else:
            # Make a request to the Gemini API 
            # ... (Your existing Gemini API call) ...

        return jsonify({'message': bot_response})
    except Exception as e:
        return jsonify({'message': f'Error: {e}'}), 500

# ... (Rest of your Python code) ...
