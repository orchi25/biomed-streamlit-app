import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("Clinical Analytics Dashboard")

file_path = "patient_database.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path, on_bad_lines='skip')
    
    # TABS: Clean way to organize dashboards
    tab1, tab2 = st.tabs(["Population Stats", "Raw Data"])
    
    with tab1:
        st.subheader("Patient Demographics")
        
        # BAR CHART: Blood Types
        fig_blood = px.bar(df, x="Blood Type", title="Distribution of Blood Types", color="Blood Type")
        st.plotly_chart(fig_blood)
        
        # SCATTER PLOT: Age Analysis
        # We are creating a jitter plot to see age distribution
        fig_age = px.histogram(df, x="Age", nbins=10, title="Patient Age Distribution")
        st.plotly_chart(fig_age)

    with tab2:
        st.dataframe(df)
        
else:
    st.warning("No patient data found. Please go to the Intake Form and add patients!")
    
st.divider()
st.header("Global Health Research Data")

# Load data directly from a public URL
url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
public_data = pd.read_csv(url)

st.write("Connected to Public Diabetes Database via Cloud URL")

# Interactive Toggle
show_correlations = st.toggle("Show Correlation Heatmap")

if show_correlations:
    # Simple Scatter Matrix to show relationships
    fig = px.scatter_matrix(
        public_data, 
        dimensions=["Glucose", "BloodPressure", "BMI", "Age"],
        color="Outcome",
        title="Diabetes Risk Factors"
    )
    st.plotly_chart(fig)