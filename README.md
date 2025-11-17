# E-Commerce Product Delivery Prediction

## 1. Overview
This project provides a complete, production-ready pipeline for predicting e-commerce product delivery performance. It includes:

- **ETL Pipeline**: Extract, transform, and load raw CSV files  
- **Machine Learning Pipeline**: Model training, hyperparameter tuning, predictions  
- **Dashboard Integration**: Power BI & Tableau-ready artifacts  
- **One-Click Execution**: Automated pipeline that performs the entire workflow end-to-end  
- **CI/CD Support**: GitHub Actions workflow  
- **Documentation & Release Notes**  

---

## 2. Features Included

### ETL Pipeline (etl/)
- `extract.py`
- `transform.py`
- `load.py`
- `pipeline.py`

### Machine Learning Pipeline (ml/)
- `advanced_train.py`
- `predict.py`

### Dashboard Helpers (scripts/)
- `export_to_parquet.py`
- `create_hyper.py`

### One-click Automation
- `run_all.py`
- `run_all.sh`

### CI/CD
- `.github/workflows/ci.yml`

---

## 3. Quickstart Guide

### Step 1 — Setup
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2 — Run entire pipeline
```
python run_all.py
```

### Output Files
- Processed CSV → `data/processed/processed_data.csv`
- Model → `models/advanced_model.pkl`
- Metadata → `models/metadata.json`
- Predictions → `predictions.csv`
- Parquet → `data/processed/processed_data.parquet`
- Deliverable ZIP → `E_commerceProductDeliveryPrediction-deliverable.zip`

---

## 4. Dashboard Integration (Power BI / Tableau)

Convert processed CSV to Parquet:
```
python scripts/export_to_parquet.py --input data/processed/processed_data.csv --output data/processed/processed_data.parquet
```

---

## 5. Release Notes — v1.0 Final

### What's New
- Complete ETL + ML Pipeline  
- Full automation  
- Dashboard-ready outputs  
- CI workflow  
- Documentation  

### Known Limitations
- Auto target detection may need manual override  
- Tableau `.hyper` export is placeholder  

---

## 6. Summary
This single README provides full documentation for your refined, production-ready project.


## 📦 E-Commerce Product Delivery Prediction – Dataset & Insights Add-on

This extended section provides deeper insights into the original dataset used for model training and evaluation.

---

# 📦 E-Commerce Product Delivery Prediction (Original Dataset Overview)

This project also includes an analysis of a structured e-commerce logistics dataset containing **10,999 records** and **12 features** related to warehouse operations, customer behavior, and product shipment details.

## 🚀 Technologies Used
- Python, Pandas, Seaborn, Matplotlib  
- Scikit-learn (Random Forest, Decision Tree, Logistic Regression, KNN)  
- Jupyter Notebook  

---

## 📘 Data Dictionary

| Variable             | Description                                             |
|----------------------|---------------------------------------------------------|
| ID                   | Unique Customer ID                                      |
| Warehouse_block      | Warehouse location (A, B, C, D, E)                      |
| Mode_of_Shipment     | Shipment method (Ship, Flight, Road)                    |
| Customer_care_calls  | Number of customer calls regarding shipment             |
| Customer_rating      | Customer rating (1 - Lowest, 5 - Highest)               |
| Cost_of_the_Product  | Cost of product (USD)                                   |
| Prior_purchases      | Number of previous orders by customer                   |
| Product_importance   | Category: low, medium, high                             |
| Gender               | Male / Female                                           |
| Discount_offered     | Discount percentage                                     |
| Weight_in_gms        | Weight of product in grams                              |
| Reached.on.Time_Y.N  | Target variable: 1 = Late, 0 = On time                  |

---

## 📊 Key Insights From Exploratory Analysis

- **Product weight and cost** are major contributors to delivery delays.  
- More **customer care calls = higher chance of late delivery**.  
- **Loyal customers** (higher prior purchases) tend to receive faster deliveries.  
- Discounts below **10%** correlate with more late deliveries.  

---

## 🧠 ML Model Performance Overview

| Model                | Accuracy |
|----------------------|----------|
| Decision Tree        | 69%      |
| Random Forest        | 68%      |
| Logistic Regression  | 63%      |
| KNN                  | 65%      |

The **Decision Tree Classifier** performed the best with **69% accuracy**.

---

## 📌 Combined Conclusion

Product characteristics (like weight and cost), customer behavior (inquiries and prior purchases), and shipping method significantly influence delivery timing.  
Among machine learning models, **Decision Trees** provided the most reliable accuracy for this dataset and business case.

---
