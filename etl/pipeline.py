"""etl/pipeline.py - orchestrate extract -> transform -> load"""
from . import extract, transform, load
import logging, sys, os

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def run():
    logging.info('Starting ETL pipeline')
    try:
        df = extract.extract_all()
    except Exception as e:
        logging.error('Extract failed: %s', e)
        sys.exit(1)
    logging.info('Extracted %d rows', len(df))
    df_t = transform.basic_transform(df)
    logging.info('Transformed: %d rows, %d cols', df_t.shape[0], df_t.shape[1])
    out_path = load.load_to_csv(df_t)
    logging.info('Loaded processed data to %s', out_path)
    return out_path

if __name__ == '__main__':
    run()
