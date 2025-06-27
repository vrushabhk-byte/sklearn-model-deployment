from fastapi import FastAPI, Request
from app.preprocess import preprocess_input
import joblib

app = FastAPI()

# Load model
model = joblib.load("model/model.pkl")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
async def predict(request: Request):
    input_data = await request.json()
    processed = preprocess_input(input_data)
    prediction = model.predict([processed])
    return {"prediction": prediction.tolist()}
