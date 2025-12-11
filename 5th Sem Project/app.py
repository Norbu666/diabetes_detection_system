from flask import Flask, render_template, request, send_from_directory
import joblib
import numpy as np
import os

from database import (
    save_prediction, get_all_predictions,
    save_male_prediction, get_male_predictions
)

app = Flask(__name__, static_folder='Frontend', template_folder='Frontend')

# Load models and scalers
general_model = joblib.load("MLModel/model.pkl")
general_scaler = joblib.load("MLModel/scaler.pkl")

male_model = joblib.load("MLModel/male_rf_model.pkl")
male_scaler = joblib.load("MLModel/male_scaler.pkl")

print("Both models loaded successfully!")


# HOME PAGE
@app.route('/')
def home():
    return send_from_directory('Frontend', 'cover.html')


# FEMALE / GENERAL PREDICTION
@app.route('/predict', methods=['POST'])
def predict():

    preg = float(request.form['Pregnancies'])
    glucose = float(request.form['Glucose'])
    bp = float(request.form['BloodPressure'])
    skin = float(request.form['SkinThickness'])
    insulin = float(request.form['Insulin'])
    bmi = float(request.form['BMI'])
    dpf = float(request.form['DiabetesPedigreeFunction'])
    age = float(request.form['Age'])

    input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    scaled = general_scaler.transform(input_data)
    prediction = general_model.predict(scaled)[0]

    result = "Diabetic 😔" if prediction == 1 else "Non-Diabetic 😀"

    save_prediction({
        "preg": preg,
        "glucose": glucose,
        "bp": bp,
        "skin": skin,
        "insulin": insulin,
        "bmi": bmi,
        "dpf": dpf,
        "age": age,
        "result": result
    })

    return render_template("result.html", prediction_result=result, history_type="female")


# MALE PREDICTION
@app.route('/predict_male', methods=['POST'])
def predict_male():

    age = float(request.form["age"])
    hypertension = float(request.form["hypertension"])
    heart = float(request.form["heart_disease"])
    smoking = request.form["smoking_history"]
    bmi = float(request.form["bmi"])
    hba1c = float(request.form["hba1c"])
    glucose = float(request.form["blood_glucose"])

    smoking_map = {"never": 3, "current": 0, "former": 1, "No Info": 2}
    smoke_val = smoking_map.get(smoking, 2)

    gender_val = 1

    input_data = np.array([[gender_val, age, hypertension, heart,
                            smoke_val, bmi, hba1c, glucose]])

    scaled = male_scaler.transform(input_data)
    prediction = male_model.predict(scaled)[0]

    result = "Diabetic 😔" if prediction == 1 else "Non-Diabetic 😀"

    save_male_prediction({
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart,
        "smoking": smoking,
        "bmi": bmi,
        "hba1c": hba1c,
        "glucose": glucose,
        "result": result
    })

    return render_template("result.html", prediction_result=result, history_type="male")


# FEMALE HISTORY
@app.route('/history')
def history():
    records = get_all_predictions()
    return render_template("history.html", records=records)


# MALE HISTORY
@app.route('/male_history')
def male_history():
    records = get_male_predictions()
    return render_template("male_history.html", records=records)


# STATIC FILES
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('Frontend', filename)


if __name__ == '__main__':
    app.run(debug=True)
