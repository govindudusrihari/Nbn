import os
import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your actual API key

def get_gemini_response(prompt):
  """
  Get a response from Gemini API
  """
  response = openai.ChatCompletion.create(
      model="gpt-4",  # Use the Gemini Pro model
      messages=[{"role": "user", "content": prompt}],
  )
  return response.choices[0].message.content

# Example prompt
prompt = "Write a poem about a cat."

response = get_gemini_response(prompt)
print(response)
