import streamlit as st
import pandas as pd
import plotly.express as px

dataset = pd.read_csv("/home/scotuzzi/scotuzzi/lab/python/futebol/brasileiro/campeonato-brasileiro-full.csv")
dataset.drop(columns=["formacao_mandante", "formacao_visitante", "tecnico_mandante", "tecnico_visitante"], inplace=True)
# print(dataset.loc[dataset['mandante'] == 'Guarani'])

st.set_page_config(layout='wide')

mandante = st.sidebar.selectbox(
    "Time da casa",
    (dataset['mandante'].unique())
)

visitante = st.sidebar.selectbox(
    "Time visitante",
    (dataset['visitante'].unique())
)

st.title("Análise das partidas")

st.write("Gols por partida")
st.bar_chart(dataset.loc[(dataset['mandante'] == mandante) & (dataset['visitante'] == visitante)][['mandante_placar', 'visitante_placar']])

st.write("Vitórias e empates")
resultado = dataset.loc[(dataset['mandante'] == mandante) & (dataset['visitante'] == visitante)]
vitoriasMandante = len(resultado.loc[resultado['vencedor'] == mandante])
vitoriasVisitante = len(resultado.loc[resultado['vencedor'] == visitante])
empates = len(resultado) - (vitoriasVisitante + vitoriasMandante)

pieDf = pd.DataFrame([[mandante, vitoriasMandante], [visitante, vitoriasVisitante], ['Empate', empates]], columns=['time_vencedor', 'quantidade'])

fig = px.pie(pieDf, values='quantidade', names='time_vencedor')
st.write(fig)

st.write("Painel detalhado")
st.dataframe(dataset.loc[(dataset['mandante'] == mandante) & (dataset['visitante'] == visitante)])
