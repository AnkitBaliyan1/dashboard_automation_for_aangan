import numpy as np
import pandas as pd
import streamlit as st
from utils import *
import re

def main():
    
    st.title("Aangan DashEase")
    
    data = st.sidebar.file_uploader("Enter the CSV file", type="csv")
    user_input = st.text_area("Enter the list of columns (separated by comma or space) for analysis")
    percentage = st.sidebar.checkbox("Get Percentage")
    
    filter_button = st.sidebar.checkbox("Add Filter")
    
    if filter_button:
        filter_column_name = st.sidebar.text_input("Name of Column you wish to filter by")
        if filter_column_name:
            filter_pass = True
    
        else:
            st.write("Enter the block name above to proceed")
            filter_pass=False
    else:
        filter_column_name = None
        filter_pass=True
        
    
    
    percent = 1 if percentage else 0
    
    if filter_pass:
    
        if data and user_input:
    
            items_list = re.split(r'[,\s]+', user_input.strip())
            items_list = [item.strip() for item in items_list if item.strip()]
    
            df, filter_by = get_data(data, filter_column_name)
    
            if df is not None and st.button("Get Dashboard"):
                if filter_by is not None:
                    
                    st.success(f"Dashboard filtered with respect to \"{filter_column_name}\" - {filter_by}")
    
    
                get_view(df, items_list, percent)
    
                
    
    
        elif data:
            st.error("Enter the list of columns you wish to analyse")
    
        elif user_input:
            st.error("Enter the data for analysis.")
    
        else:
            st.error("No input detected, Enter the desired information.")

    if st.sidebar.button("About"):
            about_text = open("README.md", 'r').read()
            st.markdown(about_text)

if __name__ == '__main__':
    main()
        
