"""etl/extract.py - read CSVs from data/raw"""
import os
import pandas as pd
from typing import List

RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')

def list_raw_files() -> List[str]:
    if not os.path.exists(RAW_DIR):
        return []
    return [os.path.join(RAW_DIR, f) for f in os.listdir(RAW_DIR) if f.lower().endswith('.csv')]

def extract_all() -> pd.DataFrame:
    files = list_raw_files()
    if not files:
        raise FileNotFoundError(f'No CSV files found in {RAW_DIR}. Please add raw CSVs.')
    dfs = []
    for f in files:
        df = pd.read_csv(f)
        dfs.append(df)
    combined = pd.concat(dfs, ignore_index=True)
    return combined

if __name__ == '__main__':
    print('Raw files:', list_raw_files())
