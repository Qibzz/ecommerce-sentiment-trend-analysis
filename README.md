# E-Commerce Sentiment & Trend Analysis

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?logo=pandas)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

Proyek analisis sentimen dan tren pada data ulasan e-commerce, mencakup pipeline Data Engineering, Exploratory Data Analysis, dan model Machine Learning untuk klasifikasi sentimen.

---

## Latar Belakang

Di era e-commerce, ulasan pelanggan merupakan sumber data yang sangat berharga. Proyek ini menganalisis 2.500 review pengguna Shopee (Juli 2022 – April 2023) untuk memahami pola kepuasan pengguna, mengidentifikasi keluhan utama, dan memberikan rekomendasi berbasis data kepada tim produk.

---

# 🛒 E-Commerce Sentiment & Trend Analysis

Proyek ini merupakan sistem analisis end-to-end yang mencakup Data Engineering, Data Analysis, dan AI Modeling untuk memahami feedback pengguna pada platform E-Commerce.

## 📊 Dataset Specifications
| Atribut | Detail |
| :--- | :--- |
| **Sumber Data** | Google Play Store — Shopee ID |
| **Jumlah Data** | 2.500 reviews (balanced, 500/rating) |
| **Periode** | Juli 2022 – April 2023 |
| **Bahasa** | Bahasa Indonesia |
| **Kolom Utama** | `content`, `score`, `at`, `replyContent`, `thumbsUpCount` |

## 🛠️ Tools & Libraries
| Tool / Library | Kegunaan |
| :--- | :--- |
| **Python 3.10+** | Bahasa pemrograman utama |
| **Pandas & NumPy** | Data manipulation & cleaning |
| **Matplotlib & Seaborn** | Visualisasi data & insight |
| **WordCloud** | Visualisasi frekuensi kata pada ulasan |
| **Google Colab** | Environment eksekusi notebook |
| **Git & GitHub** | Version control dan portofolio |

## 🚀 Project Steps
1. **Data Engineering**: Handling missing values, cleaning text, dan structuring data.
2. **Data Analysis**: Eksplorasi tren rating dan visualisasi distribusi sentimen.
3. **AI Modeling**: Implementasi Natural Language Processing (NLP) untuk klasifikasi sentimen otomatis.

---

## Fitur Utama

- **Data Cleaning Pipeline**: Penanganan missing values, anomali response time, dan feature engineering dari kolom datetime.
- **EDA & Visualisasi**: Analisis distribusi rating, tren bulanan, word frequency, dan wordcloud menggunakan Matplotlib & Seaborn.
- **Topic Categorization** : Kategorisasi keluhan pengguna ke dalam topik (Performa Aplikasi, Pengiriman, SPayLater, dll) menggunakan keyword matching.
- **CS Response Analysis** : Analisis response rate dan median response time Customer Service per rating.
- **Insight Bisnis** Rekomendasi actionable berdasarkan temuan data
---

## Cara Menjalankan

1. Clone repo ini:
```bash
   git clone https://github.com/Qibzz/ecommerce-sentiment-trend-analysis.git
```
2. Upload dataset ke environment: data/Shopee_Sampled_Reviews.csv
3. Buka notebooks/ecommerce_analysis.ipynb di Google Colab
4. Jalankan semua cell secara berurutan

---


## Struktur Proyek

├── data/
│   └── Shopee_Sampled_Reviews.csv   # Dataset review Shopee (2.500 rows)
├── notebooks/
│   └── ecommerce_analysis.ipynb     # Notebook utama EDA
├── outputs/                         # Hasil visualisasi (PNG)
├── src/                             # Script pendukung (coming soon)
├── README.md
└── .gitignore     
