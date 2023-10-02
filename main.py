import pandas as pd
import numpy as np
import streamlit as st
import time
import re


st.title("Generate Trace Matrix")

def simulate_data_processing():
    # Simulating some data processing task
    time.sleep(3)
    return "Trace Matrix   successfully generated. [Click here to view](https://docs.google.com/spreadsheets/d/19ZW_Eq3ySx925glrnokXDLBvx69_A7sTP02f8-NuB4Q/edit#gid=28624861)"
user_input = st.text_input("Please Enter the uri of the application", " ")
option = st.selectbox("Select an option:", ["Risk Analysis", "URS"])
grant_access = st.checkbox("Grant edit access to  services@pcube.com")
    
              
if st.button("Submit"):
    with st.spinner("Processing..."):
    
        time.sleep(3)
        success_message = "Trace Matrix successfully generated. [Click here to view](https://docs.google.com/spreadsheets/d/1lWuVtD4iqYprCtteKHEK5Ol_7_poU21Z6L-OlMQQlTQ )"
        st.success(success_message)


