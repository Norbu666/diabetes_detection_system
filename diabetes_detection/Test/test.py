import joblib
import numpy as np


model = joblib.load("male_rf_model.pkl")
scaler = joblib.load("male_scaler.pkl")

smoking_map = {"never": 3, "current": 0, "former": 1, "No Info": 2}

age = 21
gender_val = 1 
hypertension = 0
heart_disease = 0
smoking_history = "never"
bmi = 22.5
hba1c = 6.2
glucose = 155

smoke_val = smoking_map[smoking_history]

input_data = np.array([[gender_val, age, hypertension,
                        heart_disease, smoke_val,
                        bmi, hba1c, glucose]])

scaled_data = scaler.transform(input_data)

prediction = model.predict(scaled_data)[0]

result = "Diabetic 😔" if prediction == 1 else "Non-Diabetic 😀"

print("\n===== TEST RESULT =====")
print("Input:", input_data)
print("Prediction:", result)
