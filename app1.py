import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Multiple Disease Prediction", layout="wide", page_icon="🩺")

# Load models
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f'{working_dir}/models/diabetes_models/knn_diabetes.pkl', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/models/heart_models/lg_model.pkl', 'rb'))
kidney_disease_model = pickle.load(open(f'{working_dir}/models/kidney_models/gb_kindey.pkl', 'rb'))

# Custom CSS for styling
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {background-color: #f0f2f6;}
    .main {background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);}
    .css-18e3th9 {padding-top: 0px;} /* Remove the top padding */
    .stButton>button {border-radius: 10px; background-color: #4CAF50; color: white; padding: 10px 24px;}
    </style>
    """, unsafe_allow_html=True
)

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction",
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Kidney Disease Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction Section
if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction Using Machine Learning")
    st.write("### Please fill out the details below to check for diabetes.")
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
    with col2:
        Glucose = st.number_input("Glucose Level", min_value=0.0, format="%.2f")
    with col3:
        BloodPressure = st.number_input("Blood Pressure Value", min_value=0.0, format="%.2f")
    with col1:
        SkinThickness = st.number_input("Skin Thickness Value", min_value=0.0, format="%.2f")
    with col2:
        Insulin = st.number_input("Insulin Value", min_value=0.0, format="%.2f")
    with col3:
        BMI = st.number_input("BMI Value", min_value=0.0, format="%.2f")
    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function Value", min_value=0.0, format="%.2f")
    with col2:
        Age = st.number_input("Age", min_value=0, step=1)
    
    if st.button("Diabetes Test Result"):
        # BMI Categories
        NewBMI_Underweight = 1 if BMI <= 18.5 else 0
        NewBMI_Overweight = 1 if 24.9 < BMI <= 29.9 else 0
        NewBMI_Obesity_1 = 1 if 29.9 < BMI <= 34.9 else 0
        NewBMI_Obesity_2 = 1 if 34.9 < BMI <= 39.9 else 0
        NewBMI_Obesity_3 = 1 if BMI > 39.9 else 0
        
        # Insulin Score
        NewInsulinScore_Normal = 1 if 16 <= Insulin <= 166 else 0
        
        # Glucose Levels
        NewGlucose_Low = 1 if Glucose <= 70 else 0
        NewGlucose_Normal = 1 if 70 < Glucose <= 99 else 0
        NewGlucose_Overweight = 1 if 99 < Glucose <= 126 else 0
        NewGlucose_Secret = 1 if Glucose > 126 else 0

        user_input = [
            Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI,
            DiabetesPedigreeFunction, Age, NewBMI_Underweight, NewBMI_Overweight,
            NewBMI_Obesity_1, NewBMI_Obesity_2, NewBMI_Obesity_3, NewInsulinScore_Normal,
            NewGlucose_Low, NewGlucose_Normal, NewGlucose_Overweight, NewGlucose_Secret
        ]

        # Predict
        prediction = diabetes_model.predict([user_input])
        diabetes_result = "The person has diabetes." if prediction[0] == 1 else "The person does not have diabetes."
        st.success(diabetes_result)

# Heart Disease Prediction Section
if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction Using Machine Learning")
    st.write("### Fill in the details to determine the risk of heart disease.")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=0, step=1)
    with col2:
        sex = st.selectbox("Sex", options=["Male", "Female"])
    with col3:
        cp = st.number_input("Chest Pain Types", min_value=0, step=1)
    with col1:
        trestbps = st.number_input("Resting Blood Pressure", min_value=0.0, format="%.2f")
    with col2:
        chol = st.number_input("Serum Cholesterol in mg/dl", min_value=0.0, format="%.2f")
    with col3:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1])
    with col1:
        restecg = st.number_input("Resting Electrocardiographic results", min_value=0, step=1)
    with col2:
        thalach = st.number_input("Maximum Heart Rate achieved", min_value=0.0, format="%.2f")
    with col3:
        exang = st.selectbox("Exercise Induced Angina", options=[0, 1])
    with col1:
        oldpeak = st.number_input("ST depression induced by exercise", min_value=0.0, format="%.2f")
    with col2:
        slope = st.number_input("Slope of the peak exercise ST segment", min_value=0, step=1)
    with col3:
        ca = st.number_input("Major vessels colored by fluoroscopy", min_value=0, step=1)
    with col1:
        thal = st.number_input("Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect", min_value=0, max_value=2, step=1)
    
    if st.button("Heart Disease Test Result"):
        user_input = [age, sex == "Male", cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        prediction = heart_disease_model.predict([user_input])
        heart_disease_result = "This person has heart disease." if prediction[0] == 1 else "This person does not have heart disease."
        st.success(heart_disease_result)

# Kidney Disease Prediction Section
if selected == 'Kidney Disease Prediction':
    st.title("Kidney Disease Prediction Using Machine Learning")
    st.write("### Enter the following information to check for kidney disease.")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        age = st.number_input('Age', min_value=0, step=1)
    with col2:
        blood_pressure = st.number_input('Blood Pressure', min_value=0.0, format="%.2f")
    with col3:
        specific_gravity = st.number_input('Specific Gravity', min_value=0.0, format="%.2f")
    with col4:
        albumin = st.number_input('Albumin', min_value=0, step=1)
    with col5:
        sugar = st.number_input('Sugar', min_value=0, step=1)
    with col1:
        red_blood_cells = st.selectbox('Red Blood Cells', options=['Normal', 'Abnormal'])
    with col2:
        pus_cell = st.selectbox('Pus Cell', options=['Normal', 'Abnormal'])
    with col3:
        pus_cell_clumps = st.selectbox('Pus Cell Clumps', options=['Present', 'Not Present'])
    with col4:
        bacteria = st.selectbox('Bacteria', options=['Present', 'Not Present'])
    with col5:
        blood_glucose_random = st.number_input('Blood Glucose Random', min_value=0.0, format="%.2f")
    with col1:
        blood_urea = st.number_input('Blood Urea', min_value=0.0, format="%.2f")
    with col2:
        serum_creatinine = st.number_input('Serum Creatinine', min_value=0.0, format="%.2f")
    with col3:
        sodium = st.number_input('Sodium', min_value=0.0, format="%.2f")
    with col4:
        potassium = st.number_input('Potassium', min_value=0.0, format="%.2f")
    with col5:
        haemoglobin = st.number_input('Haemoglobin', min_value=0.0, format="%.2f")
    with col1:
        packed_cell_volume = st.number_input('Packed Cell Volume', min_value=0, step=1)
    with col2:
        white_blood_cell_count = st.number_input('White Blood Cell Count', min_value=0, step=1)
    with col3:
        red_blood_cell_count = st.number_input('Red Blood Cell Count', min_value=0.0, format="%.2f")
    with col4:
        hypertension = st.selectbox('Hypertension', options=[0, 1])
    with col5:
        diabetes_mellitus = st.selectbox('Diabetes Mellitus', options=[0, 1])
    with col1:
        coronary_artery_disease = st.selectbox('Coronary Artery Disease', options=[0, 1])
    with col2:
        appetite = st.selectbox('Appetite', options=['Good', 'Poor'])
    with col3:
        peda_edema = st.selectbox('Pedal Edema', options=[0, 1])
    with col4:
        aanemia = st.selectbox('Anemia', options=[0, 1])
    
    if st.button("Kidney's Test Result"):
        user_input = [
            age, blood_pressure, specific_gravity, albumin, sugar, 
            1 if red_blood_cells == 'Normal' else 0, 
            1 if pus_cell == 'Normal' else 0, 
            1 if pus_cell_clumps == 'Present' else 0, 
            1 if bacteria == 'Present' else 0,
            blood_glucose_random, blood_urea, serum_creatinine, sodium,
            potassium, haemoglobin, packed_cell_volume, white_blood_cell_count,
            red_blood_cell_count, hypertension, diabetes_mellitus,
            coronary_artery_disease, 1 if appetite == 'Good' else 0,
            peda_edema, aanemia
        ]
        prediction = kidney_disease_model.predict([user_input])
        kidney_diagnosis = "The person has kidney disease." if prediction[0] == 1 else "The person does not have kidney disease."
        st.success(kidney_diagnosis)
