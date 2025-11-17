# ml/predict.py
import pandas as pd, joblib, os, argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', default='predictions.csv')
    args = p.parse_args()
    mfile = os.path.join('models','model.pkl')
    if not os.path.exists(mfile):
        raise FileNotFoundError('Model not found. Train model first with ml/train_model.py')
    store = joblib.load(mfile)
    model = store['model']
    features = store['features']
    df = pd.read_csv(args.input)
    X = df[features].select_dtypes(include=['number']).fillna(0)
    preds = model.predict(X)
    df['prediction'] = preds
    df.to_csv(args.output, index=False)
    print('Wrote predictions to', args.output)

if __name__ == '__main__':
    main()
