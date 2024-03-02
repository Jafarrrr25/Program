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
    day_count_user = data_day['weekday'].value_counts()
    hour_count_user = data_hour['weekday'].value_counts()

    # Menyamakan indeks dengan reindex()
    day_count_user = day_count_user.reindex(hour_count_user.index, fill_value=0).astype(int)

    total = day_count_user + hour_count_user

    # BUat plot
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=total.index, y=total.values, palette='viridis')

    # Menambahkan judul dan label sumbu
    plt.title('Customer List by Day', fontsize=16)
    plt.xlabel('Weather Conditions', fontsize=12)
    plt.ylabel('Customer', fontsize=12)

    # Menambahkan label angka di atas setiap bar
    for i, count in enumerate(total.values):
        plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12)
    
    st.pyplot(plt)
    
elif option == 'Bulanan':
    st.write('Ini adalah halaman tentang kami.')
    monthD_count_user = data_day['month'].value_counts().astype(int)
    monthH_count_user = data_hour['month'].value_counts().astype(int)

    total_month = monthD_count_user + monthH_count_user

    # BUat plot
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=total_month.index, y=total_month.values, palette='viridis')

    # Menambahkan judul dan label sumbu
    plt.title('Customer List by Month', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Customer', fontsize=12)

    # Menambahkan label angka di atas setiap bar
    for i, count in enumerate(total_month.values):
        plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12)
    
    st.pyplot(plt)

elif option == 'Jam':
    st.write('Silakan hubungi kami di sini.')
    hour_count = data_hour['hour'].value_counts().astype(int)

    # BUat plot
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=hour_count.index, y=hour_count.values, palette='viridis')

    # Menambahkan judul dan label sumbu
    plt.title('Customer List by Hour', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Customer', fontsize=12)

    # Menambahkan label angka di atas setiap bar
    for i, count in enumerate(hour_count.values):
        plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12)
    
    st.pyplot(plt)