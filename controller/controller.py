from model.model import ModeloPlaystore
from view.view import VisualizacaoPlaystore
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns



class ControladorPlaystore:
    def executar_aplicacao(self):
        dados = ModeloPlaystore.obter_dados()
        visualizacao = VisualizacaoPlaystore()
        
        if not dados.empty:
            
            st.subheader("Informações sobre apps de acordo com sua categoria.")
            categoria_selecionada = visualizacao.selecionar_categoria(dados)
            categoria_filtrada = dados[dados['Category'] == categoria_selecionada]
            
            visualizacao.exibir_tabela(categoria_filtrada)
            visualizacao.exibir_mensagem(f"Total de Apps Gratuitos e Pagos da categoria: {categoria_selecionada}")
            visualizacao.exibir_contagem_apps(categoria_filtrada)
            visualizacao.exibir_mensagem(f"Total de Apps com ou sem anúncios da categoria: {categoria_selecionada}")
            visualizacao.exibir_contagem_ads(categoria_filtrada)
            
            visualizacao.exibir_mensagem(f"### Porcentagem de Apps por Faixa Etária")
            porcentagem_faixa_etaria = (dados['Content Rating'].value_counts(normalize=True) * 100).sort_values()

            fig, ax = plt.subplots(figsize=(10, 6))  # Ajuste o tamanho conforme necessário
            ax.barh(porcentagem_faixa_etaria.index, porcentagem_faixa_etaria, color='#4682B4')
            ax.set_xlabel("Porcentagem (%)")
            ax.set_title("Distribuição de Apps por Faixa Etária")
            
            for i, v in enumerate(porcentagem_faixa_etaria):
                ax.text(v + 0.5, i, f"{v:.1f}%", va='center')

            st.pyplot(fig)

            
            top_apps = dados.sort_values(by='Maximum Installs', ascending=False).head(10)
            st.title("Top 10 Aplicativos mais Baixados")
            st.dataframe(top_apps[['App Name', 'Category', 'Maximum Installs']])
            
            
            st.title("Distribuição de Aplicativos Pagos vs. Gratuitos por Categoria")
            pagos_gratuitos = dados.groupby(['Category', 'Free']).size().unstack().fillna(0)
            pagos_gratuitos.plot(kind='bar', stacked=True, figsize=(12, 6))
            plt.title("Aplicativos Pagos vs. Gratuitos por Categoria")
            plt.ylabel("Número de Apps")
            st.pyplot(plt)
            
            
            st.title("Correlação entre Avaliação e Instalações")
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=dados, x='Rating', y='Maximum Installs', hue='Category', alpha=0.6)
            plt.title("Avaliação vs. Instalações")
            plt.xlabel("Rating")
            plt.ylabel("Máximo de Instalações")
            st.pyplot(plt)
            
            
            st.title("Distribuição de Aplicativos por Faixa Etária")
            faixa_etaria = dados['Content Rating'].value_counts(normalize=True) * 100
            faixa_etaria.plot(kind='barh', figsize=(10, 6), color='skyblue')
            plt.title("Percentual de Apps por Faixa Etária")
            plt.xlabel("Porcentagem (%)")
            plt.ylabel("Content Rating")
            st.pyplot(plt)
            
        else:
            visualizacao.exibir_mensagem("Erro ao carregar os dados.")