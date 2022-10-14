import streamlit as st
import pandas as pd

def main_page():
    st.header("Monitoramento Capacidade SBC")
    st.sidebar.header("Filtros")

def oracle():
    st.header("Monitoramento SBC Oracle")
    st.text("Em desenvolvimento...")
    df = pd.read_csv("../input/oracle/oracle.csv")
    filters = df.style.highlight_max(subset=["Ocupação de CPU(%)","Ocupação de memória(%)"],color="red")


#------ FILTRO DE DATA & HORA ------------
    st.sidebar.header("Filtros")
    data_choice = st.sidebar.date_input("Data",key=df["Day"])

    st.sidebar.time_input("Hora: ",key=df["Hour"])


#------ FILTRO DE EQUIPAMENTO ------------
    user_options = st.sidebar.selectbox(
        "Equipamento: ",
        (df["Device"])
    )

    df_filtered = df.loc[df["Device"] == user_options]

    st.dataframe(df_filtered)


def huawei():
    st.header("Monitoramento SBC Huawei")
    st.text("Em desenvolvimento...")
def sonus():
    st.header("Monitoramento SBC Sonus")
    st.text("Em desenvolvimento...")

def genband():
    st.header("Monitoramento SBC Genband")
    st.text("Em desenvolvimento...")

pages = {
    "Página principal": main_page,
    "Oracle": oracle,
    "Huawei": huawei,
    "Genband": genband,
    "Sonus": sonus,
}

select_page = st.selectbox("Fabricante: ",pages.keys())
pages[select_page]()