# E-Commerce Sentiment & Trend Analysis

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?logo=pandas)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

Proyek analisis sentimen dan tren pada data ulasan e-commerce, mencakup pipeline Data Engineering, Exploratory Data Analysis, dan model Machine Learning untuk klasifikasi sentimen.

---

## Latar Belakang

Di era e-commerce, ulasan pelanggan merupakan sumber data yang sangat berharga. Proyek ini membangun pipeline end-to-end mulai dari pengumpulan dan pembersihan data, eksplorasi tren, hingga prediksi sentimen secara otomatis menggunakan Machine Learning.

---

## Tujuan Proyek

- Membangun pipeline pembersihan data yang robust menggunakan Pandas
- Menganalisis distribusi rating dan korelasi harga-rating per kategori
- Melatih model klasifikasi sentimen berbasis TF-IDF + Naive Bayes
- Menyajikan insight bisnis yang actionable dari data ulasan

---

## Fitur Utama

- **Data Cleaning Pipeline**: Automasi penanganan data duplikat dan nilai kosong (null values).
- **Trend Visualization**: Analisis korelasi harga vs kepuasan pelanggan dengan Seaborn.
- **Sentiment Engine**: Model klasifikasi teks dengan akurasi tinggi menggunakan pendekatan TF-IDF.
2. Tambahkan Folder Structure

---

## Cara Menjalankan

1. Clone repo ini:
```bash
   git clone https://github.com/Qibzz/ecommerce-sentiment-trend-analysis.git
```
2. Buka `notebooks/ecommerce_analysis.ipynb` di Google Colab
3. Jalankan semua cell secara berurutan

---


## Struktur Proyek

```text
├── data/           # Dataset simulasi/mentah
├── notebooks/      # Google Colab / Jupyter Notebooks
├── src/            # Script Python pendukung
├── README.md       # Dokumentasi proyek
└── .gitignore      # File yang diabaikan oleh Git
