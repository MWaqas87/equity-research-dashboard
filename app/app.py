
import streamlit as st
import plotly.graph_objects as go
from equity_utils import get_company_info, get_price_history, get_financials
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

st.set_page_config(page_title="Equity Research Dashboard", layout="wide")

st.markdown("""<h1 style='text-align: center; color: #00adb5;'>📊 Equity Research Dashboard</h1>""", unsafe_allow_html=True)

ticker = st.text_input("Enter Stock Ticker", "TSLA")

if ticker:
    st.markdown("---")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("📌 Snapshot")
        company_info = get_company_info(ticker)
        st.markdown(f"**Company:** {company_info['name']}")
        st.markdown(f"**Sector:** {company_info['sector']}")
        st.markdown(f"**Industry:** {company_info['industry']}")
        st.markdown(f"**Market Cap:** {company_info['marketCap']}")
        st.markdown(f"**Beta:** {company_info['beta']}")
        st.markdown(f"**Current Price:** ${company_info['price']}")
        st.markdown(f"**52-Week Range:** ${company_info['52WeekLow']} - ${company_info['52WeekHigh']}")

    with col2:
        st.subheader("📉 Valuation Ratios")
        stock = yf.Ticker(ticker)
        info = stock.info
        ratios = {
            "P/E Ratio": info.get("trailingPE", "N/A"),
            "Return on Equity (ROE)": info.get("returnOnEquity", "N/A"),
            "Return on Assets (ROA)": info.get("returnOnAssets", "N/A"),
            "Debt-to-Equity (D/E)": info.get("debtToEquity", "N/A"),
            "Earnings Per Share (EPS)": info.get("trailingEps", "N/A")
        }
        for label, value in ratios.items():
            st.markdown(f"**{label}:** {value}")

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📈 Price Chart", "📊 Financials", "📰 News Sentiment"])

    with tab1:
        st.subheader(f"{ticker.upper()} Price History")
        history = get_price_history(ticker)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=history.index, y=history["Close"], mode='lines', name='Close'))
        fig.update_layout(xaxis_title="Date", yaxis_title="Price (USD)", template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("📊 Financial Statements")
        income_stmt, balance_sheet = get_financials(ticker)
        st.markdown("**Income Statement (Top 5 Rows):**")
        st.dataframe(income_stmt.head())
        st.markdown("**Balance Sheet (Top 5 Rows):**")
        st.dataframe(balance_sheet.head())

    with tab3:
        st.subheader("📰 Latest News & Sentiment")

        def get_news(ticker):
            url = f"https://finviz.com/quote.ashx?t={ticker}"
            headers = {"User-Agent": "Mozilla/5.0"}
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.text, "html.parser")
            table = soup.find("table", class_="fullview-news-outer")
            news = []
            if table:
                rows = table.find_all("tr")
                for row in rows[:10]:  # limit to 10 headlines
                    tds = row.find_all("td")
                    headline = tds[1].text.strip()
                    link = tds[1].a['href']
                    sentiment = TextBlob(headline).sentiment.polarity
                    news.append((headline, link, sentiment))
            return news

        news_items = get_news(ticker)
        for title, link, sentiment in news_items:
            label = "🟢 Positive" if sentiment > 0.1 else "🔴 Negative" if sentiment < -0.1 else "⚪ Neutral"
            st.markdown(f"- [{title}]({link}) — *{label}*")
