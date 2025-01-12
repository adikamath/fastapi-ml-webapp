# FastAPI Web App: Banknote Classifier 

## Introduction

My goal with this project was to learn how API endpoints work by creating a web app. In the process, I also wanted to learn how to use API endpoints to deploy ML models and as a stretch goal, create a user interface for the web app that Users could use to interact with the model and make predictions. In my search online to look for material to learn from, I came across this [mini-series by Krish Naik](https://www.youtube.com/playlist?list=PLZoTAELRMXVPgsojPOHF9i0u2L83-m9P7) which this project is largely inspired by. I went an extra step and created a simple front end/ user interface for Users to interact easily with the web app. 

Here's a high-level overview of the tech stack: 

- [Uvicorn](https://www.uvicorn.org): a Python-based web server.
- [FastAPI](https://fastapi.tiangolo.com): a simple Python-based web framework that we use to create the API endpoints for our web app.
- [scikit-learn](https://scikit-learn.org/stable/): a Python machine learning library that has some very common built-in machine learning models and machine learning tool APIs available. We'll use this to build and train our classification model. 
- [pickle](https://docs.python.org/3/library/pickle.html): a library that we will use to serialize our trained model which we can then expose to an API endpoint in our web app.
- [Streamlit](https://streamlit.io): we'll use this framework to create the frontend user interface for our web app.

The machine learning model we will train and deploy via the web app is a Random Forest classification model that is trained to classify Banknotes as authentic or fake. The training dataset for the model is the [Banknote Authentication dataset (UC Irvine Machine Learning Repository)](https://archive.ics.uci.edu/dataset/267/banknote+authentication).

One last thing to note is that this project does not go over how to deploy the web app over the web but just to create a working web app that you can run in your local environment.

## Installation & Usage

- Install the latest versions of [Python](https://www.python.org) and [pip](https://pip.pypa.io/en/stable/) (package installer) in your local environment.
- Create a directory for your project and, create and run a virtual environment. 
- Use pip to install all dependencies listed in the requirements.txt file. 
- Start the web server and run the web app using the following command in your terminal - uvicorn app:app --reload 
- Run the Streamlit server using the following command in your terminal: streamlit run frontend.py 
- The app should open in your browser.

## Attribution 

- **Dataset**: [Banknote Authentication (UC Irvine Machine Learning Repository)](https://archive.ics.uci.edu/dataset/267/banknote+authentication)
- **FastAPI Tutorial**: [FastAPI Deployment Tutorials (By Krish Naik)](https://www.youtube.com/playlist?list=PLZoTAELRMXVPgsojPOHF9i0u2L83-m9P7)

## My Blog 
[www.adityakamath.com](https://adityakamath.com)

## License

This project is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). 

You are free to:
- Share: Copy and redistribute the material in any medium or format.
- Adapt: Remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:
- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

For more details, see the full [license text](https://creativecommons.org/licenses/by/4.0/legalcode).