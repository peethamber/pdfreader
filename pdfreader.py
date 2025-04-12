import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import os

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file from list below', filenames)
    return os.path.join(folder_path, selected_filename)

st.title("View Lesson Files")
selected_file_path = file_selector()
if selected_file_path and selected_file_path.endswith('.Pdf'):
    pdf_viewer(selected_file_path)
