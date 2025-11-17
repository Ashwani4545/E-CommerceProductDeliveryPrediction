# run_all.py - cross-platform runner for ETL -> train -> predict -> export -> zip
import subprocess, os, sys, shutil
def run(cmd):
    print('RUN:', cmd)
    r = subprocess.run(cmd, shell=True)
    if r.returncode != 0:
        print('Command failed:', cmd)
steps = [
    'python -m etl.pipeline',
    'python ml/advanced_train.py',
    'python scripts/export_to_parquet.py --input data/processed/processed_data.csv --output data/processed/processed_data.parquet',
    'python -m ml.predict --input data/processed/processed_data.csv --output predictions.csv || true'
]
for s in steps:
    run(s)
# create zipped deliverable
out = 'E_commerceProductDeliveryPrediction-deliverable.zip'
if os.path.exists(out):
    os.remove(out)
import zipfile
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk('.'):
        for f in files:
            if root.startswith('./venv') or root.startswith('data/processed') or root.startswith('models'):
                continue
            zf.write(os.path.join(root,f))
print('Created', out)
