import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_URL = 'http://localhost:5000/dados'

class ModeloPlaystore:
    @staticmethod
    def obter_dados():
        response = requests.get(API_URL)
        if response.status_code == 200:
            dados = response.json()
            df = pd.DataFrame(dados)
            return df
        else:
            st.error("Erro ao obter dados da API.")
            return pd.DataFrame()
        
    dados = obter_dados()

    if dados is not None:
        st.title("Distribuição de Avaliações por Categoria")
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=dados, x='Category', y='Rating')
        plt.xticks(rotation=90)
        plt.title('Distribuição de Avaliações por Categoria')
        st.pyplot(plt)

class VisualizacaoPlaystore:
    @staticmethod
    def exibir_tabela(dados):
        st.write("Top 10 Apps por Rating:")
        st.dataframe(dados)

class ControladorPlaystore:
    @staticmethod
    def executar_aplicacao():
        dados = ModeloPlaystore.obter_dados()
        if not dados.empty:
            categoria = st.selectbox("Selecione uma Categoria", options=dados['Category'].unique())
            dados_filtrados = dados[dados['Category'] == categoria].sort_values(by='Rating', ascending=False).head(10)
            VisualizacaoPlaystore.exibir_tabela(dados_filtrados)

if __name__ == "__main__":
    st.title("Aplicativo Streamlit com API Flask")
    controlador = ControladorPlaystore()
    controlador.executar_aplicacao()