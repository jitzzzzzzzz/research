# Importing required packages
import streamlit as st
from PIL import Image

# Importing disease prediction functions
from heart import heart_pred
from cancer import cancer_pred
from diabetes import diabetes_pred
from stroke import stroke_pred
from kidney import kidney_pred

# Function for the main interface
def main():
    st.set_page_config(page_title="HealthGuard", page_icon="🩺", layout="centered")

    # Sidebar menu
    menu = ["Home", "Diabetes Prediction", "Heart Disease Prediction", 
            "Chronic Kidney Disease Prediction", "Stroke Prediction",
            "Cancer Prediction", "About"]
    choice = st.sidebar.selectbox("Navigation Menu", menu)

    # Home Page
    if choice == "Home":
        st.markdown("<h1 style='text-align: center;'>HealthGuard: Early Detection System</h1>", unsafe_allow_html=True)
        st.image("cover.jpg", use_column_width=True, caption="Your health guardian powered by AI")

        st.markdown("""
            ### Welcome to HealthGuard
            HealthGuard leverages advanced machine learning algorithms to predict the likelihood of developing various diseases, 
            based on personal health data, lifestyle, and other risk factors. This app aims to support early detection and 
            intervention, allowing for timely medical attention to improve health outcomes.

            #### Features:
            - **Diabetes Prediction**: Determine your risk for Diabetes.
            - **Heart Disease Prediction**: Assess the likelihood of heart disease.
            - **Kidney Disease Prediction**: Identify the risk of chronic kidney disease.
            - **Stroke Prediction**: Evaluate your stroke risk.
            - **Cancer Prediction**: Check your risk of certain cancers.

            **Explore the sections from the sidebar to get started.**
        """)
    
    # Prediction Pages
    elif choice == "Diabetes Prediction":
        st.subheader("Diabetes Prediction")
        diabetes_pred()
        
    elif choice == "Heart Disease Prediction":
        st.subheader("Heart Disease Prediction")
        heart_pred()
        
    elif choice == "Chronic Kidney Disease Prediction":
        st.subheader("Chronic Kidney Disease Prediction")
        kidney_pred()
        
    elif choice == "Stroke Prediction":
        st.subheader("Stroke Prediction")
        stroke_pred()
        
    elif choice == "Cancer Prediction":
        st.subheader("Cancer Prediction")
        cancer_pred()
        
    # About Page
    else:
        st.subheader("About the Creators")
        
        # Profile cards
        col1, col2 = st.columns(2)
        
        with col1:
            st.image("asr.jpeg", width=150)
            st.markdown("### Adith Sreeram")
            st.markdown("""
                **BSc in Computer Science (Data Analytics)**  
                Passionate about data-driven solutions in healthcare and machine learning.  
                - [LinkedIn](http://www.linkedin.com/in/asr373)  
                - [GitHub](https://github.com/ASR373)  
                - [Email](mailto:adithnadar@gmail.com)
            """)
        
        with col2:
            st.image("sai.jpeg", width=150)
            st.markdown("### Jithendra Sai")
            st.markdown("""
                **BSc in Computer Science (Data Analytics)**  
                Focused on big data and predictive modeling in healthcare.  
                - [LinkedIn](https://www.linkedin.com/in/jithendra-sai-8b2b541b8/)  
                - [GitHub](https://github.com/jithendrasai1)  
                - [Email](mailto:jithendrasaipappuri@gmail.com)
            """)

if __name__ == '__main__':
    main()
