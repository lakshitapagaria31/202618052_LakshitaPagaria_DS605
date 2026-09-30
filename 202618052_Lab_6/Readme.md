# Lab 6: Image Feature Extraction and Text Vectorization

## Overview

This assignment studies how the choice of data representation affects traditional machine-learning models. It contains two complementary notebooks:

- **Part A:** Extract hand-crafted features from asphalt images and classify them as crack or non-crack.
- **Part B:** Convert email text into numerical representations and classify messages as spam or ham.
- **Part C:** Improve both representations and compare the effect on model performance, dimensionality, and computation time.

Deep-learning models, CNNs, and pretrained embeddings are intentionally excluded. Image features are calculated from raw pixels with NumPy and OpenCV, while text features are generated with scikit-learn vectorizers.

## Project Structure

- `202618052_Lab_6_Image_Feature_Extraction_and_Classification.ipynb`: Image preprocessing, feature extraction, classification, evaluation, and representation improvement.
- `202618052_Lab_6_Text_Vectorization_and_Spam_Classification.ipynb`: Text cleaning, CountVectorizer representations, spam classification, evaluation, and representation improvement.
- `data/`: Local input datasets. This directory is ignored by Git and must be supplied locally before running the notebooks.
- `results/`: Generated CSV summaries and figures. This directory is also ignored by Git.
- `Readme.md`: Documentation for this lab.

## Dataset Requirements

The datasets are intentionally not stored in the GitHub repository. Place them in the following local structure:

```text
data/
├── asphalt_images/
│   ├── Cracks/
│   │   └── *.jpg
│   └── NonCracks/
│       └── *.jpg
└── emails.csv
```

### Asphalt image dataset

The image notebook expects labelled asphalt images in class-specific folders. Folder or file names should contain terms such as `crack`, `non-crack`, `no-crack`, `negative`, or `intact` so that labels can be inferred automatically. If different names are used, update the `infer_label` function in the notebook.

The default experiment uses 400 images, resizes them to `256 x 256`, and converts them to grayscale.

### Email dataset

The text notebook supports two CSV formats:

1. A raw-text file with an email/message column and a binary label column.
2. A word-count file with one numeric column per vocabulary word and a `Prediction` label column.

For the word-count format, each email is reconstructed as a bag-of-words document. Since word order is unavailable, the notebook uses unigrams rather than bigrams for this format.

## Key Components

### Part A: Image classification

1. Inspect image dimensions, channels, and data types.
2. Resize images to a common resolution and convert them to grayscale.
3. Extract intensity statistics, percentiles, skewness, kurtosis, entropy, and contrast measures.
4. Detect edges with the OpenCV Canny operator and calculate edge count and density.
5. Compare traditional classifiers:
   - Logistic Regression
   - RBF Support Vector Machine
   - k-Nearest Neighbours
   - Random Forest
   - Gradient Boosting
6. Evaluate accuracy, precision, recall, F1 score, confusion matrices, cross-validated F1, training time, and prediction time.
7. Compare the baseline feature representation with an improved representation that adds HOG-style gradient features and tuned edge features.

Recall is especially important for crack detection because a missed crack may represent a maintenance or safety risk.

### Part B: Text classification

1. Detect the input format and inspect class balance.
2. Clean text by lowercasing, removing subject prefixes, HTML, URLs, email addresses, non-alphabetic characters, and excess whitespace.
3. Remove empty and duplicate messages to reduce data leakage.
4. Fit `CountVectorizer` on training data only.
5. Compare:
   - Multinomial Naive Bayes
   - Logistic Regression
   - Linear SVM
6. Evaluate accuracy, precision, recall, F1 score, sparsity, feature count, vectorization time, training time, prediction time, and confusion matrices.
7. Improve the representation with stop-word removal, n-grams where available, `min_df`, and a vocabulary limit.

For spam filtering, precision is important because false positives can hide legitimate email, while recall is important because false negatives allow spam into the inbox.

## Evaluation and Reproducibility

Both notebooks use a fixed random state of `42` and a test size of `20%`. The vectorizer and feature scaling steps are fitted on training data only to avoid test-set leakage.

The notebooks report:

- Accuracy
- Precision
- Recall
- F1 score
- Confusion matrices
- Feature count and representation sparsity where applicable
- Training and prediction time
- Cross-validation results for the image workflow

The generated result files are written to `results/`, including model-comparison tables and figures such as class distributions, sample images, representation comparisons, and confusion matrices.

## How to Run

### 1. Install dependencies

From the repository root:

```bash
pip install -r requirements.txt
```

A Python virtual environment is recommended.

### 2. Add the local datasets

Create the `data/` structure shown above and copy the asphalt images and `emails.csv` into the appropriate locations.

### 3. Open the notebooks

From the repository root:

```bash
jupyter notebook 202618052_Lab_6/202618052_Lab_6_Image_Feature_Extraction_and_Classification.ipynb
jupyter notebook 202618052_Lab_6/202618052_Lab_6_Text_Vectorization_and_Spam_Classification.ipynb
```

Alternatively, open either notebook in VS Code with the Python and Jupyter extensions installed. Run the cells in order.

### 4. Optional path configuration

The notebooks support environment variables when the datasets or output directory are stored elsewhere:

```bash
IMAGE_DIR=path/to/asphalt_images TEXT_CSV=path/to/emails.csv OUT_DIR=path/to/results
```

On Windows PowerShell, set them with:

```powershell
$env:IMAGE_DIR = "path\to\asphalt_images"
$env:TEXT_CSV = "path\to\emails.csv"
$env:OUT_DIR = "path\to\results"
```

## Limitations

- The image experiment uses a relatively small dataset, so a single train-test split can be sensitive to the random partition.
- Hand-crafted image features may not capture all crack shapes, lighting conditions, or surface textures.
- The word-count email format does not preserve word order, which prevents meaningful bigram extraction.
- Duplicate removal, one source dataset, and a single split may limit generalisation to new images or email sources.
- Traditional models are useful and interpretable baselines, but they may underperform modern deep-learning approaches on larger datasets.

## Conclusion

Lab 6 demonstrates that representation design is central to machine learning. Carefully selected image statistics, edge features, text cleaning, vocabulary choices, and n-grams can affect model quality as much as the classifier itself. The notebooks provide a reproducible comparison of these choices using traditional, non-deep-learning methods.

## Author

Lakshita Pagaria  
Registration Number: 202618052
