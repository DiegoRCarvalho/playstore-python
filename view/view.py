import streamlit as st
import matplotlib.pyplot as plt

class VisualizacaoPlaystore:
    def exibir_tabela(self, dados):
        st.write("Top 10 Aplicativos da Categoria Selecionada (Baseado no Rating):")
        dados_ordenados = dados.sort_values(by='Rating', ascending=False).head(10)
        st.dataframe(dados_ordenados)

    def exibir_mensagem(self, mensagem):
        st.write(mensagem)
        
    def selecionar_categoria(self, dados):
        categorias = dados['Category'].unique()
        categoria_selecionada = st.selectbox("Selecione uma Categoria", categorias)
        return categoria_selecionada

    def exibir_contagem_apps(self, dados):
        contagem = dados['Free'].value_counts().rename(index={True: 'Gratuito', False: 'Pago'})
        st.table(contagem)

        fig, ax = plt.subplots(figsize=(5, 2))
        ax.pie(contagem, labels=contagem.index, autopct='%1.1f%%', startangle=90, colors=['#4682B4', '#dcd9de'])
        ax.axis('equal')

        st.pyplot(fig)
        
    def exibir_contagem_ads(self, dados):
        contagem = dados['Ad Supported'].value_counts().rename(index={True: 'Com Anúncio', False: 'Sem Anúncio'})
        st.table(contagem)

        fig, ax = plt.subplots(figsize=(5, 2))
        ax.pie(contagem, labels=contagem.index, autopct='%1.1f%%', startangle=90, colors=['#4682B4', '#dcd9de'])
        ax.axis('equal')

        st.pyplot(fig)
        
    