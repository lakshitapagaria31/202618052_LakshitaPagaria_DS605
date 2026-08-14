

# Lab 2: Vectorized Programming with NumPy and Data Wrangling (Titanic)

## Overview
This assignment demonstrates vectorized NumPy programming and Pandas-based data wrangling using the Kaggle Titanic dataset (Part B). The notebook implements array operations and linear algebra tasks in Part A, and comprehensive EDA, preprocessing, aggregation, and visualization in Part B to support analysis and model-ready preprocessing.

## Project Structure
- `202618052_Lab_2.ipynb`: Jupyter notebook containing the complete implementation for this assignment, including code, figures, and short commentary.
- `Readme.md`: This file (assignment description, dataset info, instructions, and observations).
- `requirements.txt`: Python package list for reproducibility (install with `pip install -r requirements.txt`).
- `train.csv` (not tracked in this public repository): place a local copy in `202618052_Lab_2/` before running the notebook.

## Dataset

- **Title:** Titanic: Machine Learning from Disaster (Part B)
- **Source & Link:** Kaggle — https://www.kaggle.com/competitions/titanic/data
- **Notes:** Download `train.csv` and `test.csv` from the Kaggle page and place them in the `202618052_Lab_2/` directory before executing the notebook. The dataset is not tracked in this public repository to avoid sharing data files.

## Key Components

1. **NumPy — Vectorized Programming (Part A)**
	- Generate Array A (100 random integers with fixed seed) and compute descriptive statistics (min, max, median, mean, std).
	- Create Array B using `np.arange()` and demonstrate `np.zeros()`, `np.ones()`, and `np.linspace()` with shapes and dtypes.
	- Construct 2D and 3D arrays, demonstrate indexing, slicing, reshaping and flattening.
	- Perform vectorized arithmetic and linear algebra operations: matrix addition, element-wise multiplication, matrix multiplication, transpose, determinant, inverse (with verification via `np.allclose`).
	- Sample ≥1,000 values from a normal distribution (noted mean and std) and plot a histogram; compare sample statistics with chosen parameters.

2. **Pandas — Titanic Data Wrangling (Part B)**
	- Load `train.csv` and perform initial inspection using `head()`, `tail()`, `shape`, `columns`, `info()`, and `describe()`.
	- Demonstrate `loc` and `iloc` usage with examples and explanation of differences.
	- Filtering and querying using Boolean indexing and `query()` to answer assignment questions (male >50, female 1st-class survival rate, age 20–40 & fare > median & survived, travelling alone & age <30 & did not survive, embarked='S' & Pclass 2/3 & fare above Southampton median).
	- Aggregation with `groupby()` and `agg()` to compute survival rates by `Sex`, by `Pclass`, average Age/Fare by `Pclass`, and combined Sex–Pclass aggregates.
	- Missing values analysis: count and percentage per column, imputation strategies for `Age` (mean/median/mode/random), and visualization of missing-value counts.
	- Fare outlier detection using IQR method: compute Q1/Q3/IQR and 1.5×IQR bounds and count outliers.
	- Feature engineering: `FamilySize`, `IsAlone`, and pivot table (rows=Sex, columns=Pclass, values=mean Survived) to identify highest and lowest groups.
	- Visualizations: correlation heatmap, survival rate by sex, Age vs Fare scatter colored by survival, and supporting plots for other tasks.

3. **Observations & Insights**
	- Female passengers show higher survival rates than male passengers.
	- First-class passengers have substantially higher survival probabilities.
	- Age and Fare are associated with survival; Fare is correlated with class and serves as a proxy for socioeconomic status.
	- Traveling alone correlates with lower survival rates compared to passengers with small family groups.
	- Missing `Cabin` values are pervasive; treating cabin as a missing-indicator or collapsing into deck levels is recommended for feature engineering.

## How to run
1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Download `train.csv` and `test.csv` from the Kaggle competition page and place them in `202618052_Lab_2/`.

3. Open and run the notebook:

```bash
jupyter notebook 202618052_Lab_2/202618052_Lab_2.ipynb
```

Run cells in order; the notebook contains fixed random seeds and reproducible preprocessing steps.

## Conclusion
This lab reinforces best practices for vectorized numerical programming and for preprocessing real-world tabular data with Pandas. The notebook demonstrates data cleaning, feature creation, aggregation, and visualization techniques that prepare data for downstream modeling and provide interpretable insights about survival predictors in the Titanic dataset.


