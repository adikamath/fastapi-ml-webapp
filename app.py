''' Initially, make sure to install all the required packages that are listed in the requirements.txt file 
using: pip install -r requirements.txt ''' 

'''Finally, to run the web app use the following command in the terminal: uvicorn app:app --reload 
   In the above command, the first parameter is your webapp's python filename i.e., app and the second parameter is the name of the FastAPI 
   object inside the webapp Python file which in this case is again app'''

'''To check out the swagger UI/ endpoints documentation of the webapp go to the following URL once the webapp is running- http://127.0.0.1:8000/docs '''

# Import the required libraries

# ASGI web server library
import uvicorn
# Web framework/ API framework 
from fastapi import FastAPI 
# Pydantic class that you defined for data validation
from Banknote_DataValidation import DataValidation
# libraries for data manipulation 
import numpy as np
import pandas as pd 
#library to manage pickle file of the ML model 
import pickle

# Instantiate the FastAPI app 
app = FastAPI() 

# Load the serialized pickle file of the trained model you created using the Jupyter Notebook
pickle_in = open("classifier.pkl", "rb") 
classifier = pickle.load(pickle_in) 

'''Create the different routes of the web app. These are like pages of a website where each 
route is essentially an API endpoint. As a rule of thumb in this case: 

        - Use GET requests for endpoints when passing simple data to the server 
        - Use POST requests for endpoints when the data being passed to the server is complex 
              and will involve significant server-side operations like prediction or classification
''' 

# Index route, this is default route that automatically opens at http://127.0.0.1:8000
@app.get("/")
def index():
    return {"messaage" : "Banknote classifier app"}

# A Route that takes a single parameter and returns the value passed to it with a message 
@app.get("/{name}")
def get_name(name:str):
    return(f"Welcome {name}, to the Banknote classifier app!")

# Create a route for the classification functionality
@app.post("/classify")
def classify_banknote(data:DataValidation):
    
    # store the values passed through the API endpoint
    data = data.dict()
    variance = data["variance"]
    skewness = data["skewness"]
    curtosis = data["curtosis"]
    entropy = data["entropy"]

    # Get the prediction by passing the feature values to the model return the prediction
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])

    if prediction[0] > 0.5:
        prediction = "Fake Banknote" 
    
    else: 
        prediction = "Authentic Banknote" 

    return prediction

# Run the webapp with uvicorn; Access it at http://127.0.0.1:8000 
if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)