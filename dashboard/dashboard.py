import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


data_day = pd.read_csv("data/cleaned_day.csv")
data_hour = pd.read_csv("data/cleaned_hour.csv")

#Dataframe
datetime_cols = ["date", "date"]
datetime_columns =["date", "date"]
data_day.sort_values(by="date", inplace=True)
data_day.reset_index(inplace=True)
for column in datetime_columns:
    data_day[column] = pd.to_datetime(data_day[column])

# Ini adalah contoh elemen-elemen yang bisa dimasukkan ke dalam sidebar
with st.sidebar:
    st.write("Pilih tampilan total pengunjung")
    option = st.selectbox('Pilih opsi:', ('Harian', 'Bulanan', 'Jam'))
    st.write('---')

# Bagian utama dari aplikasi Streamlit
st.title('Proyek Analisis Data')
st.write('Persewaan Sepeda pada tahun 2011-2012 ')

# Menampilkan hasil berdasarkan pilihan dari sidebar
if option == 'Harian':
    st.write(
        "Berikut merupakan grafik persewaan sepeda perhari:"
    )
    day_count_user = data_day['weekday'].value_counts()
    hour_count_user = data_hour['weekday'].value_counts()

    # Menyamakan indeks dengan reindex()
    day_count_user = day_count_user.reindex(hour_count_user.index, fill_value=0).astype(int).sort_index()

    total = day_count_user + hour_count_user

    # BUat plot
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 8))
    sns.barplot(x=total.index, y=total.values, palette='viridis')

    # Menambahkan judul dan label sumbu
    plt.title('Customer List by Day', fontsize=16)
    plt.xlabel('Day', fontsize=12)
    plt.ylabel('Customer', fontsize=12)

    # Menambahkan label angka di atas setiap bar
    for i, count in enumerate(total.values):
        plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12)
    
    st.pyplot(plt)
    st.write(
        "Berdasarkan grafik diatas, pengunjung paling banyak datang di hari Minggu, karena biasanya orang akan melakukan aktivitas yang santai pada hari Minggu untuk melepas penat."
    )
    
elif option == 'Bulanan':
    st.write(
        "Berikut merupakan grafik persewaan sepeda perbulannya:"
    )
    monthD_count_user = data_day['month'].value_counts().astype(int).sort_index()
    monthH_count_user = data_hour['month'].value_counts().astype(int).sort_index()

    total_month = monthD_count_user + monthH_count_user

    # BUat plot
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 8))
    sns.barplot(x=total_month.index, y=total_month.values, palette='viridis')

    # Menambahkan judul dan label sumbu
    plt.title('Customer List by Month', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Customer', fontsize=12)

    # Menambahkan label angka di atas setiap bar
    for i, count in enumerate(total_month.values):
        plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12)
    
    st.pyplot(plt)

    st.write(
        "Dapat dilihat bahwa bulan Mei dan Juli merupakan bulan yang paling banyak dikunjungi oleh penyewa sepeda dengan total pengunjung di masing-masing bulan adalah 1550 pengunjung. "
    )

elif option == 'Jam':
    st.write(
        "Berikut merupakan grafik persewaan sepeda perjam:"
    )
    hour_count = data_hour['hour'].value_counts().sort_index()

    # BUat plot
    sns.set_style("whitegrid")
    plt.figure(figsize=(14, 8))
    sns.barplot(x=hour_count.index, y=hour_count.values, palette='viridis')

    # Menambahkan judul dan label sumbu
    plt.title('Customer List by Hour', fontsize=16)
    plt.xlabel('Hour', fontsize=12)
    plt.ylabel('Customer', fontsize=12)

    # Menambahkan label angka di atas setiap bar
    for i, count in enumerate(hour_count.values):
        plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12)
    
    st.pyplot(plt)
    st.write(
        "Berdasarkan grafik diatas, terlihat bahwa jam 4-5 sore banyak pengunjung datang untuk menyewa sepeda. Sore hari merupakan waktu yang tepat untuk bersepeda"
    )