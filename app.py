import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(page_title="Female Education Risk Predictor", page_icon="📚", layout="wide")

# Title
st.title(" Female Secondary School Completion Risk Predictor")
st.markdown("**SDG 4 – Quality Education | District-Level Analysis | India**")
st.divider()

# Sidebar inputs
st.sidebar.header("🔢 Enter District Details")

enrollment = st.sidebar.number_input("Girls Enrollment Count", min_value=0, max_value=500000, value=5000)
num_schools = st.sidebar.number_input("Number of Schools", min_value=0, max_value=10000, value=100)
sanitation = st.sidebar.number_input("Girls Toilet Count", min_value=0, max_value=10000, value=500)
sex_ratio = st.sidebar.number_input("Sex Ratio (females per 1000 males)", min_value=500, max_value=1100, value=850)
overall_lit = st.sidebar.slider("Overall Literacy Rate (%)", 0.0, 100.0, 65.0)

st.sidebar.divider()
predict_btn = st.sidebar.button("🔍 Predict Risk Level")

# Main area
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Input Summary")
    st.write(f"- Girls Enrollment: **{enrollment}**")
    st.write(f"- Number of Schools: **{num_schools}**")
    st.write(f"- Girls Toilet Count: **{sanitation}**")
    st.write(f"- Sex Ratio: **{sex_ratio}**")
    st.write(f"- Overall Literacy: **{overall_lit}%**")

with col2:
    st.subheader("🎯 Prediction Result")
    if predict_btn:
        input_data = np.array([[enrollment, num_schools, sanitation, sex_ratio, overall_lit]])
        prediction = model.predict(input_data)[0]
        if prediction == 1:
            st.error("🔴 HIGH RISK District")
            st.markdown("This district is likely to have **low female secondary school completion rates.**")
        else:
            st.success("🟢 LOW RISK District")
            st.markdown("This district is likely to have **high female secondary school completion rates.**")
    else:
        st.info("Fill in the details and click Predict.")

st.divider()
st.caption("Developed by Sanjana M | PES University | SRN: PES1PG25CA190")