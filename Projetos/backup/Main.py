import streamlit as st
import components as cp

st.header("PENTEST TOOLS")
st.write("BETA 1.0")

# Sidebar
st.sidebar.text("Ferramentas")

ip = st.sidebar.button("Pegar ip de um site",key="ip")
praga = st.sidebar.button("Praga Virtual")
st.sidebar.button("Pentest Wireless")
st.sidebar.button("Scan de redes")
st.sidebar.button("Criptografar um arquivo")
st.sidebar.button("Criar Engenharia Social")
st.sidebar.button("Gerar wordlist personalizada")

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

def callback():
    st.session_state.button_clicked = True

def page_ip():
    targ = st.text_input("site")
    button_ip = st.button("Pegar ip", on_click=callback)
    if button_ip or st.session_state.button_clicked:
        st.write(cp.ip_target(targ))
    
def praga():
    targ2 = st.text_input("Praga")

if ip:
    page_ip()