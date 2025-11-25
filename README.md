# Fraud Detection Project

This project aims to detect fraudulent transactions using machine learning techniques. The dataset consists of transaction records, with a focus on identifying fraudulent activities.

## Project Structure

- **data/**: Contains the datasets used in the project.
  - **raw/**: Original datasets (do not modify).
    - `train.csv`: Training dataset with the target variable `is_fraud`.
    - `test.csv`: Test dataset without the target variable.
  - **processed/**: Processed datasets with engineered features.
    - `train_engineered.csv`: Processed training dataset.
    - `test_engineered.csv`: Processed test dataset.

- **notebooks/**: Jupyter notebooks for development and analysis.
  - `01_EDA.ipynb`: Exploratory Data Analysis.
  - `02_Feature_Engineering.ipynb`: Feature engineering techniques.
  - `03_Baseline_Logistic.ipynb`: Baseline logistic regression model.
  - `04_Advanced_Models.ipynb`: Advanced machine learning models.
  - `05_Final_Submission.ipynb`: Main notebook for finalizing the submission.

- **src/**: Reusable Python code.
  - `__init__.py`: Marks the directory as a Python package.
  - `data_preprocessing.py`: Functions for data cleaning and handling missing values.
  - `feature_engineering.py`: Functions for creating new features.
  - `models.py`: Definitions of machine learning models.
  - `evaluation.py`: Functions for calculating evaluation metrics.

- **models/**: Saved machine learning models.
  - `baseline_logistic.pkl`: Trained baseline logistic regression model.
  - `random_forest.pkl`: Trained random forest model.
  - `xgboost_final.pkl`: Best-performing XGBoost model.

- **visualizations/**: Saved visualizations.
  - `fraud_distribution.png`: Visualization of fraud distribution.
  - `confusion_matrix.png`: Visualization of the confusion matrix.
  - `feature_importance.png`: Visualization of feature importance.

- **submission.csv**: Main deliverable file for the project.

- **requirements.txt**: Lists the Python dependencies required for the project.

- **.gitignore**: Specifies files and directories to be ignored by version control.

- **presentation_video.mp4**: Contains a 3-5 minute presentation video or a link to it.

## Installation

To install the required dependencies, run:

```
python -m venv .venv
# mac/linux
source .venv/bin/activate
# windows (PowerShell)
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

## Usage

1. Load the datasets from the `data/raw/` directory.
2. Perform exploratory data analysis using the notebooks in the `notebooks/` directory.
3. Preprocess the data and engineer features as needed.
4. Train and evaluate models using the provided scripts in the `src/` directory.
5. Generate visualizations to understand model performance.
6. Finalize the submission in `submission.csv`.

## License

This project is licensed under the MIT License.