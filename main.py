import streamlit as st
import pandas as pd
import requests
import json
import os

st.set_page_config(layout='wide')
url = 'https://devgroup.hclapigeex.com/data'
ticker_list = {"HCL Technologies":"HCLTECH.NS", "Apple":"AAPL", "Google":"GOOG", "Microsoft":"MSFT", 
                "Tesla":"TSLA", "Bitcoin":"BTC-USD", "Ethereum":"ETH-USD", "Dogecoin":"DOGE-USD", 
                "Cardano":"ADA-USD", "Bitcoin Cash":"BCH-USD", "Filecoin":"FIL-USD", "Solana":"SOL-USD",
                "Storj":"STORJ-USD", "Polkadot":"DOT-USD"}
stocks = ("HCL Technologies", "Apple", "Google", "Microsoft", "Tesla", "Bitcoin", "Ethereum", "Dogecoin", 
            "Cardano", "Bitcoin Cash", "Filecoin", "Solana", "Storj", "Polkadot")
selected_stock = st.selectbox("Select an entity to retrieve", stocks)
url = f'{url}/{ticker_list[selected_stock]}'
print(url)
api_key = os.environ.get('DATA_RUNNER_API_KEY')
headers = {'apikey': api_key}
response = requests.get(url, headers=headers)
print(response)
data = json.loads(response.text)
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df.Date, unit='ms')
df.set_index('Date', inplace=True, drop=True)

def tripleGraph(data):
    chart1 = data
    chart2 = data.rolling(window = 12).mean().dropna()
    chart3 = data.rolling(window = 12).std().dropna()
    df = pd.concat([chart1, chart2, chart3], axis=1)
    df.columns=['Closing Price', 'Rolling Mean', 'Rolling Std']
    st.title(f'Rolling decomposition on the valuation of {selected_stock}')
    st.line_chart(df, width=800)

tripleGraph(df['Close'])