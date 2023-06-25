# Importing the required libraries
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

# Create a FastAPI instance
app = FastAPI()

# Define a data model using the Pydantic BaseModel
class model_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# Loading the saved model
diabetes_model = pickle.load(open('C:/Users/Tariq/Downloads/Temp Projects/17-Diabetes Prediction V2/trained_model.sav', 'rb'))

# Define the endpoint for diabetes prediction
@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters: model_input):
    # Convert the input parameters to JSON string
    input_data = input_parameters.json()
    # Convert the JSON string to a dictionary
    input_dictionary = json.loads(input_data)
    
    # Extract the input features from the dictionary
    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']

    # Create a list of input features
    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]

    # Perform diabetes prediction using the loaded model
    prediction = diabetes_model.predict([input_list])

    # Determine the prediction result
    if prediction[0] == 0:
        result = 'Not Diabetic'
        return result
    else:
        result = 'Diabetic'
        return result

