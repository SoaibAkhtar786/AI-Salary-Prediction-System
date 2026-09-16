# AI Based Salary Prediction System Using Linear Regression

## Project Overview
This project predicts an employee's salary based on years of experience using a Linear Regression Machine Learning model. A Streamlit web application provides an easy-to-use interface for making predictions.

## Features
- Exploratory Data Analysis (EDA)
- Linear Regression Model
- Streamlit Web Interface
- Salary Prediction
- Data Visualization

## Dataset Information
**Dataset:** `salary_data.csv`

Columns:
- YearsExperience
- Salary

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Jupyter Notebook

## Installation Requirements

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install pandas numpy matplotlib scikit-learn streamlit
```

## Project Structure

```text
AI_Salary_Prediction_System/
│── salary_data.csv
│── salary_model.pkl
│── train_model.py
│── app.py
│── EDA_Salary_Prediction.ipynb
│── Project_Synopsis.pdf
│── README.md
│── requirements.txt
```

## Steps to Run

1. Train the model:
```bash
python train_model.py
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open:
`http://localhost:8501`

## Expected Output
- Predict salary from years of experience.
- Display dataset preview.
- Show regression graph.

## Future Scope
- Add education, skills and job role.
- Use larger datasets.
- Deploy online.

## Developed By
**Name:** ____________________

**Course:** B.Tech (Computer Science & Engineering)

**Training:** AI / Machine Learning

**University:** Shaheed Bhagat Singh State University, Ferozepur
