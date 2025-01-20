import streamlit as st 
import time


if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False

def begin_callback():
        # "Yes" button was clicked
        st.session_state.button_clicked = True

def no_callback():
        # "No" button was clicked
        alert = st.warning("Please go back to the main page")
        time.sleep(3)
        alert.empty()

def calibration_callback():
        st.session_state.button_clicked = False
        st.write("Success")
def yes_callback():
        
        st.session_state.button_clicked = False
        st.write("Would you like to begin data collection?")
        st.button("Begin Calibration",on_click =calibration_callback)


if not st.session_state.button_clicked:
        st.button("Click Here to Begin Data Collection", on_click=begin_callback)

else:
        st.warning("BEFORE SELECTING YES: place one sensor on your sternum and the other on your lower back. Once you have done that, please click yes to begin calibration.")
        st.button("yes", on_click=yes_callback)
        st.button("no", on_click=no_callback)
        
