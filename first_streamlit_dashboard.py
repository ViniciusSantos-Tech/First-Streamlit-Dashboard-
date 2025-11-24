#𝗙𝗘𝗜𝗧𝗢 𝗣𝗢𝗥 𝗩𝗜𝗡𝗜𝗖𝗜𝗨𝗦 𝗦𝗔𝗡𝗧𝗢𝗦-𝗧𝗘𝗖𝗛


import streamlit as st
import pandas as pd
import plotly.express as px  

st.title('Minha primeira pagina Streamlit!')
st.set_page_config(
    page_title="Minha Primeira Página",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"

)
st.header('Um simples Grafico de Demostraçao!')
st.text('Veja meu Github!')
st.html(' <a href="https://github.com/ViniciusSantos-Tech">𝐡𝐭𝐭𝐩𝐬://𝐠𝐢𝐭𝐡𝐮𝐛.𝐜𝐨𝐦/𝐕𝐢𝐧𝐢𝐜𝐢𝐮𝐬𝐒𝐚𝐧𝐭𝐨𝐬-𝐓𝐞𝐜𝐡</a>')

dados = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro', 'Carla'],
    'Idade': [25, 30, 22, 35, 28],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Porto Alegre'],
    'Salário': [5000, 7000, 4500, 8000, 6000]
}

df = pd.DataFrame(dados)
st.dataframe(df)
st.markdown('Isso é uma tabela criada usando **st.table(df)**')

fig = px.bar(df, x='Nome', y='Salário', 
             title='Salário por Nome',
             color='Salário',
             color_continuous_scale='blues')


st.plotly_chart(fig)
st.markdown('Isso é um gráfico de barras criado usando **plotly.express**',)
