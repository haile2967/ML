House Price Prediction API

This is a FastAPI-based machine learning API that predicts house prices based on input features such as the number of bedrooms, bathrooms, size, lot size, and zip code.
The model used for prediction is an XGBoost model trained on historical housing data.

🚀 Features

Predict house prices using an XGBoost model

Uses FastAPI for API endpoints

Standardizes and inverse transforms price predictions using a pre-trained scaler

Includes an interactive web interface (index.html)

📦 Installation

Clone the repository:

git clone [https://github.com/haile2967/ML.git]
cd house-price-api

Install dependencies:

pip install -r requirements.txt

Start the FastAPI server:

uvicorn app:app --reload

Open the API docs in your browser:

Interactive Docs: http://127.0.0.1:8000/docs

Alternative Docs: http://127.0.0.1:8000/redoc

🛠 API Endpoints

1. Home Page

GET / → Serves the static index.html page

2. Predict House Price

POST /predict

Request Body (JSON):

{
  "beds": 3,
  "baths": 2,
  "size": 1500,
  "lot_size": 5000,
  "zip_code": 94103
}

Response:

{
  "prediction": 750000.0
}

📂 Project Structure

├── static/
│   ├── index.html (Frontend UI)
├── app.py (FastAPI backend)
├── requirements.txt (Dependencies)
├── xgboost_model.pkl (Trained ML model)
├── standard_scaler.pkl (Scaler for price transformation)
├── train.csv (Training data)
├── finalPro.ipynb (Model training notebook)

🛠 Dependencies

This project requires the following Python libraries:

fastapi
uvicorn
numpy
pydantic
joblib
scikit-learn
xgboost

🏗 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

📜 License

This project is licensed under the MIT License.

📧 Contact
[desu3096@gmail.com] 
Feel free to reach out!

