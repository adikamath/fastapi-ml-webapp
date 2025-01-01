
#install dependencies when creating venv for the first time: pip install fastapi uvicorn

#import required libraries 
import uvicorn 
from fastapi import FastAPI 

#create the app object 
app = FastAPI()

#define Index route which is akin to the homepage, opens automatically on http://127.0.0.1:8000 
@app.get('/') 
def index(): 
    return {'message' : 'Hello there!'}

#Create another route or a page. This page takes in one parameter and returns/ displays a message
@app.get('/Welcome')
def get_name(name : str):
    return {f'Welcome to THE app: {name}'}  

#Run the app with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host = 'http://127.0.0.1', port = 8000)


#run in terminal using the command- uvicorn main:app --reload