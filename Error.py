from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post('/chat')
async def chat(request: Request):
  user_message = await request.json()
  # ... (Your logic to process the message and generate a response)
  response = {
    'response': 'This is a response from the FastAPI server.'
  }
  return JSONResponse(response)
