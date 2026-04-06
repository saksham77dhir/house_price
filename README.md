# 🏠 House Price Prediction Web App

This project is a **Machine Learning-based web application** built using **Streamlit** that predicts house prices based on various property and location features.

---

## 📌 Overview

The application uses the **Boston Housing Dataset** to estimate house prices using an advanced regression model.

- Input: 13 housing features  
- Output: Estimated house price  

---

## ⚙️ Technologies Used

- Python  
- NumPy  
- Pandas  
- Scikit-learn  
- XGBoost  
- Streamlit  
- Pickle  

---

## 📊 Dataset Information

- Dataset: Boston Housing Dataset  
- Total Features: 13  
- Target Variable:
  - `MEDV` → Median house price (in $1000s)

---

## 🧠 Machine Learning Model

- Model: XGBoost Regressor  
- Type: Supervised Learning (Regression)  
- No feature scaling required (tree-based model)

The trained model is saved as a `.pkl` file and used in the Streamlit app.

---

## 📥 Input Features

The model uses the following features:

1. CRIM – Crime rate  
2. ZN – Residential land proportion  
3. INDUS – Industrial proportion  
4. CHAS – Charles River (0 or 1)  
5. NOX – Nitric oxide concentration  
6. RM – Average number of rooms  
7. AGE – Old houses proportion  
8. DIS – Distance to employment centers  
9. RAD – Highway access index  
10. TAX – Property tax rate  
11. PTRATIO – Pupil-teacher ratio  
12. B – Population factor  
13. LSTAT – Lower status percentage  

---
