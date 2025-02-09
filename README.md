

# House Price Prediction

This FastAPI-based machine learning API predicts house prices based on various input features.

## 🚀 Features
- **Prediction Model**: Utilizes an XGBoost model to predict house prices.
- **API Framework**: Built with FastAPI for efficient API endpoints.
- **Standardization**: Standardizes and inverse transforms price predictions using a pre-trained scaler.
- **Interactive Web Interface**: Includes a user-friendly `index.html`.

## 🌐 Live Demo
You can access the live API at: [https://ml-7-nj3n.onrender.com/](https://ml-7-nj3n.onrender.com/)

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- Git

### Steps to Install

1. **Clone the repository**:
   ```bash
   git clone https://github.com/haile2967/ML.git
   cd house-price-api
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the FastAPI server**:
   ```bash
   uvicorn app:app --reload
   ```

4. **Open the API docs in your browser**:
   - Interactive Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Alternative Docs: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🛠 API Endpoints

### 1. Home Page
- **GET** `/`
  - Serves the static `index.html` page.

### 2. Predict House Price
- **POST** `/predict`
  - **Request Body (JSON)**:
    ```json
    {
      "beds": 3,
      "baths": 2,
      "size": 1500,
      "lot_size": 5000,
      "zip_code": 94103
    }
    ```
  - **Response**:
    ```json
    {
      "prediction": 750000.0
    }
    ```

## 📂 Project Structure
```
├── static/
│   ├── index.html (Frontend UI)
├── app.py (FastAPI backend)
├── requirements.txt (Dependencies)
├── xgboost_model.pkl (Trained ML model)
├── standard_scaler.pkl (Scaler for price transformation)
├── train.csv (Training data)
├── finalPro.ipynb (Model training notebook)
```

## 🛠 Dependencies
This project requires the following Python libraries:
- `fastapi`
- `uvicorn`
- `numpy`
- `pydantic`
- `joblib`
- `scikit-learn`
- `xgboost`

## 🏗 Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## 📜 License
This project is licensed under the MIT License.

## 📧 Contact
Feel free to reach out at [desu3096@gmail.com](mailto:desu3096@gmail.com) for any inquiries!
