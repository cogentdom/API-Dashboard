import streamlit as st
import pandas as pd
import matplotlib.style as style
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json

plt.style.use('seaborn-darkgrid')
plt.rc('patch', force_edgecolor=True,edgecolor='black')
plt.rc('hist', bins='auto')
sns.set_context('notebook')
sns.set_palette('gist_heat')
st.set_page_config(layout='wide')

url = 'https://api-stock-getter-rghwdwjikq-uc.a.run.app/price/aapl'

ticker_list = ["AAPL", "GOOG", "MSFT", "TSLA"]

response = requests.get(url)
data = json.loads(response.text)
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df = df.resample('2w').mean()
print(df)

def decomp_plot(df):
    plt.figure(figsize=(17,8))
    plt.plot(df)
    plt.plot(df.rolling(window = 12).mean().dropna(), color='g')
    plt.plot(df.rolling(window = 12).std().dropna(), color='blue')
    plt.title('Rolling mean')
    plt.legend(['Apple', 'mean', 'std'])

def tripleGraph(data):
    chart1 = data
    chart2 = data.rolling(window = 12).mean().dropna()
    chart3 = data.rolling(window = 12).std().dropna()

    df = pd.concat([chart1, chart2, chart3], axis=1)
    df.columns=['Close', 'Rolling Mean', 'Rolling Std']

    st.title('Rolling value decomposition on Apple stock')
    st.line_chart(df, width=800)


# decomp_plot(df['Close'])
tripleGraph(df['Close'])