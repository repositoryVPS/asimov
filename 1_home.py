import streamlit as st
import webbrowser as wb
import pandas as pd
from datetime import datetime
import json


#CONFIGS
with open ('configs.json','r', encoding='utf-8') as arquivo:
    configs = json.load(arquivo)


if "data" not in st.session_state:
    df_data = pd.read_csv(configs["caminho_df_players_2023"], index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"]> 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data
    
    
st.markdown(configs["inicial_home"])
st.sidebar.markdown(configs["home_who"])

btn = st.button("Acesse os dados no Kaggle")
if btn:
    wb.open_new_tab("http://www.kaggle.com")


st.markdown("""
            Entre nessa dança!!
            
            """)

