
# 📊 Equity Research Dashboard

A Streamlit-based interactive dashboard for analyzing public companies by ticker symbol. This tool pulls real-time financial and stock data from Yahoo Finance to display a company's valuation metrics, market performance, and basic financials — perfect for students, aspiring analysts, or finance professionals testing equity ideas.

---

## 🚀 Features

- Input a stock ticker and get:
  - Company snapshot (sector, market cap, price range)
  - Key valuation ratios (P/E, ROE, D/E, EPS, etc.)
  - Interactive historical stock price chart (Plotly)
  - Summary of income statement and balance sheet

---

## 🧪 Sample Use

Enter tickers like:
- `TSLA` – Tesla
- `AAPL` – Apple
- `MSFT` – Microsoft

---

## 📁 Project Structure

```
equity-research-dashboard/
├── app/
│   ├── app.py              # Main Streamlit app
│   └── equity_utils.py     # Data fetching and calculations
├── requirements.txt
└── README.md
```

---

## 💻 How to Run

1. Clone the repo:
```bash
git clone https://github.com/your-username/equity-research-dashboard.git
cd equity-research-dashboard/app
```

2. Install requirements:
```bash
pip install -r ../requirements.txt
```

3. Launch Streamlit app:
```bash
streamlit run app.py
```

---

## 🛠 Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [yfinance](https://pypi.org/project/yfinance/)
- [Plotly](https://plotly.com/python/)

---

## 🌐 Live Deployment (optional)

If deployed via Streamlit Cloud:
> 🔗 [Live App URL Here]

---

## 🙋‍♂️ Author

**Mohammad Waqas**  
[LinkedIn](https://www.linkedin.com/in/mohammad-waqas-29972959/) | MSBA @ Georgetown | Sr. Banker @ BofA

---

## 📬 Feedback

Ideas, improvements, or collaboration? Feel free to fork, open an issue, or connect.

