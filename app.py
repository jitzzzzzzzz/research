import streamlit as st
from PIL import Image
from heart import heart_pred
from cancer import cancer_pred
from diabetes import diabetes_pred
from stroke import stroke_pred
from kidney import kidney_pred

def main():
    # App Sidebar and Page Titles
    st.sidebar.title("HealthGuard")
    menu = ["Home", "Diabetes Prediction", "Heart Disease Prediction", "Chronic Kidney Disease Prediction", 
            "Stroke Prediction", "Cancer Prediction", "About"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Home":
        st.title("🩺 HealthGuard: Your Health Prediction Companion")
        st.image("cover.jpg", use_column_width=True)

        st.write("""
        HealthGuard is a web-based early detection system that uses advanced machine learning algorithms to help identify the risk 
        of multiple diseases based on factors like medical history, lifestyle, and genetics. Our mission is to support healthcare 
        professionals with data-driven insights to improve patient outcomes and promote preventative care.

        ### Disease Predictions Available:
        - **Diabetes Prediction**
        - **Heart Disease Prediction**
        - **Chronic Kidney Disease Prediction**
        - **Stroke Prediction**
        - **Cancer Prediction**

        ### How to Use HealthGuard:
        1. Select a disease prediction option from the sidebar.
        2. Enter the required information.
        3. Click "Predict" to see your result.

        **Note**: HealthGuard provides guidance but is not a substitute for professional medical advice.
        """)

    elif choice == "Diabetes Prediction":
        st.header("Diabetes Prediction")
        diabetes_pred()

    elif choice == "Heart Disease Prediction":
        st.header("Heart Disease Prediction")
        heart_pred()

    elif choice == "Chronic Kidney Disease Prediction":
        st.header("Chronic Kidney Disease Prediction")
        kidney_pred()

    elif choice == "Stroke Prediction":
        st.header("Stroke Prediction")
        stroke_pred()

    elif choice == "Cancer Prediction":
        st.header("Cancer Prediction")
        cancer_pred()

    elif choice == "About":
        st.subheader("👨‍💻 About the Creators")

        col1, col2 = st.columns(2)
        with col1:
            st.write("### Adith Sreeram")
            img1 = Image.open("asr.jpeg")
            st.image(img1, width=150)
            st.markdown("""
            **Adith** is a Data Analytics enthusiast currently pursuing a Bachelor's in Computer Science. 
            With a passion for data science, Adith aims to bring insightful solutions to real-world challenges.
            """)
            st.write("[LinkedIn](http://www.linkedin.com/in/asr373) | [GitHub](https://github.com/ASR373)")

        with col2:
            st.write("### Jithendra Sai")
            img2 = Image.open("sai.jpeg")
            st.image(img2, width=150)
            st.markdown("""
            **Jithendra** is an aspiring data scientist with hands-on experience in predictive modeling and big data. 
            He is committed to making a difference through creative problem-solving and teamwork.
            """)
            st.write("[LinkedIn](https://www.linkedin.com/in/jithendra-sai-8b2b541b8/) | [GitHub](https://github.com/jithendrasai1)")

main()
