
import streamlit as st
import yfinance as yf
import pandas as pd
import ta

st.set_page_config(page_title="Dashboard Robot Trading Syariah - ChanLun & Fundamental", layout="wide")
st.title("📈 Dashboard Robot Trading Syariah - ChanLun & Fundamental")

# Input saham
ticker = st.text_input("Masukkan kode saham (contoh: BBCA.JK)", value="BBCA.JK")

if ticker:
    try:
        data = yf.download(ticker, period="6mo", interval="1d")

        if not data.empty and 'Close' in data.columns and not data['Close'].isnull().all():
            close_series = data['Close'].squeeze()
            data['MA20'] = ta.trend.sma_indicator(close_series, window=20)

            st.line_chart(data[['Close', 'MA20']].dropna())
        else:
            st.warning("Data harga penutupan (Close) tidak tersedia atau kosong.")
    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
else:
    st.info("Silakan masukkan kode saham terlebih dahulu.")
