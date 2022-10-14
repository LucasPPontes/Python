import streamlit as st
import pandas as pd

def huawei():
    st.header("Monitoramento SBC Huawei")
    st.text("Em desenvolvimento...")

    df = pd.read_csv("input/huawei/huawei.csv")


#------ FILTRO DE DATA & HORA & EQUIPAMENTO ------------

    day_choice = st.sidebar.selectbox("Data: ",(df["Start Time"]).drop_duplicates())

    device_choice = st.sidebar.selectbox(
            "Equipamento: ",
            (df["NE Name"])
        )
    
    route_choice = st.sidebar.selectbox(
        "Rota:",(df[""])
    )

    df_data_filter = df.loc[(df["Start Time"] == day_choice)&(df["NE Name"] == device_choice)]

    filters_button = st.sidebar.button("Filtrar")

    if filters_button:
        st.dataframe(df_data_filter)
    else:
        pass
