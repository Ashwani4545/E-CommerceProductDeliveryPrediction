# scripts/export_to_parquet.py
import argparse, pandas as pd, os
def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    df = pd.read_csv(args.input)
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    df.to_parquet(args.output, index=False)
    print('Wrote', args.output)
if __name__ == '__main__':
    main()
