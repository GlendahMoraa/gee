import yfinance as yf
import streamlit as st
import pandas as pd


st.write('''
# Topic

## Subtopic

Description
''')



tickerSymbol = "GOOGL"

tickerData = yf.Ticker(tickerSymbol)

ticherdf = tickerData.history(Period = 'id', start = '2010-5-31', end = '2020-5-31')


st.write('1. Closing prices')
st.line_chart(ticherdf.Close)

st.write('2. The volumes')
st.line_chart(ticherdf.Volume)