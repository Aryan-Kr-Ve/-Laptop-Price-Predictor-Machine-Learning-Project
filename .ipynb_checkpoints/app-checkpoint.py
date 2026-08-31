import streamlit as st
import pickle
import numpy as np
import pandas as pd


# ============================================================
# LOAD MODEL AND DATA
# ============================================================

pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))


# ============================================================
# TITLE
# ============================================================

st.title("Laptop Price Predictor")

st.write("Enter the laptop configuration to predict its price.")


# ============================================================
# BRAND
# ============================================================

company = st.selectbox(
    "Brand",
    df["Company"].unique()
)


# ============================================================
# TYPE
# ============================================================

laptop_type = st.selectbox(
    "Type",
    df["TypeName"].unique()
)


# ============================================================
# RAM
# ============================================================

ram = st.selectbox(
    "RAM (in GB)",
    [2, 4, 6, 8, 12, 16, 24, 32, 64]
)


# ============================================================
# WEIGHT
# ============================================================

weight = st.number_input(
    "Weight of the Laptop (kg)",
    min_value=0.1,
    max_value=10.0,
    value=1.5,
    step=0.1
)


# ============================================================
# TOUCHSCREEN
# ============================================================

touchscreen = st.selectbox(
    "Touchscreen",
    ["No", "Yes"]
)


# ============================================================
# IPS
# ============================================================

ips = st.selectbox(
    "IPS",
    ["No", "Yes"]
)


# ============================================================
# SCREEN SIZE
# ============================================================

screen_size = st.slider(
    "Screen size (inches)",
    10.0,
    18.0,
    13.0,
    0.1
)


# ============================================================
# SCREEN RESOLUTION
# ============================================================

resolution = st.selectbox(
    "Screen Resolution",
    [
        "1920x1080",
        "1366x768",
        "1600x900",
        "3840x2160",
        "3200x1800",
        "2880x1800",
        "2560x1600",
        "2560x1440",
        "2304x1440"
    ]
)


# ============================================================
# CPU
# ============================================================

cpu = st.selectbox(
    "CPU",
    df["Cpu brand"].unique()
)


# ============================================================
# HDD
# ============================================================

hdd = st.selectbox(
    "HDD (in GB)",
    [0, 128, 256, 512, 1024, 2048]
)


# ============================================================
# SSD
# ============================================================

ssd = st.selectbox(
    "SSD (in GB)",
    [0, 8, 128, 256, 512, 1024]
)


# ============================================================
# GPU
# ============================================================

gpu = st.selectbox(
    "GPU",
    df["Gpu brand"].unique()
)


# ============================================================
# OPERATING SYSTEM
# ============================================================

os = st.selectbox(
    "Operating System",
    df["os"].unique()
)


# ============================================================
# PREDICT PRICE
# ============================================================

if st.button("Predict Price"):

    try:

        # ------------------------------------------------------
        # Convert Yes/No to 1/0
        # ------------------------------------------------------

        touchscreen_value = 1 if touchscreen == "Yes" else 0
        ips_value = 1 if ips == "Yes" else 0


        # ------------------------------------------------------
        # Calculate PPI
        # ------------------------------------------------------

        X_res = int(resolution.split("x")[0])
        Y_res = int(resolution.split("x")[1])

        ppi = (
            np.sqrt(
                (X_res ** 2) +
                (Y_res ** 2)
            )
            / screen_size
        )


        # ------------------------------------------------------
        # CREATE INPUT DATAFRAME
        # ------------------------------------------------------
        # IMPORTANT:
        # "ppi" must be lowercase because this is the
        # column name expected by your trained pipeline.
        # ------------------------------------------------------

        query = pd.DataFrame({
            "Company": [company],
            "TypeName": [laptop_type],
            "Ram": [ram],
            "Weight": [weight],
            "Touchscreen": [touchscreen_value],
            "Ips": [ips_value],
            "ppi": [ppi],
            "Cpu brand": [cpu],
            "HDD": [hdd],
            "SSD": [ssd],
            "Gpu brand": [gpu],
            "os": [os]
        })


        # ------------------------------------------------------
        # PREDICTION
        # ------------------------------------------------------

        prediction = pipe.predict(query)[0]


        # ------------------------------------------------------
        # CONVERT LOG PRICE TO ACTUAL PRICE
        # ------------------------------------------------------

        price = int(np.exp(prediction))


        # ------------------------------------------------------
        # DISPLAY RESULT
        # ------------------------------------------------------

        st.success(
            f"The predicted price of this laptop is ₹{price:,}"
        )

        st.info(
            f"Calculated PPI: {ppi:.2f}"
        )


    except Exception as e:

        st.error(
            "An error occurred while predicting the laptop price."
        )

        st.exception(e)