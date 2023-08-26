# Car Price Prediction with Linear Regression

This project aims to predict car prices using a linear regression model. The project utilizes pandas and numpy for data cleaning and manipulation, trains a linear regression model to achieve an accuracy of 90%, and hosts the model in a Streamlit web app.

## Table of Contents

- [Installation](#installation)
- [Data Cleaning](#data-cleaning)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Streamlit Web App](#streamlit-web-app)
- [Usage Example](#usage-example)

## Installation

Clone the repository:

```bash
git clone https://github.com/Rajkumar0819/CarPricePrediction.git```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

To run the Program:

```bash
streamlit run app.py
```

## Data Cleaning

The data cleaning process involves using pandas and numpy to handle missing values, remove duplicates, and preprocess the dataset for training.

## Model Training and Evaluation

The linear regression model is trained using the preprocessed data. The `file.ipynb` loads th data, cleans it splits it into training and testing sets, trains the model, and evaluates its accuracy.

## Streamlit Web App

The Streamlit web app `app.py` allows users to input car details including company name, car name, fuel type, and kilometers driven. The trained linear regression model predicts the price based on the input and displays the result.

## Usage Example

1. Enter the car details in the Streamlit web app.
2. Click the "Predict Price" button.
3. The app will display the predicted price based on the entered details.

## Screenshot 1
![1](https://github.com/Rajkumar0819/CarPricePrediction/assets/113299030/f6007c26-f278-4fb3-8ed0-2535faa0a793)

## Screenshot 2
![2](https://github.com/Rajkumar0819/CarPricePrediction/assets/113299030/56bb5fb1-6a9d-4429-a995-6d2fb4c7fc11)


