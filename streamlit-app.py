import streamlit as st
import pandas as pd

st.set_page_config(page_title="final-project", layout="centered")
st.title("final project")
st.markdown("This Streamlit app uses historical software metrics to predict the likelihood of bugs in code.")

# Upload dataset
uploaded_file = st.file_uploader(" Upload your dataset (CSV format)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader(" Data Preview")
    st.dataframe(df.head())

    # Placeholder prediction logic (you can replace with your trained model later)
    st.subheader(" Predicted Bug Likelihood (Demo Output)")
    df['Bug_Prediction'] = ['Bug' if i % 2 == 0 else 'No Bug' for i in range(len(df))]
    st.dataframe(df[['Bug_Prediction']])
else:
    st.info("Please upload a CSV file to begin prediction.")
