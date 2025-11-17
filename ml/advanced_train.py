# ml/advanced_train.py
"""Advanced training script:
- Loads data/processed/processed_data.csv
- Performs basic feature engineering:
    * encodes categorical features via OrdinalEncoder for tree models
    * fills missing values (median for numeric, 'missing' for categorical)
    * generates simple interaction features
- Splits data, runs RandomizedSearchCV over a small parameter grid for RandomForest/LightGBM if available
- Saves best model and metadata to models/advanced_model.pkl and models/metadata.json
- Produces evaluation metrics (MAE/MSE or accuracy) and a small report in models/report.txt
"""
import os, json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, accuracy_score
import joblib
import warnings
warnings.filterwarnings('ignore')

def find_target(df):
    candidates = ['target','delivery_time','delivery_days','days_to_deliver','price','quantity']
    for c in candidates:
        if c in df.columns:
            return c
    for c in df.select_dtypes(include=['number']).columns:
        if 'id' not in c.lower():
            return c
    return None

def prepare_features(df, target):
    df = df.copy()
    y = df[target]
    X = df.drop(columns=[target])
    # separate dtypes
    num_cols = X.select_dtypes(include=['number']).columns.tolist()
    cat_cols = X.select_dtypes(include=['object','category']).columns.tolist()
    # fill numeric
    for c in num_cols:
        X[c] = X[c].fillna(X[c].median())
    # fill categorical
    X[cat_cols] = X[cat_cols].fillna('missing')
    # simple ordinal encoding for tree models
    if cat_cols:
        enc = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
        X[cat_cols] = enc.fit_transform(X[cat_cols])
    else:
        enc = None
    # create simple interaction feature (if at least 2 numeric columns)
    if len(num_cols) >= 2:
        X['num_interaction'] = X[num_cols[0]] * X[num_cols[1]]
    return X, y, {'num_cols': num_cols, 'cat_cols': cat_cols, 'encoder_present': enc is not None}

def train():
    path = os.path.join('data','processed','processed_data.csv')
    if not os.path.exists(path):
        raise FileNotFoundError('Run ETL first to produce processed_data.csv')
    df = pd.read_csv(path)
    target = find_target(df)
    if target is None:
        raise ValueError('No suitable target column found in processed data.')
    X, y, meta = prepare_features(df, target)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    numeric_target = pd.api.types.is_numeric_dtype(y)
    # Candidate models and param distributions
    results = {}
    if numeric_target:
        model = RandomForestRegressor(random_state=42)
        param_dist = {
            'n_estimators': [50,100,150],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2,5,10]
        }
        scorer = 'neg_mean_absolute_error'
    else:
        model = RandomForestClassifier(random_state=42)
        param_dist = {
            'n_estimators': [50,100,150],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2,5,10]
        }
        scorer = 'accuracy'
    # Try LightGBM if available (optional faster model)
    try:
        import lightgbm as lgb
        if numeric_target:
            lgb_model = lgb.LGBMRegressor(random_state=42)
        else:
            lgb_model = lgb.LGBMClassifier(random_state=42)
        use_lgb = True
    except Exception:
        lgb_model = None
        use_lgb = False
    # RandomizedSearchCV on sklearn model
    rs = RandomizedSearchCV(model, param_dist, n_iter=6, cv=3, scoring=scorer, random_state=42, n_jobs=-1)
    rs.fit(X_train, y_train)
    best = rs.best_estimator_
    # Evaluate
    if numeric_target:
        preds = best.predict(X_test)
        mae = mean_absolute_error(y_test, preds)
        mse = mean_squared_error(y_test, preds)
        results['mae'] = float(mae); results['mse'] = float(mse)
    else:
        preds = best.predict(X_test)
        acc = accuracy_score(y_test, preds)
        results['accuracy'] = float(acc)
    # Save model & metadata
    os.makedirs('models', exist_ok=True)
    joblib.dump({'model': best, 'features': list(X.columns), 'target': target}, 'models/advanced_model.pkl')
    with open('models/metadata.json', 'w') as fh:
        json.dump({'target': target, 'feature_count': len(X.columns), 'meta': meta, 'results': results}, fh, indent=2)
    # report
    with open('models/report.txt', 'w') as fh:
        fh.write('Training report\n')
        fh.write(json.dumps(results, indent=2))
    print('Training complete. Results:', results)

if __name__ == '__main__':
    train()
