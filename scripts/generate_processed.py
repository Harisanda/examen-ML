import os
import sys
# ajouter la racine du projet au PYTHONPATH afin que 'src' soit importable
ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, ROOT)

import pandas as pd
from src.feature_engineering import feature_engineering

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

if __name__ == "__main__":
    try:
        process_file("train.csv", "train_engineered.csv")
        process_file("test.csv", "test_engineered.csv")
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
    print("Processing complete.")