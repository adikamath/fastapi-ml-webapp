
'''This code defines the data model that will be used to validate
the inputs to the classification API'''

# Import the BaseModel class that let's us define data models with type validation
from pydantic import BaseModel 

# Define the data model
class DataValidation(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float