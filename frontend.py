import streamlit as st
import requests

# Set the base URL for your FastAPI app
BASE_URL = "http://127.0.0.1:8000"

# Create a title for the FastAPI app that will be always shown on any route
st.title("Banknote Classifier App")

# Create a navigation menu for Users to navigate to the two main routes of the web app/ two main endpoints
menu = ["Welcome Page", "Classify Your Banknotes"]
choice = st.sidebar.selectbox("Choose an option", menu)

# Logic for the "Welcome Page" that will take a string input, feed it to the endpoint and output a welcome message on screen
if choice == "Welcome Page":
    # Sub-heading that will be shown to the User
    st.subheader("Welcome Page")
    name = st.text_input("Please enter your name:", "")
    if st.button("Greet Me"):
        if name:
            # If you get a valid string input then invoke the  of your web app with the string input
            response = requests.get(f"{BASE_URL}/{name}")
            st.success(response.text)
        else:
            # Display an error warning asking the User to enter a valid string to execute the greeting
            st.warning("Please enter your name!")

# The page and logic that will be triggered if the User chooses the Banknote Classifier option from the menu
elif choice == "Classify Your Banknotes":

    # Sub-heading that will be shown to the User
    st.subheader("Please enter values for the model's input features")

    # For each input feature, store the value that the User passes; The default value is None
    variance = st.number_input("Variance", value = None)
    skewness = st.number_input("Skewness", value = None)
    curtosis = st.number_input("Curtosis", value = None)
    entropy = st.number_input("Entropy", value = None)
        
    # If the button is clicked by the User then proceed to making the HTTP POST request using the endpoint
    if st.button("Classify", icon = "🔎"):
       
       # First check if the User has entered values for all the input features
       if all(value != None for value in [variance, skewness, curtosis, entropy]):
            # Create dictionary payload for the POST request
            payload = {
                "variance": variance,
                "skewness": skewness,
                "curtosis": curtosis,
                "entropy": entropy,
            }
            # Send POST request to API endpoint
            try:
                # HTTP POST request
                response = requests.post(f"{BASE_URL}/classify", json=payload)

                # If the HTTP request is successful, then extract the value from JSON response
                if response.status_code == 200:
                    classification = response.json()
                    st.success(f"Classification: {classification}")
                
                # Else return an error; This error is for cases where the network request was sent to the server but returned an error
                else:
                    st.error("Error: Unable to classify banknote")

            # This except block handles all other errors where the network request didn't even go through to the server
            except requests.exceptions.RequestException as e:
                st.error(f"Error Message: {e}")

       else:
          st.warning("Please enter valid numerical values for all input features")

