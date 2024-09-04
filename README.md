# Multiple Disease Prediction Web Application 🩺

A user-friendly web application built with Streamlit for predicting multiple diseases including Diabetes, Heart Disease, and Kidney Disease using machine learning models.

## Features

- **Diabetes Prediction:** Predicts the likelihood of diabetes based on input parameters such as glucose levels, insulin, BMI, and more.
- **Heart Disease Prediction:** Assesses the risk of heart disease using data such as age, cholesterol levels, chest pain types, etc.
- **Kidney Disease Prediction:** Identifies the presence of kidney disease based on various health indicators like blood pressure, serum creatinine, and others.

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Models:** Machine Learning models for disease prediction
- **Deployment:** Streamlit sharing or any other cloud platform

## How It Works

The application is divided into three sections, each corresponding to a disease:

1. **Diabetes Prediction**
   - Input: User details such as pregnancies, glucose level, BMI, age, etc.
   - Model: K-Nearest Neighbors (KNN) trained on diabetes data.
   - Output: Predicts whether the person has diabetes or not.

2. **Heart Disease Prediction**
   - Input: Parameters like age, sex, chest pain type, blood pressure, cholesterol level, etc.
   - Model: Logistic Regression (LG) model trained on heart disease data.
   - Output: Provides the likelihood of heart disease.

3. **Kidney Disease Prediction**
   - Input: Data including blood pressure, specific gravity, red blood cell count, etc.
   - Model: Gradient Boosting (GB) model for kidney disease detection.
   - Output: Predicts if kidney disease is present.

## Models

1. **Diabetes Model:** K-Nearest Neighbors (KNN) for predicting diabetes.
2. **Heart Disease Model:** Logistic Regression (LG) model for heart disease detection.
3. **Kidney Disease Model:** Gradient Boosting (GB) model for identifying kidney disease.

## How to Use

1. **Select a Disease Prediction:** Use the sidebar to choose between Diabetes, Heart Disease, or Kidney Disease prediction.
2. **Enter Details:** Fill in the necessary input fields shown on the screen.
3. **Get Results:** Click the "Test Result" button to see the prediction.

## Future Improvements

- Integration of more diseases for prediction.
- Enhancement of the UI for a better user experience.
- Addition of more advanced machine learning models.

## Screenshots

| ![Diabetes Prediction](screenshots/diabetes.png) | ![Heart Disease Prediction](screenshots/heart.png) | ![Kidney Disease Prediction](screenshots/kidney.png) |

## Conclusion

The "Multiple Disease Prediction Web Application" is an innovative tool designed to assist individuals and healthcare professionals in assessing the risk of prevalent diseases such as Diabetes, Heart Disease, and Kidney Disease. By leveraging machine learning models, this application provides accurate and fast predictions based on user inputs, enhancing early detection and proactive health management.

This project not only demonstrates the power of machine learning in healthcare but also serves as a foundation for expanding into a more comprehensive predictive health tool in the future. Further development could include incorporating additional diseases, refining models, and integrating with healthcare systems for broader impact. 
