# Lab 4: Airbnb Price Prediction with Machine Learning and Streamlit

## Overview
This assignment builds an end-to-end machine learning workflow for predicting Airbnb nightly prices using the New York City Airbnb Open Data dataset. The project combines data exploration, feature engineering, regression modeling, hyperparameter tuning, and deployment into a user-friendly Streamlit web application.

The objective is to understand the key factors affecting Airbnb listing prices and to create a model that can estimate a listing’s expected nightly rate based on its characteristics.

## Project Structure
- `202618052_Lab_4.ipynb`: Jupyter notebook containing the complete implementation of the assignment, including exploratory analysis, preprocessing, model training, evaluation, and tuning.
- `app.py`: Streamlit application that accepts listing details from the user and predicts the estimated nightly price.
- `AB_NYC_2019.csv`: Dataset used for analysis and model development.
- `Readme.md`: Project overview, workflow, setup instructions, and key findings.

## Dataset
- **Title:** New York City Airbnb Open Data
- **Source & Link:** Kaggle / Airbnb NYC dataset — https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data
- **Notes:** The dataset contains listings with attributes such as neighbourhood, room type, geographic coordinates, availability, review statistics, and price.

## Key Components

1. **Data Loading and Initial Exploration**
   - Load the Airbnb dataset into a Pandas DataFrame.
   - Inspect the shape, data types, and missing values.
   - Review summary statistics to understand the feature distribution and data quality.

2. **Exploratory Data Analysis (EDA)**
   - Analyze the price distribution and identify high-priced listings.
   - Investigate the impact of neighbourhood, room type, and listing attributes on price.
   - Check skewness, outliers, and data irregularities in the target variable.

3. **Data Cleaning and Feature Selection**
   - Remove invalid or non-positive prices.
   - Select relevant predictors such as neighbourhood group, neighbourhood, room type, latitude, longitude, minimum nights, reviews, host activity, and availability.
   - Prepare the dataset for supervised regression modeling.

4. **Preprocessing Pipeline**
   - Separate numerical and categorical features.
   - Apply median imputation for numerical variables.
   - Apply most-frequent imputation for categorical variables.
   - Standardize numerical features and one-hot encode categorical features.
   - Combine the transformations using `ColumnTransformer` and `Pipeline`.

5. **Regression Modeling**
   - Train and compare multiple regression models:
     - Linear Regression
     - Random Forest Regressor
     - Gradient Boosting Regressor
   - Evaluate performance using MAE, RMSE, and R² score.

6. **Hyperparameter Tuning**
   - Apply `GridSearchCV` with cross-validation to optimize the Gradient Boosting model.
   - Tune parameters such as `n_estimators`, `learning_rate`, and `max_depth`.
   - Select the best-performing model based on validation performance.

7. **Model Diagnostics**
   - Compare training and testing performance to analyze generalization.
   - Examine actual vs predicted plots, residual plots, and error distribution.
   - Assess whether the model is underfitting or overfitting.

8. **Model Saving and Deployment**
   - Save the final optimized pipeline using `joblib`.
   - Integrate the model into a Streamlit app for interactive price prediction.

## Modeling Approach
The prediction task is formulated as a supervised regression problem, where the target variable is the nightly Airbnb price.

The final model is a tuned Gradient Boosting Regressor, chosen after comparing multiple regression algorithms and improving performance through cross-validated hyperparameter optimization.

## Key Insights
- Listing location is one of the strongest determinants of Airbnb price.
- Room type significantly influences pricing, with entire homes generally commanding higher rates.
- Geographic coordinates and neighbourhood characteristics help explain local price variation.
- Review-related variables, availability, and host activity also contribute to price differences.
- A well-constructed preprocessing pipeline is essential for handling mixed data types and improving model performance.

## How to Run
### 1. Install dependencies
From the project root, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 2. Open the notebook
To reproduce the analysis and modeling workflow:

```bash
jupyter notebook 202618052_Lab_4/202618052_Lab_4.ipynb
```

### 3. Run the Streamlit app
To launch the interactive Airbnb price predictor:

```bash
cd 202618052_Lab_4
streamlit run app.py
```

Then enter the listing details in the web interface and the model will generate an estimated nightly price.

## Expected Workflow
1. Load the dataset.
2. Clean and analyze data quality.
3. Engineer and select useful features.
4. Train multiple regression models.
5. Tune the best-performing model.
6. Save the trained pipeline.
7. Use the Streamlit app for real-time prediction.

## Conclusion
This lab demonstrates a complete machine learning workflow for real estate-style price prediction. It covers data analysis, preprocessing, regression modeling, tuning, and deployment in a practical business context. The final system provides a useful tool for estimating Airbnb listing prices based on user-supplied listing attributes.

## Author
Lakshita Pagaria  
Registration Number: 202618052
