import os
import sys
import pandas as pd
import joblib

ROOT = os.path.dirname(os.path.dirname(__file__))
P = os.path.join(ROOT, "data", "processed", "test_engineered.csv")
MODEL_PATHS = [
    os.path.join(ROOT, "models", "xgboost_final.pkl"),
    os.path.join(ROOT, "models", "random_forest.pkl"),
    os.path.join(ROOT, "models", "baseline_logistic.pkl"),
]

if not os.path.exists(P):
    print("Processed test file not found:", P); sys.exit(1)

df_test = pd.read_csv(P)
# choose model available
model = None
for m in MODEL_PATHS:
    if os.path.exists(m):
        model = joblib.load(m)
        print("Loaded model:", m)
        break
if model is None:
    print("No model found in models/*.pkl"); sys.exit(1)

# attempt prediction
X = df_test.copy()
# remove id if present
ids = X['id'] if 'id' in X.columns else pd.Series(range(1, len(X)+1), name='id')
if 'id' in X.columns: X = X.drop(columns=['id'])
# if target present, drop
if 'is_fraud' in X.columns: X = X.drop(columns=['is_fraud'])

# predict (handle classifiers with predict_proba or predict)
try:
    if hasattr(model, "predict_proba"):
        preds = model.predict_proba(X)[:, 1]
        preds = (preds >= 0.5).astype(int)
    else:
        preds = model.predict(X)
except Exception as e:
    print("Prediction failed:", e); sys.exit(1)

sub = pd.DataFrame({"id": ids, "is_fraud": preds})
outp = os.path.join(ROOT, "submission.csv")
sub.to_csv(outp, index=False)
print("Wrote submission:", outp)