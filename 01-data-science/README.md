# IBM Data Science Professional Certificate — SpaceX Capstone

**Source repo:** https://github.com/ruisuphd/IBM_Data_Science  
**Programme:** IBM Data Science Professional Certificate (Coursera)  
**Stack:** Python, Jupyter Notebook, Plotly Dash, SQL, Folium, scikit-learn

## Overview

End-to-end capstone project predicting whether SpaceX Falcon 9 first stages will land successfully. A cost model is developed to estimate launch costs based on landing prediction, providing a competitive intelligence tool for alternative launch providers.

## Contents

| File | Description |
|------|-------------|
| `jupyter-labs-spacex-data-collection-api.ipynb` | Data collection via SpaceX REST API |
| `jupyter-labs-webscraping.ipynb` | Supplementary data via web scraping |
| `labs-jupyter-spacex-Data wrangling.ipynb` | Data cleaning and wrangling |
| `jupyter-labs-eda-sql-coursera_sqllite.ipynb` | EDA with SQL (SQLite) |
| `edadataviz.ipynb` | EDA with Matplotlib and Seaborn |
| `lab_jupyter_launch_site_location.ipynb` | Geospatial analysis with Folium |
| `SpaceX_Machine Learning Prediction_Part_5.ipynb` | ML classification models |
| `spacex-dash-app.py` | Interactive Plotly Dash dashboard |
| `dataset_part_*.csv`, `spacex_web_scraped.csv` | Datasets |

## Setup

```bash
pip install pandas numpy scikit-learn matplotlib seaborn folium plotly dash requests beautifulsoup4
jupyter notebook
```

## Key Results

Four classifiers (Logistic Regression, SVM, Decision Tree, KNN) were tuned via GridSearchCV. Decision Tree and SVM achieved the best test accuracy. See the ML prediction notebook for full results.
