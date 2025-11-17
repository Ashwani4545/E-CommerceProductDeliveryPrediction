# Power BI & Tableau Integration Guide
1. Run ETL: python -m etl.pipeline
2. Convert to parquet: python scripts/export_to_parquet.py --input data/processed/processed_data.csv --output data/processed/processed_data.parquet
3. Open Power BI or Tableau and connect to parquet/csv.
For production, write to a database and connect BI tools there.
