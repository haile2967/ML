from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
# Load your trained model and scaler
model = joblib.load('xgboost_model.pkl')
price_scaler = joblib.load('standard_scaler.pkl')  # Load the scaler used to standardize 'price'

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend's origin for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class InputData(BaseModel):
    beds: float
    baths: float
    size: float
    lot_size: float
    zip_code: int



@app.post("/predict")
def predict(data: InputData):
    try: # Prepare the input data as a numpy array
            input_data = np.array([[data.beds, data.baths, data.size, data.lot_size, data.zip_code]])

            # Make a prediction
            prediction = model.predict(input_data).reshape(-1, 1)  # Ensure 2D shape

            # Create a placeholder array with the same shape as training data
            placeholder = np.zeros((1, 6))  # Assuming 6 features were used for scaling
            placeholder[0, -1] = prediction[0, 0]  # Place prediction in last column

            # Inverse transform only the price column
            actual_price = price_scaler.inverse_transform(placeholder)[0, -1]  # Extract real price

            # return {"prediction": float(actual_price)}
            return JSONResponse(content={"prediction": actual_price})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.get("/")
async def read_root():
    return FileResponse("static/index.html")