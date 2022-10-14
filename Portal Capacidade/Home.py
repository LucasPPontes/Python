import streamlit as st
import pandas as pd

import pages.provider.oracle as Oracle
import pages.provider.genband as Genband
import pages.provider.huawei as Huawei
import pages.provider.sonus as Sonus

st.header("Monitoramento Capacidade SBC")
st.sidebar.header("Filtros")

user_choice = st.selectbox("Fabricante:",("Oracle","Huawei","Sonus","Genband"))

if user_choice == "Oracle":
    Oracle.oracle()
elif user_choice == "Huawei":
    Huawei.huawei()
elif user_choice == "Sonus":
    Sonus.sonus()
elif user_choice == "Genband":
    Genband.genband()