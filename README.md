# Simple Linear Regression Explorer

## 📖 Overview

This project is an interactive web application built with Streamlit that allows users to explore the concepts of simple linear regression. Instead of using a static dataset, it generates synthetic data based on user-defined parameters, fits a linear regression model to the data, and visualizes the results.

The application is structured following the **CRISP-DM (Cross-Industry Standard Process for Data Mining)** methodology, walking through the steps from business understanding to deployment.

## ✨ Features

- **Interactive Data Generation:** Dynamically create a dataset by specifying:
    - Number of data points
    - The true underlying slope (`a`) of the data
    - The amount of random noise (variance)
- **Model Training:** A simple linear regression model from `scikit-learn` is trained on the generated data.
- **Interactive Evaluation:**
    - See the "true" equation used to generate the data versus the equation learned by the model.
    - Manually adjust the model's slope (`a`) to see how it impacts the regression line and evaluation metrics (MSE and R² Score).
- **Rich Visualization:** A Plotly chart displays:
    - The raw generated data points (scatter plot).
    - The "true" line used to generate the data.
    - The line learned by the regression model.
    - The user-modified regression line.

## 🛠️ Installation & Setup

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/brant502/5114056-HW1.git
    cd 5114056-HW1
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    The required Python packages are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

Once the setup is complete, you can run the Streamlit application with the following command:

```bash
streamlit run app.py
```

This will start a local web server and open the application in your default web browser.

## 📦 Dependencies

This project relies on the following main Python libraries:

-   `streamlit`
-   `pandas`
-   `numpy`
-   `scikit-learn`
-   `plotly`
-   `yfinance` (Note: This was used in a previous version and is no longer required for the current synthetic data generation but remains in the requirements file).
