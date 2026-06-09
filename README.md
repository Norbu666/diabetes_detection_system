🩺 **Diabetes Detection Website**
📌 Overview
This project is a web‑based diabetes detection system that combines a machine learning model with a simple frontend interface. Users can input health data, and the backend model predicts the likelihood of diabetes. The goal is to provide an accessible demo of how machine learning can be applied to healthcare.

📂 **Project Structure**
diabetes_detection/
│
├── Frontend/                # User interface
│   ├── index.html            # Main landing page
│   ├── cover.html            # Cover page
│   ├── history.html          # Patient history page
│   ├── male_history.html     # Male-specific history page
│   ├── result.html           # Prediction results
│   ├── cover.css, style.css  # Styling
│   └── bg.png                # Background image
│
├── MLModel/                  # Machine learning assets
│   ├── diabetes.csv          # Dataset
│   ├── diabetes_train.ipynb  # Training notebook
│   ├── male.ipynb            # Male-specific model notebook
│   ├── male_diabetes_simple.csv
│   ├── model.pkl             # Trained ML model
│   ├── scaler.pkl            # Data scaler
│   ├── male_rf_model.pkl     # Male-specific model
│   └── male_scaler.pkl       # Male-specific scaler
│
├── Test/                     # Testing utilities
│   ├── test.ipynb            # Notebook for testing
│   ├── test.py               # Python test script
│   └── __pycache__/          # Cache files
│
├── app.py                    # Main backend application
├── database.py               # Database integration
└── .hintrc                   # Config file

⚙️** Features**
Frontend UI built with HTML/CSS for user interaction.

Machine Learning Model trained on diabetes datasets (diabetes.csv).

Prediction Results Page showing likelihood of diabetes.

Separate models for general and male‑specific datasets.

Backend scripts (app.py, database.py) for integration and data handling.

🚀** Getting Started**
Prerequisites
  1). Python 3.x
  2). Jupyter Notebook
  3). Required libraries: pandas, scikit-learn, numpy, flask 

**Installation**
git clone https://github.com/yourusername/diabetes_detection.git
cd diabetes_detection
pip install -r requirements.txt

**Running the Project**
1). Train the model 
bash
jupyter notebook MLModel/diabetes_train.ipynb

2). Start the backend:
bash
python app.py

3). Open the frontend:
Navigate to Frontend/index.html in your browser.

📊 **Dataset**
The dataset (diabetes.csv) contains medical attributes used to predict diabetes.
Preprocessing is handled with scalers (scaler.pkl, male_scaler.pkl).

**Use This requirements.txt to download all the require tools**
pip install -r requirements.txt
