import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import plotly.graph_objects as go

# --- CRISP-DM: Business Understanding ---
st.title("Simple Linear Regression Explorer")
st.header("1. Business Understanding")
st.write("""
This application demonstrates a simple linear regression problem.
The goal is to generate synthetic data based on a linear equation (`y = ax + b + noise`)
and then use a machine learning model to learn the relationship between X and y.
Users can interactively adjust the parameters used for data generation and modeling to understand their effects.
""")

# --- CRISP-DM: Data Understanding & Preparation (Data Generation) ---
st.header("2. Data Generation")
st.write("First, we'll generate our own data. You can control the parameters used to create the dataset.")

# Sliders for user input
st.sidebar.header("Data Generation Controls")
n_points = st.sidebar.slider("Number of data points (n)", 100, 1000, 500)
true_a = st.sidebar.slider("True Coefficient 'a' (y = ax + b + noise)", -10.0, 10.0, 2.0, 0.1)
noise_variance = st.sidebar.slider("Noise Variance (var)", 0, 1000, 100)

# Generate synthetic data
true_b = 50  # Let's define a fixed true intercept
X = np.linspace(0, 100, n_points)
noise = np.random.normal(0, np.sqrt(noise_variance), n_points)
y = true_a * X + true_b + noise

# Reshape for scikit-learn
X_reshaped = X.reshape(-1, 1)
df = pd.DataFrame({'X': X, 'y': y})

st.subheader("Generated Data Preview")
st.write(df.head())

# --- CRISP-DM: Modeling ---
st.header("3. Modeling")
st.write("Now, we'll use `scikit-learn`'s `LinearRegression` model to learn the relationship from the generated data.")

# Train the model
model = LinearRegression()
model.fit(X_reshaped, y)

# Get learned coefficients
learned_a = model.coef_[0]
learned_b = model.intercept_

st.write(f"**True Equation:** `y = {true_a:.2f} * X + {true_b:.2f} + noise`")
st.write(f"**Model's Learned Equation:** `y = {learned_a:.2f} * X + {learned_b:.2f}`")

# Interactive slider for 'a'
st.sidebar.header("Model Exploration")
st.write("You can also manually modify the slope 'a' to see how it affects the evaluation metrics and the plot.")
modified_a = st.sidebar.slider("Modify slope 'a'", -10.0, 10.0, learned_a, 0.1)


# --- CRISP-DM: Evaluation ---
st.header("4. Evaluation")
st.write("Let's evaluate how well our model performed and compare it to the manually modified line.")

# Make predictions
y_pred_learned = model.predict(X_reshaped)
y_pred_modified = modified_a * X + learned_b # Use the model's intercept

# Calculate metrics
mse_learned = mean_squared_error(y, y_pred_learned)
r2_learned = r2_score(y, y_pred_learned)

mse_modified = mean_squared_error(y, y_pred_modified)
r2_modified = r2_score(y, y_pred_modified)

col1, col2 = st.columns(2)
with col1:
    st.write(f"**Learned Model's Performance:**")
    st.write(f"  - MSE: {mse_learned:.2f}")
    st.write(f"  - R2 Score: {r2_learned:.2f}")

with col2:
    st.write(f"**Modified Model's Performance (a={modified_a:.2f}):**")
    st.write(f"  - MSE: {mse_modified:.2f}")
    st.write(f"  - R2 Score: {r2_modified:.2f}")


# --- CRISP-DM: Deployment (Visualization) ---
st.header("5. Visualization")
st.write("The plot below shows the original data points and the different regression lines.")

fig = go.Figure()

# 1. Scatter plot of the actual generated data
fig.add_trace(go.Scatter(x=X, y=y, mode='markers', name='Generated Data (y)', marker=dict(opacity=0.6)))

# 2. True regression line
y_true_line = true_a * X + true_b
fig.add_trace(go.Scatter(x=X, y=y_true_line, mode='lines', name=f'True Line (a={true_a:.2f})', line=dict(color='red', width=3)))

# 3. Model's learned regression line
fig.add_trace(go.Scatter(x=X, y=y_pred_learned, mode='lines', name=f'Learned Line (a={learned_a:.2f})', line=dict(color='green', width=3, dash='dash')))

# 4. Manually modified regression line
y_pred_modified_line = modified_a * X + learned_b
fig.add_trace(go.Scatter(x=X, y=y_pred_modified_line, mode='lines', name=f'Modified Line (a={modified_a:.2f})', line=dict(color='orange', width=3, dash='dot')))


fig.update_layout(
    title="Exploring Simple Linear Regression",
    xaxis_title="X",
    yaxis_title="y",
    legend_title="Lines"
)
st.plotly_chart(fig)

# --- CRISP-DM: Deployment ---
st.header("6. Deployment")
st.write("""
This Streamlit application itself is the deployment of the model.
To run this application locally, ensure you have Python and the required packages installed (`streamlit`, `pandas`, `numpy`, `scikit-learn`, `plotly`).

**Run the app with the command:**
```bash
streamlit run app.py
```
""")