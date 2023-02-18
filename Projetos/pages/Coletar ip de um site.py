import streamlit as st 
import components as cp


st.markdown("## Pegar ip de um site")
st.text("Digite o endreço do site para conseguir o ip")
site = st.text_input("Site: ")
confirm_button = st.button("Ok")

if confirm_button:
    st.write(cp.ip_target(site))
    st.write(cp.ping_target(site))
    st.write(cp.who_is(site))