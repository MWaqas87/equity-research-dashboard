
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

def get_news(ticker):
    url = f"https://finviz.com/quote.ashx?t={ticker}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find("table", class_="fullview-news-outer")
    news = []
    if table:
        rows = table.find_all("tr")
        for row in rows[:10]:
            tds = row.find_all("td")
            headline = tds[1].text.strip()
            link = tds[1].a['href'] if tds[1].a else "#"
            sentiment = TextBlob(headline).sentiment.polarity
            news.append((headline, link, sentiment))
    return news

if ticker:
    st.markdown("---")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("📌 Snapshot")
        company_info = get_company_info(ticker)
        st.markdown(f"**Company:** {company_info['name']}")
        st.markdown(f"**Sector:** {company_info['sector']}")
        st.markdown(f"**Industry:** {company_info['industry']}")
    try:
    net_income = None
    for label in ["Net Income", "Net Income Applicable To Common Shares", "NetIncome"]:
    if label in income_stmt.index:
    net_income = income_stmt.loc[label].iloc[::-1].round(2)
    break
    
    revenue = None
    for label in ["Total Revenue", "Revenue", "TotalRevenue"]:
    if label in income_stmt.index:
    revenue = income_stmt.loc[label].iloc[::-1].round(2)
    break
    
    assets = None
    for label in ["Total Assets", "Assets", "TotalAssets", "Invested Capital"]:
    if label in balance_sheet.index:
    assets = balance_sheet.loc[label].iloc[::-1].round(2)
    break
    
    liabilities = None
    for label in ["Total Liab", "Liabilities", "TotalLiabilities", "Total Debt"]:
    if label in balance_sheet.index:
    liabilities = balance_sheet.loc[label].iloc[::-1].round(2)
    break
    
    if revenue is not None and net_income is not None:
    sample = revenue.dropna().iloc[0]
    scale = 1e9 if abs(sample) >= 1e9 else 1e6 if abs(sample) >= 1e6 else 1
    unit = " (Billions USD)" if scale == 1e9 else " (Millions USD)" if scale == 1e6 else ""
    revenue /= scale
    net_income /= scale
    st.markdown("#### Revenue vs. Net Income" + unit)
    st.line_chart(pd.DataFrame({"Revenue": revenue, "Net Income": net_income}))
    else:
    st.warning("Revenue or Net Income not available. Found rows: " + ", ".join(income_stmt.index[:10]))
    
    if assets is not None and liabilities is not None:
    sample_bs = assets.dropna().iloc[0]
    scale_bs = 1e9 if abs(sample_bs) >= 1e9 else 1e6 if abs(sample_bs) >= 1e6 else 1
    unit_bs = " (Billions USD)" if scale_bs == 1e9 else " (Millions USD)" if scale_bs == 1e6 else ""
    assets /= scale_bs
    liabilities /= scale_bs
    st.markdown(f"#### {assets.name} vs. {liabilities.name}" + unit_bs)
    st.bar_chart(pd.DataFrame({"Assets": assets, "Liabilities": liabilities}))
    else:
    st.warning("Assets or Liabilities not available. Found rows: " + ", ".join(balance_sheet.index[:10]))
    
    except Exception as e:
        st.warning("An error occurred while loading financial data.")
 Exception as e:
            st.warning("An error occurred while loading financial data.")

    with tab3:
        st.subheader("📰 Latest News & Sentiment")
        news_items = get_news(ticker)
        for title, link, sentiment in news_items:
            label = "🟢 Positive" if sentiment > 0.1 else "🔴 Negative" if sentiment < -0.1 else "⚪ Neutral"
            st.markdown(f"- [{title}]({link}) — *{label}*")