from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
from allennlp.predictors.predictor import Predictor
from allennlp.models.archival import load_archive

app = FastAPI()

# Load your pre-trained AllenNLP model
archive = load_archive('path/to/your/trained/model.tar.gz')  # Replace with actual path
predictor = Predictor.from_archive(archive)

@app.post("/classify")
async def classify_handler(request: Request):
    try:
        user_message = await request.json()
        user_message = user_message.get('message')

        if not user_message:
            return JSONResponse({"error": "Missing message"}, status_code=400)

        prediction = predictor.predict(user_message)
        category = prediction['label']
        return JSONResponse({"category": category})

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
