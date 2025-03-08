# Air Quality Dashboard

Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis data kualitas udara dari berbagai lokasi.

## 📌 Cara Menjalankan Dashboard

### 1️⃣ Instalasi Dependensi
Sebelum menjalankan aplikasi, pastikan Anda telah menginstal dependensi yang diperlukan. Jalankan perintah berikut:
```bash
pip install -r requirements.txt
```
Jika tidak ada file `requirements.txt`, instal paket secara manual:
```bash
pip install streamlit pandas matplotlib seaborn
```

### 2️⃣ Menjalankan Dashboard
Gunakan perintah berikut untuk menjalankan aplikasi:
```bash
streamlit run dashboard.py
```

### 3️⃣ Interaksi dengan Dashboard
- Pilih **lokasi** (Aotizhongxin atau Dongsi) untuk melihat data spesifik.
- Pilih **jenis polutan** (PM2.5, PM10, SO2, NO2, CO, O3) untuk analisis tren.
- Gunakan **tab** untuk melihat **tren polusi udara**, **korelasi antar polutan**, dan **ringkasan statistik**.

## 📂 Struktur File
```
submission
├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───data_1.csv
| └───data_2.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt
```

## ℹ️ Catatan
- Pastikan file data **PRSA_Data_Aotizhongxin.csv** dan **PRSA_Data_Dongsi.csv** ada dalam direktori yang sesuai.
- Gunakan Python versi **3.7 atau lebih baru** agar Streamlit berjalan dengan baik.

🚀 **Selamat menganalisis kualitas udara!**

