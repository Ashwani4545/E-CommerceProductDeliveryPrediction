#!/usr/bin/env bash
set -e
echo "1) Running ETL"
python -m etl.pipeline
echo "2) Training advanced model"
python ml/advanced_train.py
echo "3) Exporting parquet for dashboards"
python scripts/export_to_parquet.py --input data/processed/processed_data.csv --output data/processed/processed_data.parquet
echo "4) Creating predictions using advanced model"
python -m ml.predict --input data/processed/processed_data.csv --output predictions.csv || true
echo "5) Zipping final deliverable"
ZIPNAME="E_commerceProductDeliveryPrediction-deliverable.zip"
zip -r ${ZIPNAME} . -x "venv/*" -x "data/processed/*" -x "models/*"
echo "Deliverable zipped to ${ZIPNAME}"
