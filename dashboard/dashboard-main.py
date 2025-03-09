import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

def create_df_polusi_udara_date(df):
    df_polusi_udara_date = df.resample(rule="D", on="datetime").agg({
        "PM2.5": "mean",
        "PM10": "mean",
        "SO2": "mean",
        "NO2": "mean",
        "CO": "mean",
        "O3": "mean"
    }).reset_index()
    
    return df_polusi_udara_date


def create_df_suhu_tekanan_udara_date(df):
    df_suhu_tekanan_udara_date = df.resample(rule="D", on="datetime").agg({
        "TEMP": "mean",
        "PRES": "mean"
    }).reset_index()
    
    return df_suhu_tekanan_udara_date

st.title("Air Quality Data : Kota Huairou")

st.header("Tingkat Polusi Udara")

df_huairou = pd.read_csv("main_data.csv")
df_huairou["datetime"] = pd.to_datetime(df_huairou[["year", "month", "day", "hour"]])
df_huairou.sort_values(by='datetime', inplace=True)
df_huairou.reset_index(drop=True, inplace=True)

min_date = df_huairou["datetime"].min()
max_date = df_huairou["datetime"].max()

with st.sidebar:
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = df_huairou[(df_huairou["datetime"] >= str(start_date)) & 
                      (df_huairou["datetime"] <= str(end_date))]

df_polusi_udara_date = create_df_polusi_udara_date(main_df)
df_suhu_tekanan_udara_date = create_df_suhu_tekanan_udara_date(main_df)


st.subheader("PM2.5")

if not df_polusi_udara_date.empty:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        df_polusi_udara_date["datetime"],    
        df_polusi_udara_date["PM2.5"],
        marker="o", 
        linewidth=3,
        color="#1ED918"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)
else:
    st.warning("No data available for the selected date range.")

st.subheader("PM10")

if not df_polusi_udara_date.empty:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        df_polusi_udara_date["datetime"],    
        df_polusi_udara_date["PM10"],
        marker="o", 
        linewidth=3,
        color="#1ED918"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)
else:
    st.warning("No data available for the selected date range.")

st.subheader("SO2")

if not df_polusi_udara_date.empty:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        df_polusi_udara_date["datetime"],    
        df_polusi_udara_date["SO2"],
        marker="o", 
        linewidth=3,
        color="#1ED918"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)
else:
    st.warning("No data available for the selected date range.")

st.subheader("NO2")

if not df_polusi_udara_date.empty:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        df_polusi_udara_date["datetime"],    
        df_polusi_udara_date["NO2"],
        marker="o", 
        linewidth=3,
        color="#1ED918"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)
else:
    st.warning("No data available for the selected date range.")

st.subheader("CO")

if not df_polusi_udara_date.empty:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        df_polusi_udara_date["datetime"],    
        df_polusi_udara_date["CO"],
        marker="o", 
        linewidth=3,
        color="#1ED918"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)
else:
    st.warning("No data available for the selected date range.")

st.subheader("O3")

if not df_polusi_udara_date.empty:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        df_polusi_udara_date["datetime"],    
        df_polusi_udara_date["O3"],
        marker="o", 
        linewidth=3,
        color="#1ED918"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)
else:
    st.warning("No data available for the selected date range.")

st.header("Tingkat Suhu dan Tekanan Udara")

st.subheader("Temperature")

if not df_suhu_tekanan_udara_date.empty:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        df_suhu_tekanan_udara_date["datetime"],    
        df_suhu_tekanan_udara_date["TEMP"],
        marker="o", 
        linewidth=3,
        color="#2E76E8"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)
else:
    st.warning("No data available for the selected date range.")

st.subheader("Pressure")

if not df_suhu_tekanan_udara_date.empty:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        df_suhu_tekanan_udara_date["datetime"],    
        df_suhu_tekanan_udara_date["PRES"],
        marker="o", 
        linewidth=3,
        color="#2E76E8"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)
else:
    st.warning("No data available for the selected date range.")

