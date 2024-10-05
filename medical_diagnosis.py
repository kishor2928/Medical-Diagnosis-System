# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 21:56:23 2024

@author: Mrunali
"""

import pickle
import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns

st.set_page_config(layout="wide")

# Load models
diabetes = pickle.load(open('diabetes_model.pkl', 'rb'))
cancer = pickle.load(open('cm.pkl', 'rb'))
heart = pickle.load(open('heart_disease_model.pkl', 'rb'))

# Define tabs
tabs = st.tabs(["Home", "Diabetes Prediction", "Cancer Prediction", "Heart Disease Prediction"])

with tabs[0]:
    st.title("Welcome to the Multiple Disease Prediction System")
    icons=['activity', 'heart', 'person']
    st.write("Welcome to the Medical Diagnosis System, a tool designed to predict various medical conditions using Machine Learning models. This system includes predictions for Diabetes, Cancer, and Heart Disease.")
    st.write("Below is a guide on how to use prediction system effectively:")
    

    st.write("""
### How to Use:

**1. Navigation:** 

On the main page, you will find three tabs horizontally aligned at the top: Diabetes Prediction, Cancer Prediction, and Heart Disease Prediction.
Click on each tab to navigate to the respective prediction page.

**2. Input Parameters:**

Each prediction page requires specific input parameters related to the respective health condition:
- **Diabetes Prediction:** Parameters include number of pregnancies, glucose level, blood pressure, etc.
- **Cancer Prediction:** Parameters include age, gender, lifestyle factors, symptoms, etc.
- **Heart Disease Prediction:** Parameters include age, sex, chest pain type, cardiovascular health indicators, etc.

**3. Prediction:**

Click on the respective "Test Result" button to see the prediction for that health condition.

**4. Result Interpretation:**

The system will display whether the person is predicted to have the health condition or not based on the input data.
Results are provided as straightforward diagnostic statements.

**5. Navigation Tips:**

Use the horizontal tabs at the top of the page to switch between prediction models.
Each tab opens a dedicated page with input fields and predictive results specific to that health condition.

**Disclaimer:**

- This system is for educational purposes and should not substitute professional medical advice.
- Always consult with a healthcare provider for any medical concerns or diagnoses.
""")


# Diabetes Prediction Page
with tabs[1]:
    st.markdown("<h1 style='text-align: center; color: white;'>Diabetes Prediction</h1>", unsafe_allow_html=True)
    
    # Input section
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Glucose = st.text_input('Glucose Level')
        Insulin = st.text_input('Insulin Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        BMI = st.text_input('BMI value')

    with col4:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        Age = st.text_input('Age of the Person')

    # Prediction button
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        st.success(diab_diagnosis)
    
    # Chart section
    
    st.markdown("<h1 style='text-align: center; color: white;'>Prediction Result</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])

    with col1:
        # Sample pie chart
        labels = ['Diabetic', 'Non Diabetic']
        values = [30, 70]  # Sample data
        fig = px.pie(values=values, names=labels, title='Diabetic vs Non-Diabetic')
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig)

    with col2:
        # Sample bar chart
        df = pd.DataFrame({
            'Outcome': labels,
            'Age': values
        })
        bar_fig = px.bar(df, x='Outcome', y='Age', title='Outcome vs. Age')
        st.plotly_chart(bar_fig)
        
    st.header("Additional Information")

    st.write("""
        Cancer is a disease where some of the body's cells grow uncontrollably and spread to other parts of the body. There are many types of cancer, each with different risk factors and preventive measures.
        """)

    st.header("Causes")
    st.write("""
            - **Genetics:** Family history of cancer.
            - **Lifestyle Factors:** Smoking, alcohol consumption, poor diet, and lack of physical activity.
            - **Environmental Factors:** Exposure to harmful chemicals and radiation.
            - **Infections:** Certain viruses and bacteria can increase cancer risk.
            - **Chronic Inflammation:** Long-term inflammation can lead to DNA damage.
            """)

            # Prevention of Cancer
    st.header("Prevention")
    st.write("""
            - **Healthy Diet:** Plenty of fruits, vegetables, and whole grains; limit processed foods and red meats.
            - **Avoid Tobacco:** No smoking or chewing tobacco.
            - **Limit Alcohol:** Drink in moderation.
            - **Regular Exercise:** Helps maintain a healthy weight and reduce risk.
            - **Protect Skin:** Use sunscreen and avoid excessive sun exposure.
            """)
   
    

# Cancer Prediction Page
with tabs[2]:
    st.markdown("<h1 style='text-align: center; color: white;'>Cancer Prediction</h1>", unsafe_allow_html=True)
    
    # Input section
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Age = st.text_input('Age of the person')
        DustAllergy = st.text_input('DustAllergy')
        BalancedDiet = st.text_input('BalancedDiet')
        ChestPain = st.text_input('ChestPain')
        WeightLoss = st.text_input('WeightLoss')

    with col2:
        Gender = st.text_input('Gender')
        OccuPationalHazards = st.text_input('OccuPationalHazards')
        Obesity = st.text_input('Obesity')
        CoughingofBlood = st.text_input('CoughingofBlood')
        ShortnessofBreath = st.text_input('ShortnessofBreath')

    with col3:
        AirPollution = st.text_input('Air Pollution')
        GeneticRisk = st.text_input('GeneticRisk')
        Smoking = st.text_input('Smoking')
        Fatigue = st.text_input('Fatigue')
        Wheezing = st.text_input('Wheezing')

    with col4:
        Alcoholuse = st.text_input('Alcoholuse')
        chronicLungDisease = st.text_input('chronicLungDisease')
        PassiveSmoker = st.text_input('PassiveSmoke')
        Snoring = st.text_input('Snoring')
        

    with col5:
        ClubbingofFingerNails = st.text_input('ClubbingofFingerNails')
        FrequentCold = st.text_input('FrequentCold')
        DryCough = st.text_input('DryCough')
        SwallowingDifficulty = st.text_input('SwallowingDifficulty')
    
    # Prediction button
    if st.button("Cancer's Test Result"):
        user_input = [Age, Gender, AirPollution, Alcoholuse, DustAllergy, OccuPationalHazards, GeneticRisk,
                      chronicLungDisease, BalancedDiet, Obesity, Smoking, PassiveSmoker, ChestPain, CoughingofBlood, Fatigue,
                      WeightLoss, ShortnessofBreath, Wheezing, SwallowingDifficulty, ClubbingofFingerNails, FrequentCold, DryCough, Snoring]
        user_input = [float(x) for x in user_input]
        cancer_prediction = cancer.predict([user_input])

        if cancer_prediction[0] == 1:
            cancer_diagnosis = "The person has cancer"
        else:
            cancer_diagnosis = "The person does not have cancer"
        st.success(cancer_diagnosis)
    
    # Chart section
    st.markdown("<h1 style='text-align: center; color: white;'>Prediction Result</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])

    with col1:
        # Sample pie chart
        labels = ['Positive', 'Negative']
        values = [20, 80]  # Sample data
        fig = px.pie(values=values, names=labels, title='Cancer Prediction Result')
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig)

    with col2:
        df = pd.DataFrame({
            'Level': labels,
            'Age': values
        })
        bar_fig = px.bar(df, x='Level', y='Age', title='Level vs. Age')
        st.plotly_chart(bar_fig)
        
    st.header("Additional Information")
    st.write("""
    Cancer is a disease where some of the body's cells grow uncontrollably and spread to other parts of the body. There are many types of cancer, each with different risk factors and preventive measures.
    """)

    # Causes of Cancer
    st.header("Causes")
    st.write("""
    - **Genetics:** Family history of cancer.
    - **Lifestyle Factors:** Smoking, alcohol consumption, poor diet, and lack of physical activity.
    - **Environmental Factors:** Exposure to harmful chemicals and radiation.
    - **Infections:** Certain viruses and bacteria can increase cancer risk.
    - **Chronic Inflammation:** Long-term inflammation can lead to DNA damage.
    """)

    # Prevention of Cancer
    st.header("Prevention")
    st.write("""
    - **Healthy Diet:** Plenty of fruits, vegetables, and whole grains; limit processed foods and red meats.
    - **Avoid Tobacco:** No smoking or chewing tobacco.
    - **Limit Alcohol:** Drink in moderation.
    - **Regular Exercise:** Helps maintain a healthy weight and reduce risk.
    - **Protect Skin:** Use sunscreen and avoid excessive sun exposure.
    """)


# Heart Disease Prediction Page
with tabs[3]:
    st.markdown("<h1 style='text-align: center; color: white;'>Heart Disease Prediction</h1>", unsafe_allow_html=True)
    
    # Input section
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        restecg = st.text_input('Resting Electrocardiographic results')
        exang = st.text_input('Exercise Induced Angina')
        ca = st.text_input('Major vessels colored by flourosopy')

    with col2:
        sex = st.text_input('Sex')
        chol = st.text_input('Serum Cholestoral in mg/dl')
        thalach = st.text_input('Maximum Heart Rate achieved')
        oldpeak = st.text_input('ST depression induced by exercise')
        

    with col3:
        cp = st.text_input('Chest Pain types')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        slope = st.text_input('Slope of the peak exercise ST segment')
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    # Prediction button
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        st.success(heart_diagnosis)
    
    # Chart section
    st.markdown("<h1 style='text-align: center; color: white;'>Prediction Result</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])

    with col1:
        # Sample pie chart
        labels = ['Positive', 'Negative']
        values = [25, 75]  # Sample data
        fig = px.pie(values=values, names=labels, title='Heart Disease Prediction Result')
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig)

    with col2:
        # Sample bar chart
        df = pd.DataFrame({
            'target': labels,
            'age': values
        })
        bar_fig = px.bar(df, x='target', y='age', title= 'Age Vs Target')
        st.plotly_chart(bar_fig)
        
    st.header("Additioanl Information")
    st.write("""
    Heart disease refers to various types of heart conditions, including coronary artery disease, heart attacks, and more. It is a leading cause of death globally.
    """)

    # Causes of Heart Disease
    st.header("Causes")
    st.write("""
    - **Unhealthy Diet:** High in saturated fats, trans fats, cholesterol, and sodium.
    - **Lack of Exercise:** Sedentary lifestyle can increase risk.
    - **Smoking:** Damages the heart and blood vessels.
    - **High Blood Pressure:** Can cause damage to arteries.
    - **High Cholesterol:** Can lead to plaque build-up in arteries.
    - **Diabetes:** High blood sugar can damage blood vessels and nerves.
    """)

    # Prevention of Heart Disease
    st.header("Prevention")
    st.write("""
    - **Heart-Healthy Diet:** Rich in fruits, vegetables, whole grains, and lean proteins.
    - **Regular Physical Activity:** At least 150 minutes of moderate exercise per week.
    - **Maintain Healthy Weight:** Helps reduce risk factors.
    - **Avoid Smoking:** Quitting smoking significantly reduces risk.
    - **Regular Check-ups:** Monitor blood pressure, cholesterol levels, and blood sugar.
    """)
