📦 E-Commerce Product Delivery Prediction
⭐ 1. Overview

This project provides a complete, production-ready pipeline for predicting whether an e-commerce product will be delivered on time.
It includes automated ETL, machine learning pipelines, dashboard-ready data outputs, CI support, and project documentation.

🚀 2. Technologies Used

Python (Pandas, NumPy, Seaborn, Matplotlib)

Scikit-learn:

Random Forest

Decision Tree

Logistic Regression

KNN

Jupyter Notebook

Parquet conversion for BI tools

GitHub Actions (CI)

📘 3. Data Dictionary
Variable	Description
ID	Unique Customer ID
Warehouse_block	Warehouse location (A, B, C, D, E)
Mode_of_Shipment	Shipment method (Ship, Flight, Road)
Customer_care_calls	Number of calls made by customer regarding shipment
Customer_rating	Rating (1 = lowest, 5 = highest)
Cost_of_the_Product	Product cost in USD
Prior_purchases	Number of prior purchases by customer
Product_importance	low / medium / high
Gender	Male / Female
Discount_offered	Discount percentage
Weight_in_gms	Weight of product in grams
Reached.on.Time_Y.N	Target: 1 = Late, 0 = On Time
📊 4. Key Insights From Exploratory Analysis

Product weight and cost strongly influence delivery time.

More customer care calls correlate with delayed delivery.

Loyal customers (high prior purchases) have better on-time delivery rates.

Discounts below 10% are linked to more late deliveries.

Heavier products (2500–3500g) and low-cost items (< $250) tend to face more delays.

🧠 5. ML Model Performance Overview
Model	Accuracy
Decision Tree	69%
Random Forest	68%
Logistic Regression	63%
KNN	65%

📌 The Decision Tree Classifier achieved the best accuracy.

⚙️ 6. Features Included
ETL Pipeline (etl/)

extract.py — Fetch raw CSV files

transform.py — Clean, normalize, handle missing data

load.py — Save processed dataset

pipeline.py — Execute full ETL

Machine Learning Pipeline (ml/)

advanced_train.py — Feature engineering + RandomizedSearchCV

predict.py — Predict outcomes using trained model

Dashboard Helpers (scripts/)

export_to_parquet.py

create_hyper.py (Tableau helper placeholder)

One-click Automation

run_all.py

run_all.sh

CI/CD (GitHub Actions)

.github/workflows/ci.yml — Runs tests, ETL, verification

⚡ 7. Quickstart Guide
Step 1 — Setup Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

Step 2 — Run Entire Pipeline
python run_all.py

Generated Outputs
File	Location
Processed CSV	data/processed/processed_data.csv
Model	models/advanced_model.pkl
Metadata	models/metadata.json
Predictions	predictions.csv
BI Parquet File	data/processed/processed_data.parquet
Deliverable ZIP	E_commerceProductDeliveryPrediction-deliverable.zip
📊 8. Dashboard Integration (Power BI / Tableau)

Convert CSV → Parquet:

python scripts/export_to_parquet.py --input data/processed/processed_data.csv --output data/processed/processed_data.parquet


Import into:

Power BI → Get Data → Parquet

Tableau → File → Open → Parquet/CSV

📝 9. Release Notes — v1.0 Final
✅ What’s New

Complete ETL + ML pipeline

Automated workflow

BI-ready outputs

CI workflow

Full documentation

Model performance reporting

⚠️ Known Limitations

Auto target detection may need manual override

.hyper export is implemented as a placeholder

📌 10. Conclusion

This project delivers a production-ready solution for analyzing and predicting delivery performance in e-commerce logistics.

Key takeaways:

Product attributes, customer behavior, and shipping method significantly impact delivery timing.

Decision Tree models provide high interpretability and competitive performance.

Automated pipelines streamline ETL, model training, and deployment preparation.

This makes the project suitable for:

Data science portfolios

Machine learning deployment practice

Business intelligence integration

Academic submissions
