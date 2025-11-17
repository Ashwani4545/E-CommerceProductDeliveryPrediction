"""etl/transform.py - basic cleaning"""
import pandas as pd
import re

def to_snake_case(s: str) -> str:
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    s = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s)
    s = re.sub('[^0-9a-zA-Z_]+', '_', s)
    return s.lower().strip('_')

def basic_transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={c: to_snake_case(c) for c in df.columns})
    df = df.drop_duplicates().reset_index(drop=True)
    for col in df.columns:
        if df[col].dtype == object:
            coerced = pd.to_numeric(df[col], errors='ignore')
            if coerced.dtype != object:
                df[col] = coerced
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            med = df[col].median()
            df[col] = df[col].fillna(med)
        else:
            df[col] = df[col].fillna('unknown')
    return df

if __name__ == '__main__':
    import pandas as pd
    print('Running basic transform on example dataframe')
    df = pd.DataFrame({'A':[1,2,None], 'Name':['a', None, 'c']})
    print(basic_transform(df))
