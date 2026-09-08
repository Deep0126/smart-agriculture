from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(title="Smart Agriculture ML API")

# Mock Schemas
class CropPredictionRequest(BaseModel):
    nitrogen: float
    phosphorus: float
    potassium: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

class DiseaseDetectionRequest(BaseModel):
    image_url: str

@app.get("/")
def read_root():
    return {"message": "Smart Agriculture ML Service is running"}

@app.post("/predict/crop")
def predict_crop(data: CropPredictionRequest):
    # Mock logic (In reality, we would load .pkl model here)
    crops = ['Rice', 'Maize', 'Chickpea', 'Kidneybeans', 'Pigeonpeas', 'Mothbeans', 'Mungbean', 'Blackgram', 'Lentil', 'Pomegranate', 'Banana', 'Mango', 'Grapes', 'Watermelon', 'Muskmelon', 'Apple', 'Orange', 'Papaya', 'Coconut', 'Cotton', 'Jute', 'Coffee']
    predicted_crop = random.choice(crops)
    return {"predicted_crop": predicted_crop, "confidence": round(random.uniform(70.0, 99.9), 2)}

@app.post("/predict/disease")
def predict_disease(data: DiseaseDetectionRequest):
    # Mock logic for image
    diseases = ['Healthy', 'Leaf Blight', 'Rust', 'Powdery Mildew']
    predicted_disease = random.choice(diseases)
    return {"predicted_disease": predicted_disease, "treatment": "Use fungicide or proper watering."}
