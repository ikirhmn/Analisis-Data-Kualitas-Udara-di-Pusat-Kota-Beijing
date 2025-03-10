import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap



sns.set(style='dark')

# Load data
aotizhongxin_df = pd.read_csv("data/PRSA_Data_Aotizhongxin_20130301-20170228.csv")
dongsin_df = pd.read_csv("data/PRSA_Data_Dongsi_20130301-20170228.csv")

# Buat kolom tanggal dan set sebagai indeks
aotizhongxin_df['date'] = pd.to_datetime(aotizhongxin_df[['year', 'month', 'day']])
dongsin_df['date'] = pd.to_datetime(dongsin_df[['year', 'month', 'day']])

# Tambahkan kolom lokasi
aotizhongxin_df['Lokasi'] = 'Aotizhongxin'
dongsin_df['Lokasi'] = 'Dongsi'

aotizhongxin_df['latitude'] = 39.98
aotizhongxin_df['longitude'] = 116.41

dongsin_df['latitude'] = 39.93
dongsin_df['longitude'] = 116.42


# Gabungkan dataset tanpa mengabaikan indeks
combined_df = pd.concat([aotizhongxin_df, dongsin_df]).set_index('date')

# Title Dashboard
st.title('🌍 Air Quality Dashboard Pusat Kota Beijing')
st.markdown("""
Dashboard ini memberikan wawasan tentang kualitas udara berdasarkan data dari dua lokasi di Beijing.
""")
st.markdown("### **Ringkasan Data**")
col1, col2 = st.columns(2)
col1.metric("Total Data Aotizhongxin", len(aotizhongxin_df))
col2.metric("Total Data Dongsi", len(dongsin_df))

# Pilihan Polutan dan Skala Waktu
col1, col2 = st.columns(2)
with col1:
    pollutant = st.selectbox("☁️ Pilih Polutan", ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"], index=0)
with col2:
    time_scale = st.selectbox("📅 Pilih Skala Waktu", ["Tahunan", "Bulanan", "Mingguan"], index=1)

# Mapping pilihan skala waktu ke kode resampling Pandas
time_scale_map = {
    "Tahunan": "Y",
    "Bulanan": "M",
    "Mingguan": "W"
}

# **1. Tren Polusi Udara**
st.subheader("📈 Tren Polusi Udara di Dua Lokasi")
fig, ax = plt.subplots(figsize=(16, 6))

for loc in ["Aotizhongxin", "Dongsi"]:
    data = combined_df[combined_df["Lokasi"] == loc]
    avg_data = data[pollutant].resample(time_scale_map[time_scale]).mean()
    sns.lineplot(x=avg_data.index, y=avg_data, ax=ax, label=f"{pollutant} - {loc}")

ax.set_xlabel("Tanggal")
ax.set_ylabel(f"Konsentrasi {pollutant} (µg/m³)")
ax.set_title(f"📈 Tren {pollutant} berdasarkan {time_scale}")
ax.legend()
st.pyplot(fig)

# **2. Korelasi antara Faktor Cuaca dan Polusi Udara**
# **2. Korelasi antara Faktor Cuaca dan Polusi Udara**
st.subheader("🌦️ Hubungan Cuaca dengan Polusi Udara")

# Faktor cuaca yang bisa dipilih
weather_factors = ["TEMP", "PRES", "DEWP", "RAIN"]
factor = st.selectbox("🔍 Pilih Faktor Cuaca", weather_factors, index=0)

# Reset index agar tidak ada duplikasi indeks dan pastikan tidak ada NaN
cleaned_df = combined_df.reset_index().dropna(subset=[factor, pollutant])

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x=cleaned_df[factor], y=cleaned_df[pollutant], hue=cleaned_df["Lokasi"], alpha=0.5, ax=ax)

ax.set_xlabel(factor)
ax.set_ylabel(pollutant)
ax.set_title(f"Korelasi antara {factor} dan {pollutant}")

st.pyplot(fig)

# **3. Visualisasi Geospasial**
st.subheader("🌍 Visualisasi Geospasial Polusi Udara")

# Buat peta dasar di tengah Beijing
m = folium.Map(location=[39.9042, 116.4074], zoom_start=12, tiles="OpenStreetMap")

# Pastikan hanya baris dengan data lokasi yang valid
geo_df = combined_df.dropna(subset=['latitude', 'longitude', 'PM2.5'])

# Tambahkan HeatMap berdasarkan PM2.5
heat_data = geo_df[['latitude', 'longitude', 'PM2.5']].values.tolist()
HeatMap(heat_data).add_to(m)

# Tampilkan peta di Streamlit
st_folium(m, width=700, height=500)


# **4. Heatmap Korelasi**
st.subheader("📊 Matriks Korelasi Polutan dan Faktor Cuaca")
correlation_matrix = combined_df[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3", "TEMP", "PRES", "DEWP", "RAIN"]].corr()

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
st.pyplot(fig)

st.caption('📌 Copyright © 2025')
