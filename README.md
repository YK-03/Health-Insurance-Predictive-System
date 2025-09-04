# Insurance Cost Prediction Web App

This project is a simple web application built with Streamlit that predicts medical insurance costs based on a person's attributes. It uses a Linear Regression model trained on a dataset of insurance beneficiaries to provide real-time cost estimations.

## 📋 Table of Contents
- [Features](#-features)
- [Demo](#-demo)
- [Project-Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#-usage)
- [Model Details](#-model-details)
- [Dataset](#-dataset)

## ✨ Features

-   **Interactive UI**: A user-friendly web interface built with Streamlit.
-   **Real-time Predictions**: Get instant insurance cost estimates as you adjust the inputs.
-   **Dynamic BMI Calculation**: Automatically calculates Body Mass Index (BMI) from height and weight.
-   **Predicts costs based on**:
    -   Age
    -   Gender
    -   BMI
    -   Number of children
    -   Smoking status
    -   Geographical region

## 📸 Demo

Here is a quick look at the application's user interface:

*(A screenshot of your running Streamlit application would be perfect here!)*

## 📂 Project Structure

The project directory is organized as follows:

```
.
├── insurance.py        # The main Python script for the Streamlit app and ML model
├── insurance.csv       # The dataset used for training the model
└── README.md           # This file
```

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have Python 3.7+ installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1.  **Clone the repository (or download the files)**
    If you are using Git, you can clone the repository. Otherwise, just ensure `insurance.py` and `insurance.csv` are in the same folder.

2.  **Install the required libraries**
    Navigate to your project directory in the terminal and run the following command to install the necessary Python packages:
    ```bash
    pip install streamlit pandas scikit-learn numpy
    ```

## Usage

1.  **Run the application**
    Open your terminal, navigate to the project directory, and execute the following command:
    ```bash
    streamlit run insurance.py
    ```

2.  **Interact with the app**
    Your web browser will automatically open a new tab at `http://localhost:8501`.
    -   Use the sliders, radio buttons, and input fields to enter the required information.
    -   The app will calculate the BMI automatically.
    -   Click the **"Predict Insurance Cost"** button to see the estimated insurance charge.

## 🤖 Model Details

The prediction model is a **Linear Regression** algorithm from the `scikit-learn` library.

-   **Features (X)**: `age`, `sex`, `bmi`, `children`, `smoker`, `region`
-   **Target (Y)**: `charges`

Categorical features (`sex`, `smoker`, `region`) are encoded into numerical values before being fed into the model. The dataset is split into a training set (80%) and a testing set (20%) to train and evaluate the model's performance.

## 📊 Dataset

The project uses the `insurance.csv` dataset, which contains 1338 rows of data about insurance beneficiaries in the United States.

**Columns:**
-   `age`: Age of the primary beneficiary.
-   `sex`: Gender of the beneficiary (`male`, `female`).
-   `bmi`: Body mass index.
-   `children`: Number of children covered by health insurance.
-   `smoker`: Whether the beneficiary is a smoker (`yes`, `no`).
-   `region`: The beneficiary's residential area in the US (`northeast`, `southeast`, `southwest`, `northwest`).
-   `charges`: Individual medical costs billed by health insurance.
