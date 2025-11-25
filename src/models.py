from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

def get_logistic_regression_model():
    model = LogisticRegression(max_iter=1000)
    return model

def get_random_forest_model(n_estimators=100, max_depth=None):
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    return model

def get_xgboost_model(learning_rate=0.1, n_estimators=100, max_depth=3):
    model = XGBClassifier(learning_rate=learning_rate, n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    return model