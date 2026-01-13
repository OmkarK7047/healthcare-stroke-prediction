from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    hypertension = int(request.form['Hypertension'])
    heart_disease = int(request.form['heart_disease'])
    avg_glucose_level = float(request.form['avg_glucose_level'])
    bmi = float(request.form['bmi'])
    gender = int(request.form['gender'])
    ever_married = int(request.form['ever_married'])
    work_type = int(request.form['work_type'])
    Residence_type = int(request.form['Residence_type'])
    smoking_status = int(request.form['smoking_status'])

    
    # input_data = np.array([[age, hypertension, heart_disease, avg_glucose_level, bmi]])
    input_data = np.array([[ 
    gender,
    age,
    hypertension,
    heart_disease,
    ever_married,
    work_type,
    Residence_type,
    avg_glucose_level,
    bmi,
    smoking_status
    ]])
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)

    probability = model.predict_proba(scaled_data)[0][1] * 100
    probability = round(probability, 2)

    if prediction==1 :
        result = f"High risk of stroke with a probability of {probability}%."
    else:
        result = f"Low risk of stroke with a probability of {probability}%."

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    print("Starting Python Flask Server For Stroke Prediction...")
    app.run(debug=True)
