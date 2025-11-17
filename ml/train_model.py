# ml/train_model.py
import os, pandas as pd, joblib

def find_target(df):
    candidates = ['target','delivery_time','delivery_days','days_to_deliver','price','quantity']
    for c in candidates:
        if c in df.columns:
            return c
    for c in df.select_dtypes(include=['number']).columns:
        if 'id' not in c.lower():
            return c
    return None

def train():
    path = os.path.join('data','processed','processed_data.csv')
    if not os.path.exists(path):
        raise FileNotFoundError('Run ETL first to produce processed_data.csv')
    df = pd.read_csv(path)
    target = find_target(df)
    if target is None:
        raise ValueError('No suitable target column found in processed data.')
    X = df.drop(columns=[target])
    X = X.select_dtypes(include=['number']).fillna(0)
    y = df[target]
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    numeric_target = pd.api.types.is_numeric_dtype(y)
    if numeric_target:
        from sklearn.ensemble import RandomForestRegressor as Model
    else:
        from sklearn.ensemble import RandomForestClassifier as Model
    model = Model(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    if numeric_target:
        from sklearn.metrics import mean_squared_error
        preds = model.predict(X_test)
        print('MSE:', mean_squared_error(y_test, preds))
    else:
        from sklearn.metrics import accuracy_score
        preds = model.predict(X_test)
        print('Accuracy:', accuracy_score(y_test, preds))
    os.makedirs('models', exist_ok=True)
    joblib.dump({'model': model, 'features': list(X.columns), 'target': target}, 'models/model.pkl')
    print('Saved model to models/model.pkl')

if __name__ == '__main__':
    train()
