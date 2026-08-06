# Lab 1: Book Data Scraping and Analysis

## Overview
This assignment demonstrates the complete process of collecting, cleaning, analyzing, and interpreting book data. The project uses a Scrapy spider to scrape raw book details from the target website, followed by data preprocessing, feature engineering, visualization, and insight generation.

## Project Structure
- `202618052_Lab_1.ipynb`: A Jupyter notebook containing the full workflow for the assignment, including data loading, cleaning, feature creation, plotting, and interpretation.
- `data/raw_books.csv`: Raw dataset exported from the Scrapy spider before preprocessing.
- `data/cleaned_books.csv`: Cleaned dataset produced after preprocessing and deduplication.
- `plots/`: Folder containing visual outputs generated during analysis.
- `ds605_lab1/`: Scrapy project folder, including spider and project configuration files.

## Key Components
1. **Data Collection**
   - A Scrapy spider follows pagination and visits each individual book page.
   - Extracted fields include title, category, price, rating, availability, description, UPC, and review count.
   - The scraping output is saved as `data/raw_books.csv`.

2. **Data Preprocessing**
   - Text fields are cleaned to remove extra spaces.
   - Price values are converted from strings to numeric format.
   - Star ratings are mapped from text labels to integer values.
   - Stock availability is parsed to extract numeric count.
   - Missing descriptions are replaced with a placeholder.
   - Duplicate records are removed based on UPC.

3. **Feature Engineering**
   - `description_word_count`: number of words in each book description.
   - `price_band`: low, medium, or high price categories based on quantiles.
   - `affordability_score`: normalized score indicating relative affordability.
   - `value_score`: ratio of rating to price to assess value.
   - `recommended`: boolean flag for highly rated books priced at or below the median.

4. **Visualization and Analysis**
   - Price distribution histogram.
   - Rating distribution count plot.
   - Average price by top categories.
   - Price vs rating relationship boxplot.
   - Category vs stock distribution boxplot.
   - Word cloud generated from book descriptions.

5. **Insights and Interpretation**
   - Observations about pricing patterns, rating distribution, category behavior, and book value.
   - Discussion of data limitations, including missing descriptions and single-source scraping.

## Conclusion
This lab delivers a structured approach to scraping and analyzing book metadata. It highlights the importance of data cleaning, feature selection, and visual analysis to derive meaningful business insights from raw scraped data.
