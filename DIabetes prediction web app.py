# Importing the libraries
import numpy as np 
import pickle 
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open("C:/Users/Tariq/Downloads/Temp Projects/17-Diabetes Prediction V2/trained_model.sav",'rb'))


#Create a function for prediction 

def diabetes_prediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return ('The person is not diabetic')
    else:
      return ('The person is diabetic')
  
    
  
def main():
    
    # Giving a title
    st.title("Diabetes Prediction Web App")
    
    #Getting the input data from the uer 
    Pregnancies	= st.text_input("Number of Pregnancies")
    Glucose	= st.text_input("Glucoe Level")
    BloodPressure = st.text_input("Blood Presure Value")
    SkinThickness = st.text_input("Skin Thickness value")
    Insulin	= st.text_input("Inulin Value")
    BMI	= st.text_input("BMI Value")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
    Age = st.text_input("Age of the person")
    
    #Code for prediction 
    diganosis = ''
    
    #Creating a button for prediction 
    if st.button("Diabetes Test Result"):
        diganosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction,Age])
    
    st.success(diganosis)
    
if __name__ == "__main__":
    main()



