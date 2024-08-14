import streamlit as st


st.set_page_config(
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Player",players)


player_stats = df_data[df_data["Name"] == player].iloc[0]
st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"__Clube__: {player_stats['Name']}")
st.markdown(f"__Posição__: {player_stats['Position']}")


col1,col2,col3,col4 = st.columns(4)
col1.markdown(f"__Idade__: {player_stats['Age']}")
col2.markdown(f"__Altura__: {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"__Peso__: {player_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

col1,col2,col3,col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"{player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"{player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"{player_stats['Release Clause(£)']:,}")



