import streamlit as st
import numpy as np
import pickle

# load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Prediction")

st.write("Enter all 13 values separated by commas:")

st.caption("Order: CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT")

# single input
input_data = st.text_input("Input values")

if st.button("Predict Price"):
    try:
        # convert input to array
        data = np.asarray(input_data.split(','), dtype=float)

        # reshape
        data = data.reshape(1, -1)

        # check number of features
        if data.shape[1] != 13:
            st.error("Please enter exactly 13 values!")
        else:
            prediction = model.predict(data)
            st.success(f"Estimated Price: ${prediction[0]*1000:.2f}")

    except Exception as e:
        st.error("Invalid input! Please enter numeric values correctly.")