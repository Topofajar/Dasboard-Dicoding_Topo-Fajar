#!/usr/bin/env python
# coding: utf-8

# # Library

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import datetime
sns.set(style='dark')


# # Data Frame

# ## All Data

# In[2]:


all_data = pd.read_csv("https://raw.githubusercontent.com/Topofajar/Proyek-Analisis-Data-Air-Quality-Dataset/main/all_data%20(5).csv")
all_data.tail()


# In[ ]:


# Mengurutkan all_data berdasarkan date time
all_data.sort_values(by="datetime", inplace=True)
all_data.reset_index(inplace=True)
all_data.head(10)


# # Data Frame Total Polutaan

# In[ ]:


def create_df_total_polutan(data) :
    df_total_polutan = data.groupby(['year','station']).sum()
    df_total_polutan.reset_index(inplace=True)
    df_total_polutan = pd.melt(df_total_polutan, id_vars=['year', 'station'], value_vars=['PM2.5', 'PM10'],
                        var_name='pollutant', value_name='sum_value')
    return df_total_polutan


# In[ ]:


df_total_polutan = create_df_total_polutan(all_data)


# ## Data Frame Tren PM2.5 dan PM10

# In[ ]:


month_tren_df = all_data[(all_data["datetime"] >= "2017-02-01 02:00:00") & 
                (all_data["datetime"] <= "2017-02-28 02:00:00")]
week_tren_df = all_data[(all_data["datetime"] >= "2017-02-21 02:00:00") & 
                (all_data["datetime"] <= "2017-02-28 02:00:00")]


# # Komponen Filter

# In[ ]:


with st.sidebar:
    # Menambahkan logo
    st.image("https://raw.githubusercontent.com/Topofajar/Proyek-Analisis-Data-Air-Quality-Dataset/main/air pollution logo.jpg")

    # Feedback
    text = st.text_area("Bagaimana perasaan Anda terhadap polusi di lingkungan Anda?")
    st.write(text)
    


# # Pembuatan Dashboard

# ## Tren Polutan PM2.5 & PM10

# In[ ]:


def tren_PM25 ():
    st.subheader('Treen Polutan PM2.5 Bulan Februari 2017')
    col1, col2 = st.columns(2)

    with col1:
        total_pol = month_tren_df['PM2.5'].sum()
        st.metric("Total Polutan", value=round(total_pol, 2))

    with col2:
        mean_pol = month_tren_df['PM2.5'].mean()
        st.metric("Rata-Rata Polutan", value=round(mean_pol, 2))

    Bulanan = st.checkbox('Report PM2.5 satu bulan terakhir')
    Mingguan = st.checkbox('Report PM2.5 satu minggu terakhir')

    if Bulanan:
        fig, ax = plt.subplots(figsize=(12, 5))

        # Plot setiap stasiun
        colors = ['red','blue', 'green']
        for i,loc in zip((1,2,3),["Aotizhongxin", "Dingling", "Changping"]):
            filtered_df = month_tren_df[month_tren_df['station'] == loc]
            ax.plot(filtered_df['datetime'], filtered_df['PM2.5'], label=loc, color=colors[i % len(colors)])

        # Menambahkan judul dan label sumbu
        ax.set_title('Tren Konsentrasi PM2.5 Bulan Februari 2017')
        ax.set_xlabel('Tanggal', size=13)
        ax.set_ylabel('Konsentrasi PM10 (ug/m^3)', size=13)
        ax.legend()

        # Menampilkan grafik di Streamlit
        st.pyplot(fig)

    if Mingguan:
        fig, ax = plt.subplots(figsize=(12, 5))

        # Plot setiap stasiun
        colors = ['red','blue', 'green']
        for i,loc in zip((1,2,3),["Aotizhongxin", "Dingling", "Changping"]):
            filtered_df = week_tren_df[week_tren_df['station'] == loc]
            ax.plot(filtered_df['datetime'], filtered_df['PM2.5'], label=loc, color=colors[i % len(colors)])

        # Menambahkan judul dan label sumbu
        ax.set_title('Tren Konsentrasi PM2.5 Minggu Ini')
        ax.set_xlabel('Tanggal', size=13)
        ax.set_ylabel('Konsentrasi PM10 (ug/m^3)', size=13)
        ax.legend()

        # Menampilkan grafik di Streamlit
        st.pyplot(fig)


# In[ ]:


def tren_PM10():
    st.subheader('Treen Polutan PM10 Bulan Februari 2017')
    col1, col2 = st.columns(2)

    with col1:
        total_pol = month_tren_df['PM10'].sum()
        st.metric("Total Polutan", value=round(total_pol, 2))

    with col2:
        mean_pol = month_tren_df['PM10'].mean()
        st.metric("Rata-Rata Polutan", value=round(mean_pol, 2))

    Bulanan1 = st.checkbox('Report PM10 satu bulan terakhir')
    Mingguan1 = st.checkbox('Report PM10 satu minggu terakhir')

    if Bulanan1:
        fig, ax = plt.subplots(figsize=(12, 5))

        # Plot setiap stasiun
        colors = ['red','blue', 'green']
        for i,loc in zip((1,2,3),["Aotizhongxin", "Dingling", "Changping"]):
            filtered_df = month_tren_df[month_tren_df['station'] == loc]
            ax.plot(filtered_df['datetime'], filtered_df['PM10'], label=loc, color=colors[i % len(colors)])

        # Menambahkan judul dan label sumbu
        ax.set_title('Tren Konsentrasi PM10 Bulan Februari 2017')
        ax.set_xlabel('Tanggal', size=13)
        ax.set_ylabel('Konsentrasi PM10 (ug/m^3)', size=13)
        ax.legend()

        # Menampilkan grafik di Streamlit
        st.pyplot(fig)

    if Mingguan1:
        fig, ax = plt.subplots(figsize=(12, 5))

        # Plot setiap stasiun
        colors = ['red','blue', 'green']
        for i,loc in zip((1,2,3),["Aotizhongxin", "Dingling", "Changping"]):
            filtered_df = week_tren_df[week_tren_df['station'] == loc]
            ax.plot(filtered_df['datetime'], filtered_df['PM10'], label=loc, color=colors[i % len(colors)])

        # Menambahkan judul dan label sumbu
        ax.set_title('Tren Konsentrasi PM10 Minggu Ini')
        ax.set_xlabel('Tanggal', size=13)
        ax.set_ylabel('Konsentrasi PM10 (ug/m^3)', size=13)
        ax.legend()

        # Menampilkan grafik di Streamlit
        st.pyplot(fig)


# In[ ]:


def tren_tahunan():
    st.subheader('Pantauan Polusi Udara Tahunan')
    st.subheader('Pilih Kota :')

    Aotizhongxin = st.checkbox('Aotizhongxin')
    Dingling = st.checkbox('Dingling')
    Changping = st.checkbox('Changping')

    if Aotizhongxin:
        fig, ax = plt.subplots(figsize=(12, 5))
        filtered_df = df_total_polutan[df_total_polutan['station'] == "Aotizhongxin"]
        sns.barplot(data=filtered_df, x="year", y="sum_value", hue="pollutant", ax=ax, errwidth=0)

        # Menambahkan judul dan label sumbu
        ax.set_title('Total Polutan per tahun di Aotizhongxin')
        ax.set_xlabel('Tanggal', size=13)
        ax.set_ylabel('Total Konsentrasi PM10 (ug/m^3)', size=13)
        ax.legend()

        # Menampilkan grafik di Streamlit
        st.pyplot(fig)
        
    if Dingling:
        fig, ax = plt.subplots(figsize=(12, 5))
        filtered_df = df_total_polutan[df_total_polutan['station'] == "Dingling"]
        sns.barplot(data=filtered_df, x="year", y="sum_value", hue="pollutant", ax=ax, errwidth=0)

        # Menambahkan judul dan label sumbu
        ax.set_title('Total Polutan per tahun di Dingling')
        ax.set_xlabel('Tanggal', size=13)
        ax.set_ylabel('Total Konsentrasi PM10 (ug/m^3)', size=13)
        ax.legend()

        # Menampilkan grafik di Streamlit
        st.pyplot(fig)
        
    if Changping:
        fig, ax = plt.subplots(figsize=(12, 5))
        filtered_df = df_total_polutan[df_total_polutan['station'] == "Changping"]
        sns.barplot(data=filtered_df, x="year", y="sum_value", hue="pollutant", ax=ax, errwidth=0)

        # Menambahkan judul dan label sumbu
        ax.set_title('Total Polutan per tahun di Changping')
        ax.set_xlabel('Tanggal', size=13)
        ax.set_ylabel('Total Konsentrasi PM10 (ug/m^3)', size=13)
        ax.legend()

        # Menampilkan grafik di Streamlit
        st.pyplot(fig)


# ## Tab

# In[ ]:


st.title('Pantauan Polusi Udara')
tab1, tab2, tab3 = st.tabs(["Tren PM2.5", "Tren PM10", "Tren Tahunan"])
 
with tab1:
    tren_PM25()
with tab2:
    tren_PM10() 
with tab3:
    tren_tahunan()

