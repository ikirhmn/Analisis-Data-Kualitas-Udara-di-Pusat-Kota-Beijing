import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Pertanyaan Bisnis:
#1. Bagaimana tren kualitas udara (PM2.5, PM10, SO2, NO2, CO, O3) pada bagian pusat kota beijing (Antizhongxin, Dongsi) berubah dari waktu ke waktu?
#2. Apakah ada korelasi antara kondisi cuaca (suhu, tekanan, kelembaban, curah hujan) dan tingkat polusi udara?

# Load data
aotizhongxin_df = pd.read_csv("F:\Kuliah\Semangattt ML\DBS Latihan\Project Dashboard\Analisis-Data-Kualitas-Udara-di-Pusat-Kota-Beijing\dashboard\PRSA_Data_Aotizhongxin_20130301-20170228.csv")
dongsin_df = pd.read_csv("F:\Kuliah\Semangattt ML\DBS Latihan\Project Dashboard\Analisis-Data-Kualitas-Udara-di-Pusat-Kota-Beijing\dashboard\PRSA_Data_Dongsi_20130301-20170228.csv")

aotizhongxin_df['date'] = pd.to_datetime(aotizhongxin_df[['year', 'month', 'day']])
dongsin_df['date'] = pd.to_datetime(dongsin_df[['year', 'month', 'day']])

aotizhongxin_df.set_index('date', inplace=True)
dongsin_df.set_index('date', inplace=True)

# Menentukan dataset yang digunakan
st.title('Air Quality Dashboard :sparkles:')
st.markdown("""Dashboard ini memberikan wawasan tentang kualitas udara berdasarkan data dari berbagai lokasi.""")

tab1, tab2, tab3 = st.tabs(["Tren Polusi Udara", "Korelasi Antar Polutan", "Ringkasan Statistik"])

# **1. Analisis Tren Polusi Udara**
with tab1:
    st.subheader("Tren Polusi Udara")
    col1, col2 = st.columns(2)
    with col1:
        location = st.radio("Pilih Lokasi", ["Aotizhongxin", "Dongsi"], index=0)
    with col2:
        pollutant = st.selectbox("Pilih Polutan", ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"], index=0)
    
    data = aotizhongxin_df if location == "Aotizhongxin" else dongsin_df
    
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(data.index, data[pollutant], marker='o', linewidth=2, color="#90CAF9")
    ax.set_xlabel("Tanggal")
    ax.set_ylabel(f"Konsentrasi {pollutant} (µg/m³)")
    ax.set_title(f"Tren {pollutant} di {location}")
    st.pyplot(fig)

# **2. Korelasi Antar Polutan**
with tab2:
    st.subheader("Matriks Korelasi Polutan")
    correlation_matrix = data[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig)

# **3. Ringkasan Statistik Polusi Udara**
with tab3:
    st.subheader("Ringkasan Statistik")
    st.dataframe(data[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].describe())

st.caption('Copyright © 2025')
