# Finance-Analytics-Python

# Finance Analytics Dashboard

A Streamlit dashboard and set of analysis scripts built on a company financial dataset (Revenue, Profit, ROI, Expenses, Sector) to explore revenue trends, profitability, sector performance, and risk/return by company.

## Structure

```
├── data/
│   └── financial_data.csv          # NOT included — add your own (see below)
├── scripts/
│   ├── clean_data.py               # loads raw data, cleans it, saves financial_data_clean.csv
│   ├── Dashboard.py                 # Streamlit app — run this for the interactive dashboard
│   ├── Q1_top_revenue.py            # Top 10 companies by revenue
│   ├── Q2_top_profit.py             # Profit share by company (pie)
│   ├── Q3_Avg_roi.py                # Average ROI KPI card
│   ├── Q4_Monthly_revenue.py        # Revenue trend over time
│   ├── Q5_yearly_profit_growth.py   # Year-over-year profit growth %
│   ├── Q6_sector_revenue.py         # Revenue by sector
│   ├── Q7_sector_profit.py          # Profit share by sector (pie)
│   ├── Q8_top_stocks.py             # Companies ranked by average ROI
│   └── Q9_profit_margin.py          # Profit margin by company
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone <this-repo-url>
cd <repo-name>
pip install -r requirements.txt
```

Add your dataset at `data/financial_data.csv`. It must have at least these columns: `Date, Company, Sector, Revenue, Profit, Expenses, Investment, ROI (%)`.

Run the cleaning step once, before anything else:

```bash
python scripts/clean_data.py
```

This produces `data/financial_data_clean.csv`, which every other script and the dashboard reads from.

## Run the dashboard

```bash
streamlit run scripts/Dashboard.py
```

## Run an individual analysis script

```bash
python scripts/Q1_top_revenue.py
```

## Known limitations

- Each `Q*.py` script independently loads and groups the data — there's no shared module, so logic like sector grouping is duplicated across files rather than reused.
- No automated tests.
- Dataset is not included in this repo; you must supply your own with matching column names.

