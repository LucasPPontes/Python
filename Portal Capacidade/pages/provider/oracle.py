from ast import arg
import streamlit as st
import pandas as pd


def oracle():
    st.header("Monitoramento SBC Oracle")
    st.text("Em desenvolvimento...")
    df = pd.read_csv("input/oracle/oracle.csv")
    #filters = df.style.highlight_max(subset=["Ocupação de CPU(%)","Ocupação de memória(%)"],color="red")


#------ FILTRO DE DATA & HORA & EQUIPAMENTO ------------
    day_choice = st.sidebar.selectbox("Data: ",(df["Day"]).drop_duplicates())
    hour_choice = st.sidebar.selectbox("Hora: ",(df["Hour"]).drop_duplicates())
    
    device_choice = st.sidebar.selectbox(
        "Equipamento: ",
        (df["Device"])
    )

#------ FILTRO DE EQUIPAMENTO ------------
    

    df_data_filter = df.loc[(df["Day"] == day_choice)&(df["Hour"] == hour_choice)&(df["Device"] == device_choice)]

    filters_button = st.sidebar.button("Filtrar")

    if filters_button:
        st.dataframe(df_data_filter)
    else:
        st.dataframe(df)

    clear_filters = st.sidebar.button("Limpar filtros")
    
    


    