# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:10:26 2023

@author: user
"""

# import pickle
# import streamlit as st
# from streamlit_option_menu import option_menu


# # loading a save models

# diabetes_model = pickle.load(open("C:/Users/user/Downloads/Diabetes Prediction/trained_model.sav", 'rb'))
# breast_model = pickle.load(open("C:/Users/user/Desktop/Multiple disease prediction/breast_model.sav", 'rb'))
# heart_model = pickle.load(open("C:/Users/user/Desktop/Multiple disease prediction/heart_model.sav", 'rb'))


# # creating a navbar for navigation

# with st.sidebar:
    
#     selected = option_menu("Multiple Disease Prediction System", 
                           
#                            ['Diabetes Prediction',
#                             'Heart Disease Prediction',
#                             'Breast Cancer Prediction'],
                           
#                            icons= ['activity', 'heart-pulse', 'person'],
                           
#                            default_index = 0)  # this means we have three button and making index 0 indicate when we open the web it should open index 0 button as default.



 
    
# # Diabetes Prediction Page

# if (selected == 'Diabetes Prediction'):
    
#     # title of page
#     st.title("Diabetes Prediction System")
    
    
#     # getting the input data from the user
#     # columns for input fields 
    
#     col1,col2,col3 = st.columns(3)
    
#     with col1:
#         Pregnancies = st.text_input('Number of Pregnancies')
        
#     with col2:
#         Glucose = st.text_input('Level of Glucose')
        
#     with col3:
#         BloodPressure = st.text_input('Level of BloodPressure')
        
#     with col1:
#         SkinThickness = st.text_input('Level of SkinThickness')
        
#     with col2:
#         Insulin = st.text_input('Level of Insulin')
        
#     with col3:
#         BMI = st.text_input('Level of BMI')
        
#     with col1:
#         DiabetesPedigreeFunction = st.text_input('Level of DiabetesPedigreeFunction')
        
#     with col2:
#         Age = st.text_input("Age of a person")
    
    
#     # code for a prediction
    
#     diab_diagnosis = ''
    
#     # creating a button for prediction
    
#     if st.button('Diabetes Test'):
#         diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]) # we have used double list to indicate that we are predicting for one data point.
        
#         if (diab_prediction[0]==1):
#             diab_diagnosis = "The Person has Diabetes."
            
#         else:
#             diab_diagnosis = "The Person has not Diabetes."
            
#     st.success(diab_diagnosis)
        
        
    
    
    
    
# # Heart Disease Prediction    
# if (selected == 'Heart Disease Prediction'):
    
#     # title of page
#     st.title("Heart Disease Prediction System")
    
#     # getting the input data from the user
#     # columns for input fields
    
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         age = st.text_input("Enter a age of a person")
        
#     with col2:
#         sex = st.text_input("Enter a sex")
        
#     with col3:
#         cp = st.text_input("Enter a cp")
        
#     with col1:
#         trestbps = st.text_input("Enter a trestbps")
        
#     with col2:
#         chol = st.text_input("Enter a chol")
        
#     with col3:
#         fbs = st.text_input("Enter a fbs")
        
#     with col1:
#         restecg = st.text_input("Enter a restecg")
        
#     with col2:
#         thalach = st.text_input("Enter a thalach")
        
#     with col3:
#         exang = st.text_input("Enter a exang")
        
#     with col1:
#         oldpeak = st.text_input("Enter a oldpeak")
        
#     with col2:
#         slope = st.text_input("Enter a slope")
        
#     with col3:
#         ca = st.text_input("Enter a ca")
        
#     with col1:
#         thal = st.text_input("Enter a thal")
        
        
    
#     # code for prediciton 
    
#     heart_diagnosis = ''
    
    
#     #creating a button for prediction
    
#     if st.button('Heart Disease Test'):
#         heart_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        
#         if (heart_prediction[0]==0):
#             heart_diagnosis = "The Person has a healty heart"
            
#         else:
#             heart_diagnosis = "The Person has a defective heart."
            
            
#     st.success(heart_diagnosis)


    

    
    
# # Breast Cancer Prediction    
# if (selected == 'Breast Cancer Prediction'):
    
#     # title of page
#     st.title("Breast Cancer Prediction System")
    
    
#     # getting the input data from the user
#     # columns for input fields
    
#     col1,col2,col3,col4,col5 = st.columns(5)
    
#     with col1:
#         mean_radius = st.text_input("Enter a mean radius")
#     with col2:
#         mean_texture = st.text_input("Enter a mean texture")
#     with col3:
#         mean_perimeter = st.text_input("Enter a mean perimeter")
#     with col4:
#         mean_area = st.text_input("Enter a mean area")
#     with col5:
#         mean_smoothness = st.text_input("Enter a mean smoothness")
#     with col1:
#         mean_compactness = st.text_input("Enter a mean compactness")
#     with col2:
#         mean_concavity = st.text_input("Enter a mean concavity")
#     with col3:
#         mean_concave_points = st.text_input("Enter a mean concave points")
#     with col4:
#         mean_symmetry = st.text_input("Enter a mean symmetry")
#     with col5:
#         mean_fractal_dimension = st.text_input("Enter a mean fractal dimension")
#     with col1:
#         radius_error = st.text_input("Enter a radius error")
#     with col2:
#         texture_error = st.text_input("Enter a texture error")
#     with col3:
#         perimeter_error = st.text_input("Enter a perimeter error")
#     with col4:
#         area_error = st.text_input("Enter an area error")
#     with col5:
#         smoothness_error = st.text_input("Enter a smoothness error")
#     with col1:
#         compactness_error = st.text_input("Enter a compactness error")
#     with col2:
#         concavity_error = st.text_input("Enter a concavity error")
#     with col3:
#         points_error = st.text_input("Enter a concave points error")
#     with col4:
#         symmetry_error = st.text_input("Enter a symmetry error")
#     with col5:
#         fractal_dimension_error = st.text_input("Enter a fractal dimension error")
#     with col1:
#         worst_radius = st.text_input("Enter a worst radius")
#     with col2:
#         worst_texture = st.text_input("Enter a worst texture")
#     with col3:
#         worst_perimeter = st.text_input("Enter a worst perimeter")
#     with col4:
#         worst_area = st.text_input("Enter a worst area")
#     with col5:
#         worst_smoothness = st.text_input("Enter a worst smoothness")
#     with col1:
#         worst_compactness = st.text_input("Enter a worst compactness")
#     with col2:
#         worst_concavity = st.text_input("Enter a worst concavity")
#     with col3:
#         worst_concave_points = st.text_input("Enter a worst concave points")
#     with col4:
#         worst_symmetry = st.text_input("Enter a worst symmetry")
#     with col5:
#         worst_fractal_dimension = st.text_input("Enter a worst fractal dimension")
        

    
#     # code for prediction
    
#     breast_diagnosis = ''
    
    
#     # creating a button for prediction 
    
#     if st.button('Breast Cancer Test'):
#         breast_prediction = breast_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,points_error,symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]])
        
#         if (breast_prediction[0]==0):
#             breast_diagnosis = 'The Breast cancer is Malignant'
            
#         else:
#             breast_diagnosis = 'The Breast Cancer is Benign'
            
#     st.success(breast_diagnosis) 


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Loading the saved models
diabetes_model = pickle.load(open("C:/Users/user/Desktop/Multiple disease prediction/trained_model.sav", 'rb'))
breast_model = pickle.load(open("C:/Users/user/Desktop/Multiple disease prediction/breast_model.sav", 'rb'))
heart_model = pickle.load(open("C:/Users/user/Desktop/Multiple disease prediction/heart_model.sav", 'rb'))


# Creating a navbar for navigation
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System",
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Breast Cancer Prediction'],
                           icons=['activity', 'heart-pulse', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # Title of page
    st.title("Diabetes Prediction System")
    
    # Input fields
    st.header("Enter Patient Details")
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
    with col2:
        glucose = st.number_input("Glucose Level", min_value=0.0, step=1.0)
    with col3:
        blood_pressure = st.number_input("Blood Pressure Level", min_value=0.0, step=1.0)
    with col1:
        skin_thickness = st.number_input("Skin Thickness Level", min_value=0.0, step=1.0)
    with col2:
        insulin = st.number_input("Insulin Level", min_value=0.0, step=1.0)
    with col3:
        bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, step=1.0)
    with col1:
        diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, step=0.01)
    with col2:
        age = st.number_input("Age", min_value=0, step=1)
   
    
   
    

    
    # Prediction
    if st.button("Predict Diabetes"):
       if any(
           [
               pregnancies == 0,
               glucose == 0.0,
               blood_pressure == 0.0,
               skin_thickness == 0.0,
               insulin == 0.0,
               bmi == 0.0,
               diabetes_pedigree == 0.0,
               age == 0,
           ]
       ):
           st.error("Invalid input. Please make sure all fields are filled correctly.")
       else:
           prediction = diabetes_model.predict(
               [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]]
           )
           result = "The person does not have diabetes."
           if prediction[0] == 1:
               result = "The person has diabetes."
           st.success(result)


# Heart Disease Prediction
elif selected == 'Heart Disease Prediction':
    # Title of page
    st.title("Heart Disease Prediction System")
    
    # Input fields
    st.header("Enter Patient Details")
    age = st.number_input("Age", min_value=0, step=1)
    sex = st.selectbox("Sex", ['Male', 'Female'])
    chest_pain_type = st.selectbox("Chest Pain Type", ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
    resting_blood_pressure = st.number_input("Resting Blood Pressure", min_value=0.0, step=1.0)
    serum_cholesterol = st.number_input("Serum Cholesterol", min_value=0.0, step=1.0)
    fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ['False', 'True'])
    resting_ecg_results = st.selectbox("Resting ECG Results", ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
    max_heart_rate = st.number_input("Maximum Heart Rate", min_value=0, step=1)
    exercise_induced_angina = st.selectbox("Exercise Induced Angina", ['No', 'Yes'])
    st_depression = st.number_input("ST Depression induced by exercise relative to rest", min_value=0.0, step=0.1)
    st_slope = st.selectbox("The slope of the peak exercise ST segment", ['Upsloping', 'Flat', 'Downsloping'])
    num_major_vessels = st.number_input("Number of major vessels (0-3) colored by fluoroscopy", min_value=0, max_value=3, step=1)
    thalassemia = st.selectbox("Thalassemia", ['Normal', 'Fixed Defect', 'Reversible Defect'])
    
    # Prediction
    if st.button("Predict Heart Disease"):
        prediction = heart_model.predict([[age, sex, chest_pain_type, resting_blood_pressure, serum_cholesterol, fasting_blood_sugar,
                                           resting_ecg_results, max_heart_rate, exercise_induced_angina, st_depression, st_slope,
                                           num_major_vessels, thalassemia]])
        result = "The person has a healthy heart."
        if prediction[0] == 1:
            result = "The person has a defective heart."
        st.success(result)


# Breast Cancer Prediction
elif selected == 'Breast Cancer Prediction':
    # Title of page
    st.title("Breast Cancer Prediction System")
    
    # Input fields
    st.header("Enter Patient Details")
    mean_radius = st.number_input("Mean Radius", min_value=0.0, step=0.1)
    mean_texture = st.number_input("Mean Texture", min_value=0.0, step=0.1)
    mean_perimeter = st.number_input("Mean Perimeter", min_value=0.0, step=0.1)
    mean_area = st.number_input("Mean Area", min_value=0.0, step=0.1)
    mean_smoothness = st.number_input("Mean Smoothness", min_value=0.0, step=0.1)
    mean_compactness = st.number_input("Mean Compactness", min_value=0.0, step=0.1)
    mean_concavity = st.number_input("Mean Concavity", min_value=0.0, step=0.1)
    mean_concave_points = st.number_input("Mean Concave Points", min_value=0.0, step=0.1)
    mean_symmetry = st.number_input("Mean Symmetry", min_value=0.0, step=0.1)
    mean_fractal_dimension = st.number_input("Mean Fractal Dimension", min_value=0.0, step=0.1)
    radius_error = st.number_input("Radius Error", min_value=0.0, step=0.1)
    texture_error = st.number_input("Texture Error", min_value=0.0, step=0.1)
    perimeter_error = st.number_input("Perimeter Error", min_value=0.0, step=0.1)
    area_error = st.number_input("Area Error", min_value=0.0, step=0.1)
    smoothness_error = st.number_input("Smoothness Error", min_value=0.0, step=0.1)
    compactness_error = st.number_input("Compactness Error", min_value=0.0, step=0.1)
    concavity_error = st.number_input("Concavity Error", min_value=0.0, step=0.1)
    concave_points_error = st.number_input("Concave Points Error", min_value=0.0, step=0.1)
    symmetry_error = st.number_input("Symmetry Error", min_value=0.0, step=0.1)
    fractal_dimension_error = st.number_input("Fractal Dimension Error", min_value=0.0, step=0.1)
    worst_radius = st.number_input("Worst Radius", min_value=0.0, step=0.1)
    worst_texture = st.number_input("Worst Texture", min_value=0.0, step=0.1)
    worst_perimeter = st.number_input("Worst Perimeter", min_value=0.0, step=0.1)
    worst_area = st.number_input("Worst Area", min_value=0.0, step=0.1)
    worst_smoothness = st.number_input("Worst Smoothness", min_value=0.0, step=0.1)
    worst_compactness = st.number_input("Worst Compactness", min_value=0.0, step=0.1)
    worst_concavity = st.number_input("Worst Concavity", min_value=0.0, step=0.1)
    worst_concave_points = st.number_input("Worst Concave Points", min_value=0.0, step=0.1)
    worst_symmetry = st.number_input("Worst Symmetry", min_value=0.0, step=0.1)
    worst_fractal_dimension = st.number_input("Worst Fractal Dimension", min_value=0.0, step=0.1)
    
    # Prediction
    if st.button("Predict Breast Cancer"):
        prediction = breast_model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness,
                                            mean_compactness, mean_concavity, mean_concave_points, mean_symmetry,
                                            mean_fractal_dimension, radius_error, texture_error, perimeter_error,
                                            area_error, smoothness_error, compactness_error, concavity_error,
                                            concave_points_error, symmetry_error, fractal_dimension_error,
                                            worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness,
                                            worst_compactness, worst_concavity, worst_concave_points, worst_symmetry,
                                            worst_fractal_dimension]])
        result = "The breast tumor is benign (non-cancerous)."
        if prediction[0] == 1:
            result = "The breast tumor is malignant (cancerous)."
        st.success(result)


    
    
    
    
    
    
    