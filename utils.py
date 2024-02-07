import pandas as pd
import numpy as np
import streamlit as st



def get_data(data, filter_column_name):

    data = pd.read_csv(data)
    df = data.head(69)
    #df = df.astype(str)
    df.fillna("No Answer", inplace=True)
    
    if filter_column_name is not None:
        if filter_column_name in df.columns:
            filter_by = st.sidebar.selectbox(f"Choose the values from \"{filter_column_name}\" values",df[filter_column_name].unique().tolist())

            filtered_df = df[df[filter_column_name]==filter_by]

            return filtered_df, filter_by
                
        else:
            st.error(f"No column called \"{filter_column_name}\" in given dataset")
            return None, None

    else:
        return df, None


def get_view(df, col_list, percent):



    new_df = pd.DataFrame()

    for col in col_list:
        if col in df.columns:
            if percent==0:
                # Create a Series with the value counts of the current column
                series = df[col].value_counts()
            elif percent==1:
                series = df[col].value_counts(normalize=True)*100
                series = series.round(2)
                

            # Add the Series to the new DataFrame as a new column
            new_df[col] = series

        else:
            st.error(f"Column: \"{col}\" not found in the dataset to generate view.")

    view = new_df.T
    view.reset_index(inplace=True)

    if percent==1:
        st.subheader("Percentage view")
    
    st.write(view)
