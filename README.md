# 👨‍🎓 Author & Project Details
Author: Aryan Kumar Verma

Program: Master of Computer Applications (MCA)

Semester & Section: 3rd Semester — Section 'B'

Roll Number: MCA/40081/25

Project Type: 3rd Semester Mini Project
# 💻 Laptop Price Predictor

An end-to-end Machine Learning web application designed to predict laptop prices accurately based on user-specified hardware and software specifications. This project was developed as part of the **MCA 3rd Semester Mini Project** curriculum.

---

## 📌 Project Overview

With hundreds of laptop configurations available on the market, pricing can vary drastically based on specifications such as processor type, RAM, storage configuration, GPU, and screen resolution. 

This project cleans, processes, and analyzes historical laptop dataset features, applies feature engineering, and evaluates multiple machine learning regression algorithms to find the best-performing model for laptop price estimation.

### 🎯 Key Highlights
- **Final Model Accuracy / $R^2$ Score:** **~89%**
- **Exploratory Data Analysis (EDA):** Deep dive into correlations between hardware features and price trends.
- **Preprocessing Pipeline:** Custom handling for categorical features (One-Hot Encoding) and target transformation (Log-transform on price).
- **Interactive UI:** Web interface to enter laptop configurations and get instant price predictions.

---

## ⚙️ Features & Inputs

The model predicts prices based on the following configurations:
- **Brand / Company:** Apple, Dell, HP, Lenovo, Asus, Acer, MSI, etc.
- **Type:** Ultrabook, Gaming, Notebook, Netbook, Workstation, 2-in-1 Convertible
- **RAM:** 2GB to 64GB
- **Weight:** In kilograms (kg)
- **Touchscreen & IPS Display:** Yes / No
- **Screen Size & Resolution:** Full HD, 4K, Retina, etc. (Calculates Pixels Per Inch - PPI)
- **CPU:** Intel (Core i3, i5, i7, others) / AMD Processors
- **HDD & SSD:** Storage combinations in GB / TB
- **GPU:** Intel, Nvidia, AMD
- **Operating System:** Windows, macOS, Linux/Other

---

## 🧠 Machine Learning Models Evaluated

To ensure maximum prediction accuracy, several regression algorithms were trained and benchmarked:

| Model | Evaluated |
|---|---|
| Linear Regression | Yes |
| Ridge & Lasso Regression | Yes |
| K-Nearest Neighbors (KNN) | Yes |
| Decision Tree Regressor | Yes |
| Random Forest Regressor | Yes |
| Extra Trees Regressor | Yes |
| AdaBoost Regressor | Yes |
| Gradient Boosting Regressor | Yes |
| XGBoost Regressor | Yes |
| **Voting / Stacking Regressor** | **Best Performance (~89% accuracy)** |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Data Analysis & Processing:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-Learn, XGBoost
- **Model Deployment / Web UI:** Streamlit / Flask
- **Model Serialization:** Pickle

---

## 📂 Project Structure

```text
├── dataset/
│   └── laptop_data.csv          # Raw and cleaned dataset
├── notebooks/
│   └── laptop_price_eda.ipynb   # EDA, Data Cleaning & Model Training
├── models/
│   ├── pipe.pkl                 # Trained ML Pipeline
│   └── df.pkl                   # Processed DataFrame reference
├── app.py                       # Streamlit / Web application script
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
