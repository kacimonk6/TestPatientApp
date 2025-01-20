import streamlit as st
import pandas as pd
import supabase
from supabase import create_client, Client


##rename multipage app to title of app
st.markdown("<h1 style = 'text-align: center; color: #001e69; '>Welcome to the LETREP25 Project! Please use the left sidebar to access data collection</h1>", unsafe_allow_html=True)
st.sidebar.success("Select a page from the list")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("letulogo.png")

st.markdown("<h1 style = 'text-align: center; color: #001e69; font-size: 20px; '>Patient Interface</h1>", unsafe_allow_html=True)



# Supabase credentials
url = "https://hghjfrcvvyhkcopnebbb.supabase.co" 
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhnaGpmcmN2dnloa2NvcG5lYmJiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzAyMDc3ODcsImV4cCI6MjA0NTc4Mzc4N30.cUReuxG7PRCWIheOWI-yp2PVWRnyMwtNVwDd1z5s4g0" 
supabase = supabase.create_client(url, key)


# File details



    
bucket_name = "LETREPbucket"
file_name = st.empty()
file_name.text_input("Please enter the patient's ID", value="", key="1")
#file_name = st.text_input("Please enter the patient's ID number")

# Download the file
try:
    response = supabase.storage.from_(bucket_name).download(file_name)

    # Check for errors
    if response.error:
        raise Exception(response.error.message)

    # Save the file locally
    with open(file_name, "wb") as file:
        file.write(response.data)

    st.write(f"File '{file_name}' downloaded successfully.")

except Exception as e:
    st.write(f"Error downloading file: {e}")