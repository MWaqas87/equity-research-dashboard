
import yfinance as yf
import pandas as pd

def get_company_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        'name': info.get('longName', 'N/A'),
        'sector': info.get('sector', 'N/A'),
        'industry': info.get('industry', 'N/A'),
        'marketCap': info.get('marketCap', 'N/A'),
        'beta': info.get('beta', 'N/A'),
        'price': info.get('currentPrice', 'N/A'),
        '52WeekHigh': info.get('fiftyTwoWeekHigh', 'N/A'),
        '52WeekLow': info.get('fiftyTwoWeekLow', 'N/A')
    }

def get_valuation_ratios(info):
    return {
        'P/E': info.get('trailingPE', 'N/A'),
        'ROE': info.get('returnOnEquity', 'N/A'),
        'ROA': info.get('returnOnAssets', 'N/A'),
        'D/E': info.get('debtToEquity', 'N/A'),
        'EPS': info.get('trailingEps', 'N/A')
    }

def get_price_history(ticker, period='1y'):
    stock = yf.Ticker(ticker)
    return stock.history(period=period)

def get_financials(ticker):
    stock = yf.Ticker(ticker)
    income_stmt = stock.financials
    balance_sheet = stock.balance_sheet
    return income_stmt, balance_sheet
