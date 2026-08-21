# Lab 3: Hotel Booking Demand Analysis

## Overview
This assignment applies data cleaning, exploratory data analysis, and machine learning techniques to the Hotel Booking Demand dataset. The project examines booking behavior, identifies patterns in room demand, and investigates the key drivers behind cancellations and reservation outcomes in the hospitality industry.

## Project Structure
- `202618052_Lab_3.ipynb`: Jupyter notebook containing the complete implementation of the assignment, including data exploration, preprocessing, visualization, and modeling.
- `hotel_bookings.csv`: The dataset used for analysis and prediction.
- `Readme.md`: This file, which summarizes the objective, workflow, and key findings.

## Dataset
- **Title:** Hotel Booking Demand
- **Source & Link:** Kaggle — https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand
- **Notes:** The dataset contains booking records for city and resort hotels, including guest, reservation, and cancellation-related attributes.

## Key Components

1. **Data Acquisition and Initial Exploration**
   - Load the hotel booking dataset and inspect its structure.
   - Check the number of rows and columns, data types, and missing values.
   - Review summary statistics to understand booking distributions.

2. **Data Cleaning and Preprocessing**
   - Handle missing values in categorical and numerical fields.
   - Clean inconsistent entries and normalize data types.
   - Prepare the dataset for modeling by addressing invalid or noisy values.

3. **Exploratory Data Analysis (EDA)**
   - Analyze booking trends by hotel type, market segment, and customer profile.
   - Examine cancellation patterns and their relationship with lead time, stay duration, and guest attributes.
   - Use visualizations such as bar charts, histograms, heatmaps, and boxplots to interpret patterns.

4. **Feature Engineering**
   - Derive meaningful variables such as total guests, length of stay, and other booking characteristics.
   - Transform categorical variables into model-ready formats.
   - Prepare features that capture useful business insights for prediction.

5. **Predictive Modeling**
   - Train machine learning models to predict booking-related outcomes.
   - Evaluate different algorithms using appropriate classification metrics.
   - Compare model performance and identify the most effective approach.

6. **Evaluation and Interpretation**
   - Measure accuracy, precision, recall, F1-score, and other relevant metrics.
   - Interpret the importance of major features and discuss their impact on booking decisions.
   - Summarize practical implications for hotel operations and demand forecasting.

## Insights and Observations
- Hotel demand varies significantly across hotel type, market segment, and booking channel.
- Lead time, deposit status, and market segment are important factors in influencing bookings and cancellations.
- Customer behavior differs between resort and city hotel guests.
- Cancellation risk is often associated with booking characteristics, customer patterns, and reservation timing.
- Data-driven analysis can help hotels improve occupancy planning, pricing strategy, and service management.

## How to Run
1. Install the required Python packages:

```bash
pip install -r requirements.txt
```

2. Open the notebook:

```bash
jupyter notebook 202618052_Lab_3/202618052_Lab_3.ipynb
```

3. Run all cells in order to reproduce the analysis and predictive modeling workflow.

## Conclusion
This lab demonstrates a complete data science workflow for hotel booking demand analysis. From initial data inspection to predictive modeling and evaluation, the project highlights the value of exploratory analysis and machine learning in understanding reservation patterns and supporting operational decisions in the hospitality sector.

## Author
Lakshita Pagaria
Registration Number: 202618052
