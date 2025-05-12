
import streamlit as st
import plotly.graph_objects as go
from equity_utils import get_company_info, get_valuation_ratios, get_price_history, get_financials
import pandas as pd

st.set_page_config(page_title="Equity Research Dashboard", layout="wide")

st.title("📊 Equity Research Dashboard")

ticker = st.text_input("Enter Ticker Symbol", "TSLA")

if ticker:
    company_info = get_company_info(ticker)
    valuation_ratios = get_valuation_ratios(company_info)
    price_data = get_price_history(ticker)
    income_stmt, balance_sheet = get_financials(ticker)

    tabs = st.tabs(["Snapshot", "Valuation", "Price Chart", "Financials"])

    with tabs[0]:
        st.subheader("📌 Company Snapshot")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Name:** {company_info['name']}")
            st.markdown(f"**Sector:** {company_info['sector']}")
            st.markdown(f"**Industry:** {company_info['industry']}")
        with col2:
            st.markdown(f"**Market Cap:** {company_info['marketCap']}")
            st.markdown(f"**Beta:** {company_info['beta']}")
            st.markdown(f"**Price:** {company_info['price']}")
            st.markdown(f"**52-Week High/Low:** {company_info['52WeekHigh']} / {company_info['52WeekLow']}")

    with tabs[1]:
        st.subheader("📉 Valuation Ratios")
        for key, value in valuation_ratios.items():
            st.markdown(f"**{key}:** {value}")

    with tabs[2]:
        st.subheader("📈 Price History")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=price_data.index, y=price_data["Close"], mode='lines', name='Close Price'))
        fig.update_layout(title=f"{ticker.upper()} Stock Price", xaxis_title="Date", yaxis_title="Price")
        st.plotly_chart(fig, use_container_width=True)

    with tabs[3]:
        st.subheader("📊 Financials")
        st.markdown("**Income Statement (Top 5 Rows):**")
        st.dataframe(income_stmt.head())
        st.markdown("**Balance Sheet (Top 5 Rows):**")
        st.dataframe(balance_sheet.head())
