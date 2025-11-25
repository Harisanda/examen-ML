import pandas as pd
import numpy as np

def create_features(df):
    # safe example: create new_feature only si colonnes présentes
    if {'feature1', 'feature2'}.issubset(df.columns):
        df['new_feature'] = df['feature1'].fillna(0) * df['feature2'].fillna(0)
    else:
        # crée une colonne neutre si les colonnes attendues n'existent pas
        df['new_feature'] = 0
    return df

def encode_categorical_features(df):
    # encode seulement si la colonne existe
    cat_cols = [c for c in ['categorical_feature'] if c in df.columns]
    if len(cat_cols) > 0:
        df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
    return df

def scale_features(df):
    from sklearn.preprocessing import StandardScaler
    # choisir colonnes numériques excluant identifiants
    numerical_features = df.select_dtypes(include=['number']).columns.tolist()
    numerical_features = [c for c in numerical_features if c not in ('id', 'transaction_id', 'is_fraud')]
    if len(numerical_features) == 0:
        return df
    scaler = StandardScaler()
    df[numerical_features] = scaler.fit_transform(df[numerical_features].astype(float))
    return df

def feature_engineering(df):
    df = create_features(df)
    df = encode_categorical_features(df)
    df = scale_features(df)
    return df

if __name__ == "__main__":
    # petit test si exécuté en ligne de commande
    import sys, os
    path = sys.argv[1] if len(sys.argv) > 1 else None
    if path and os.path.exists(path):
        df = pd.read_csv(path)
        df2 = feature_engineering(df)
        print("feature_engineering: input rows:", len(df), "-> output cols:", df2.shape[1])
    else:
        print("Usage: python src/feature_engineering.py path/to/file.csv")