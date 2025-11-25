import os
import sys
# ajouter la racine du projet au PYTHONPATH afin que 'src' soit importable
ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, ROOT)

import pandas as pd
import numpy as np
from src.feature_engineering import feature_engineering
from sklearn.preprocessing import LabelEncoder

RAW = os.path.join(ROOT, "data", "raw")
OUT = os.path.join(ROOT, "data", "processed")
os.makedirs(OUT, exist_ok=True)

def process_file(fname_in, fname_out):
    p_in = os.path.join(RAW, fname_in)
    p_out = os.path.join(OUT, fname_out)
    if not os.path.exists(p_in):
        raise FileNotFoundError(f"{p_in} not found")
    df = pd.read_csv(p_in)
    df_proc = feature_engineering(df)
    df_proc.to_csv(p_out, index=False)
    print("Wrote:", p_out)

def create_temporal_features(df):
    df['hour_of_day'] = (df['step'] - 1) % 24
    df['day_of_week'] = ((df['step'] - 1) // 24) % 7
    df['week_number'] = (df['step'] - 1) // (24 * 7)
    df['is_night'] = df['hour_of_day'].between(22, 6).astype(int)
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    df['is_business_hours'] = df['hour_of_day'].between(8, 17).astype(int)
    return df

def create_amount_features(df):
    df['amount_log'] = np.log1p(df['amount'])
    df['amount_sqrt'] = np.sqrt(df['amount'])
    Q95 = df['amount'].quantile(0.95)
    Q99 = df['amount'].quantile(0.99)
    df['is_high_amount'] = (df['amount'] > Q95).astype(int)
    df['is_very_high'] = (df['amount'] > Q99).astype(int)
    df['is_round_amount'] = (df['amount'] % 1000 == 0).astype(int)
    return df

def create_age_features(df):
    df['is_senior'] = (df['age'] >= 60).astype(int)
    df['is_young'] = (df['age'] <= 25).astype(int)
    df['age_group'] = pd.cut(df['age'], bins=[0, 25, 40, 60, 100], labels=['young', 'adult', 'senior', 'elderly'])
    return df

def encode_categorical_features(df):
    le = LabelEncoder()
    df['type_encoded'] = le.fit_transform(df['type'])
    return df

def create_interaction_features(df):
    df['amount_per_age'] = df['amount'] / (df['age'] + 1)
    df['night_high_amount'] = df['is_night'] * df['is_high_amount']
    df['weekend_senior'] = df['is_weekend'] * df['is_senior']
    df['night_senior'] = df['is_night'] * df['is_senior']
    return df

def create_features(df):
    df = create_temporal_features(df)
    df = create_amount_features(df)
    df = create_age_features(df)
    df = encode_categorical_features(df)
    df = create_interaction_features(df)
    # Nettoyage final
    df = df.drop(columns=['transaction_id', 'customer_id', 'type'], errors='ignore')
    return df

if __name__ == "__main__":
    try:
        process_file("train.csv", "train_engineered.csv")
        process_file("test.csv", "test_engineered.csv")
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
    print("Processing complete.")