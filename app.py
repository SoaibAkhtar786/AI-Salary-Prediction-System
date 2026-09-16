import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Salary Prediction System",
    page_icon="💼",
    layout="centered"
)

# ----------------------------
# Load Model
# ----------------------------
with open("salary_model.pkl", "rb") as file:
    model = pickle.load(file)

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_csv("salary_data.csv")

# ----------------------------
# Title
# ----------------------------
st.title("💼 AI Salary Prediction System")
st.markdown("### Predict Salary using Linear Regression")
st.write("---")

# ----------------------------
# User Input
# ----------------------------
experience = st.slider(
    "Select Years of Experience",
    min_value=0.0,
    max_value=15.0,
    value=1.0,
    step=0.1
)

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict Salary"):

    input_data = pd.DataFrame({
        "YearsExperience": [experience]
    })

    predicted_salary = model.predict(input_data)

    st.success(
        f"Estimated Salary : ₹ {predicted_salary[0]:,.2f}"
    )

# ----------------------------
# Dataset Preview
# ----------------------------
st.write("---")
st.subheader("Dataset Preview")
st.dataframe(df)

# ----------------------------
# Graph
# ----------------------------
st.write("---")
st.subheader("Salary vs Experience")

fig, ax = plt.subplots(figsize=(7, 4))

ax.scatter(
    df["YearsExperience"],
    df["Salary"],
    color="blue",
    label="Actual Data"
)

ax.plot(
    df["YearsExperience"],
    model.predict(df[["YearsExperience"]]),
    color="red",
    linewidth=2,
    label="Regression Line"
)

ax.set_xlabel("Years of Experience")
ax.set_ylabel("Salary")
ax.legend()

st.pyplot(fig)

# ----------------------------
# Footer
# ----------------------------
st.write("---")
st.caption("Developed using Python, Pandas, Matplotlib, Scikit-learn & Streamlit")