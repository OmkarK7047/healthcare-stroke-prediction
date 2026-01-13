🏥 Healthcare Stroke Risk Prediction System
________________________________________________________________________________________________________________________

An end-to-end Machine Learning + Flask application that predicts the risk of stroke using patient health data and displays the result through a clean web interface with percentage-based risk prediction.
________________________________________________________________________________________________________________________

📌 Problem Statement
Stroke is a life-threatening medical condition that can lead to permanent disability or death.  
Early identification of individuals at high risk can help in preventive care and timely medical intervention.

This project aims to build a machine learning-based stroke prediction system and deploy it as a web application.
________________________________________________________________________________________________________________________

📊 Dataset Information
- Healthcare Stroke Dataset
- Total records: 5110
- Target variable: `stroke`
  - `0` → No Stroke
  - `1` → Stroke
- Dataset is highly imbalanced, which is common in real-world healthcare data.
________________________________________________________________________________________________________________________

 Features Used
- Age  
- Gender  
- Hypertension  
- Heart Disease  
- Ever Married  
- Work Type  
- Residence Type  
- Average Glucose Level  
- BMI  
- Smoking Status  
________________________________________________________________________________________________________________________

🧠 Machine Learning Details

Problem Type
- Supervised Learning  
- Binary Classification  

Models Implemented
- Logistic Regression  
- Decision Tree Classifier  
- Random Forest Classifier ✅  

Model Selection
Random Forest was selected as the final model due to:
- Better performance on tabular healthcare data
- Higher Recall and F1-score
- Robust handling of feature interactions
________________________________________________________________________________________________________________________

📈 Model Evaluation

Due to class imbalance, accuracy alone is not sufficient.

Evaluation Metrics
- Accuracy  
- Precision  
- Recall (prioritized)  
- F1-score  
- Confusion Matrix  

> Recall is prioritized to minimize false negatives, which is critical in healthcare applications.
________________________________________________________________________________________________________________________

🌐 Web Application (Flask)

The trained machine learning model is deployed using Flask

Application Features
- User-friendly web interface
- Accepts patient health inputs
- Applies the same preprocessing used during training
- Displays stroke risk as a percentage
- Color-coded prediction output:
  - 🔴 High Risk
  - 🟢 Low Risk
________________________________________________________________________________________________________________________

🛠️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Flask  
- HTML  
- CSS  


