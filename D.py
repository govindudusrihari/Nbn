from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

# Gemini API Configuration (REPLACE THESE)
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"  
GEMINI_MODEL = "gemini-1.5-flash-latest"  
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/"

@app.post("/chat")
async def chat_handler(request: Request):
    try:
        user_message = await request.json()
        user_message = user_message.get('message')

        if not user_message:
            return JSONResponse({"error": "Missing message"}, status_code=400)

        # Query Gemini 
        gemini_response = query_gemini(user_message)
        return JSONResponse({"response": gemini_response})

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

def query_gemini(text):
    """Sends a query to the Gemini API and returns the response."""
    url = f"{GEMINI_URL}{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{"parts": [{"text": text}]}]
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        return response_data["candidates"][0]["content"]
    else:
        raise Exception(f"Gemini API request failed with status code {response.status_code}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
