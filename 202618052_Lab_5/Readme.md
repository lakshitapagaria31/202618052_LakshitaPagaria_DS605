# Lab 5: Machine Learning with Scikit-learn and From Scratch

## Overview
This assignment applies supervised machine learning to the UCI Garment Worker Productivity dataset. The notebook develops regression and binary classification models using Scikit-learn, then recreates the main algorithms and evaluation metrics using NumPy and Pandas.

The workflow covers data inspection, feature engineering, preprocessing, model training, evaluation, comparison, and optimization using a fixed train/test split.

## Project Structure
- `202618052_Lab_5.ipynb`: Jupyter notebook containing the complete implementation, analysis, model comparisons, and convergence plots.
- `garments_worker_productivity.csv`: Dataset containing garment production and worker productivity observations.
- `Readme.md`: This file, which summarizes the objective, workflow, dataset, and instructions.

## Dataset
- **Title:** Productivity Prediction of Garment Employees
- **Source:** UCI Machine Learning Repository
- **Notes:** The dataset includes production targets, actual productivity, working time, incentives, idle time, worker counts, departments, teams, quarters, and date information.

Two learning tasks are defined:

- **Regression target:** `actual_productivity`
- **Classification target:** `MeetsTarget`, equal to `1` when `actual_productivity >= targeted_productivity` and `0` otherwise

The `actual_productivity` column is excluded from classification features because it is used to create `MeetsTarget`. This prevents target leakage.

## Key Components

1. **Data Inspection and Cleaning**
	- Load the dataset and inspect its shape, columns, data types, descriptive statistics, missing values, and duplicate rows.
	- Remove an automatically generated index column when present.

2. **Feature Engineering and Selection**
	- Convert the date column to datetime format.
	- Extract month, day of month, and day of week features.
	- Select numerical and categorical features explicitly for both learning tasks.

3. **Reproducible Data Splitting**
	- Create one fixed train/test split using random state `42` and a test size of `20%`.
	- Reuse the same indices for all model implementations.

4. **Scikit-learn Modeling**
	- Build preprocessing pipelines using median numerical imputation, standardization, categorical mode imputation, and one-hot encoding.
	- Train `LinearRegression` for productivity prediction.
	- Train `LogisticRegression` for target achievement classification.

5. **From-scratch Regression**
	- Implement numerical and categorical preprocessing with Pandas and NumPy.
	- Implement Linear Regression using the normal equation and a NumPy pseudo-inverse.
	- Calculate MAE, RMSE, and R2 manually.

6. **From-scratch Classification**
	- Implement the sigmoid function and binary cross-entropy loss.
	- Train Logistic Regression using vectorized gradient descent.
	- Calculate accuracy, precision, recall, and F1 score manually.

7. **Optimization and Comparison**
	- Improve the manual classifier using a tuned learning rate, L2 regularization, and early stopping.
	- Compare Scikit-learn, baseline manual, and optimized manual implementations using model performance and execution time.
	- Visualize baseline and optimized training-loss convergence.

## Evaluation

Regression models are evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R2 score
- Training time
- Prediction time

Classification models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 score
- Training time
- Prediction time

The notebook also measures the difference between regression predictions and the agreement between classification predictions produced by the two implementations.

## How to Run

1. Install the required Python packages from the project root:

```bash
pip install -r requirements.txt
```

2. Open the notebook:

```bash
jupyter notebook 202618052_Lab_5/202618052_Lab_5.ipynb
```

3. Run all cells in order. The notebook expects `garments_worker_productivity.csv` to be in the same folder as the notebook.

The notebook can also be opened and executed in VS Code with the Python and Jupyter extensions installed.

## Conclusion
This lab demonstrates a complete machine learning workflow for garment worker productivity analysis. It compares library-based and from-scratch implementations of Linear Regression and Logistic Regression, while showing how preprocessing, evaluation, optimization, and reproducibility affect model development.

## Author
Lakshita Pagaria  
Registration Number: 202618052
