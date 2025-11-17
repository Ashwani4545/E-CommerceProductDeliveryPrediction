"""etl/load.py - save processed data"""
import os
import pandas as pd

PROCESSED_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')
os.makedirs(PROCESSED_DIR, exist_ok=True)

def load_to_csv(df: pd.DataFrame, filename: str = 'processed_data.csv') -> str:
    path = os.path.join(PROCESSED_DIR, filename)
    df.to_csv(path, index=False)
    return path

if __name__ == '__main__':
    import pandas as pd
    df = pd.DataFrame({'x':[1,2,3]})
    print('Saved to', load_to_csv(df, 'sample.csv'))
