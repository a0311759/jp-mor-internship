
import subprocess
import sys
import os

# Function to generate the requirements.txt file
def generate_requirements():
    try:
        # Freeze the current environment's installed packages and save to requirements.txt
        with open('requirements.txt', 'w') as f:
            subprocess.check_call([sys.executable, "-m", "pip", "freeze"], stdout=f)
        print("requirements.txt has been created.")
    except Exception as e:
        print(f"Failed to generate requirements.txt: {e}")

# Check if requirements.txt exists, if not, generate it
if not os.path.exists('requirements.txt'):
    generate_requirements()

# Continue with the rest of your application
import yfinance as yf
import streamlit as st
import pandas as pd

# Function to fetch stock price data for the last 12 months
def get_last_12_months_data(ticker):
    stock = yf.Ticker(ticker)
    stock_data = stock.history(period='1y', interval='1mo')  # Fetch data for the last year, monthly intervals
    return stock_data['Close']  # Return the monthly closing prices

# Streamlit app interface
def main():
    st.title("Stock Price Viewer")
    st.write("Enter a stock ticker symbol to get the closing prices over the last 12 months.")
    
    # Input for stock ticker
    ticker = st.text_input("Enter stock ticker (e.g., AAPL, MSFT, TSLA):", "AAPL").upper()

    if ticker:
        try:
            # Fetch and display stock data
            stock_data = get_last_12_months_data(ticker)

            if not stock_data.empty:
                st.write(f"Monthly closing prices for {ticker} over the last 12 months:")
                st.line_chart(stock_data)  # Display a line chart of the stock prices
                st.dataframe(stock_data)   # Display the data in a table format
            else:
                st.warning(f"No data found for ticker: {ticker}")

        except Exception as e:
            st.error(f"Error fetching data for {ticker}: {str(e)}")

if __name__ == '__main__':
    main()
