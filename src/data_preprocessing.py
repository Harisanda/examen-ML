import pandas as pd

def load_data(file_path):
    """Load dataset from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean the dataset by handling missing values and duplicates."""
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Fill missing values (example: fill with mean for numerical columns)
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        df[column].fillna(df[column].mean(), inplace=True)
    
    # Drop rows with missing target variable
    if 'is_fraud' in df.columns:
        df = df.dropna(subset=['is_fraud'])
    
    return df

def preprocess_data(train_file, test_file):
    """Load and preprocess the training and test datasets."""
    train_data = load_data(train_file)
    test_data = load_data(test_file)
    
    train_data = clean_data(train_data)
    test_data = clean_data(test_data)
    
    return train_data, test_data