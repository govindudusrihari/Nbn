from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
from transformers import pipeline  # Still using Hugging Face Transformers for now

app = FastAPI()

# Load your Hugging Face model 
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-mrpc")

@app.post("/chat")
async def chat_handler(request: Request):
    try:
        user_message = await request.json()
        user_message = user_message.get('message')

        if not user_message:
            return JSONResponse({"error": "Missing message"}, status_code=400)

        response = classifier(user_message)
        return JSONResponse({"response": response})

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
