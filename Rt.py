import os
import requests

# Replace with your actual API key
api_key = os.getenv('AIzaSyB3zVLrNM6XoHn_iQQ-ROQ2lkIOQIl1Jb0')

# Set the API endpoint
api_endpoint = "https://api.gemini.ai/v1/chat"

# Define the payload with your prompt
payload = {
  "prompt": "What is the meaning of life?",
  "model": "gemini" 
}

# Set headers
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

# Make the API request
response = requests.post(api_endpoint, json=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    response_json = response.json()
    print(response_json["text"])
else:
    print(f"Request failed with status code {response.status_code}.")
    print(response.text)
