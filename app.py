
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import plotly.graph_objects as go

# CRISP-DM: Business Understanding
st.title("HW1: Simple Linear Regression with Tesla Stock Price")
st.header("CRISP-DM: 1. Business Understanding")
st.write("""
This project aims to solve a simple linear regression problem using Tesla (TSLA) stock data.
The goal is to predict the closing price of the stock based on its opening price.
This web application allows for interactive exploration of the linear regression model and its parameters.
""")

# CRISP-DM: Data Understanding
st.header("CRISP-DM: 2. Data Understanding")
st.write("We will use Yahoo Finance (`yfinance`) to get the historical stock data for Tesla (TSLA).")

# Fetching data
@st.cache_data
def load_data(ticker):
    return yf.download(ticker, start="2020-01-01", end="2023-12-31")

data_load_state = st.text('Loading data...')
tsla_data = load_data('TSLA')
data_load_state.text('Loading data... done!')

st.subheader("Raw Data")
st.write(tsla_data.tail())

# CRISP-DM: Data Preparation
st.header("CRISP-DM: 3. Data Preparation")
st.write("We will use the 'Open' price as our feature (X) and the 'Close' price as our target (y).")
st.write("You can adjust the number of data points and the level of noise to add to the data.")

# Interactive elements
n_points = st.slider("Number of data points", 100, len(tsla_data), 250)
noise_level = st.slider("Noise level", 0.0, 100.0, 0.0)

# Prepare data
data = tsla_data[['Open', 'Close']].copy().tail(n_points)
if noise_level > 0:
    noise = np.random.normal(0, noise_level, data.shape)
    data += noise

X = data[['Open']]
y = data['Close']

# CRISP-DM: Modeling
st.header("CRISP-DM: 4. Modeling")
st.write("We will use a simple linear regression model from `scikit-learn`.")

# Train the model
model = LinearRegression()
model.fit(X, y)
a = model.coef_[0]
b = model.intercept_

st.write(f"The model equation is: `Close = {a.item():.2f} * Open + {b.item():.2f}`")

# Allow user to modify 'a'
st.write("You can modify the slope 'a' to see how it affects the regression line.")
a_modified = st.slider("Modify slope 'a'", -2.0, 2.0, a.item(), 0.01)

# CRISP-DM: Evaluation
st.header("CRISP-DM: 5. Evaluation")
st.write("We will evaluate the model using Mean Squared Error (MSE) and R-squared (R2).")

# Make predictions
y_pred = model.predict(X)
y_pred_modified = a_modified * X['Open'] + b

mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

mse_modified = mean_squared_error(y, y_pred_modified)
r2_modified = r2_score(y, y_pred_modified)

st.write(f"**Model's Performance:**")
st.write(f"  - MSE: {mse:.2f}")
st.write(f"  - R2 Score: {r2:.2f}")

st.write(f"**Modified Model's Performance (with a={a_modified:.2f}):**")
st.write(f"  - MSE: {mse_modified:.2f}")
st.write(f"  - R2 Score: {r2_modified:.2f}")

# Visualization
st.subheader("Regression Plot")
fig = go.Figure()

# Original data
fig.add_trace(go.Scatter(x=X['Open'], y=y, mode='markers', name='Actual Data'))

# Model's regression line
fig.add_trace(go.Scatter(x=X['Open'], y=y_pred, mode='lines', name=f'Model (a={a.item():.2f})'))

# Modified regression line
fig.add_trace(go.Scatter(x=X['Open'], y=y_pred_modified, mode='lines', name=f'Modified (a={a_modified:.2f})', line=dict(dash='dash')))

fig.update_layout(
    title="Tesla Stock: Open vs. Close Price",
    xaxis_title="Open Price",
    yaxis_title="Close Price"
)
st.plotly_chart(fig)


# CRISP-DM: Deployment
st.header("CRISP-DM: 6. Deployment")
st.write("""
This Streamlit application is a form of deployment. To run this application locally, you need to have Python and the required packages installed.

1.  **Install packages:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the app:**
    ```bash
    streamlit run app.py
    ```

For cloud deployment, you can use services like Streamlit Community Cloud, Heroku, or AWS.
""")

st.header("Prompt and Process")
st.write("""
**Prompt:** "I have a class assignment. Can you help me with a Tesla stock price project? HW1: write python to solve simple linear regression problem, following CRISP-DM steps, with prompt and process, not just code and result. 1. CRISP-DM 2. allow user to modify a in ax+b, noise, number of points 3. streamlit or flask web, framework deployment"

**Process:**
1.  **Business Understanding:** Defined the project's goal - predicting closing price from opening price.
2.  **Data Understanding:** Chose `yfinance` to get Tesla's stock data.
3.  **Data Preparation:** Selected 'Open' and 'Close' columns, and added sliders for user to control data points and noise.
4.  **Modeling:** Used `scikit-learn`'s `LinearRegression` to build the model.
5.  **Evaluation:** Calculated MSE and R2 score to evaluate the model. Added a slider for the user to modify the slope 'a' and see the impact on the evaluation metrics.
6.  **Deployment:** Deployed the model as a Streamlit web app and provided instructions for running it locally and deploying it to the cloud.
""")
