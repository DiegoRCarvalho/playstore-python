# Projeto utilizando o Streamlit para demonstrar dados sobre a Playstore

Este é um projeto criado para demonstrar dados sobre a Playstore. 

## Descrição

Este projeto utiliza o Streamlit para criar uma aplicação web interativa que permite a seleção de ####### a partir de um conjunto de dados #######. O objetivo é processar os uma base de dados e gerar dashboards.

## Estrutura do Projeto

```.
├── assets
│ └── Google-Playstore.csv
│ └── playstore.csv
├── controller
│ └── controller.py
├── model
│ └── model.py
├── view
│ └── view.py
├── .gitignore
├── app.py
├── converter_base_de_dados.py
├── main.py
├── LICENSE
└── README.md
```

- **assets/playstore.csv**: Arquivo CSV contendo os dados da playstore.
- **controller/controller.py**: Contém a classe `ControladorPlaystore` que coordena as operações entre o modelo e a visualização.
- **model/model.py**: Contém a classe `ModeloPlaystore` que lida com o carregamento e processamento dos dados.
- **view/view.py**: Contém a classe `VisualizacaoPlaystore` que gera as visualizações dos dados.
- **app.py**: Cria a API utilizando o Flask.
- **converter_base_de_dados.py**: Cria uma nova base de dados apenas com os apps mais instalados.
- **README.md**: Documento explicativo do projeto.

## Instalação

1. Clone o repositório:

    ```bash
      git clone https://github.com/DiegoRCarvalho/playstore-python
      cd playstore-python
    ```

2. Crie um ambiente virtual e ative-o:

    ### Criar ambiente Virtual

      ```bash
        python3 -m venv venv
      ```

    ### Ativar no Linux e Mac
      ```bash
        source venv/bin/activate 
      ```
    ### Ativar no Windows
      ```bash
        venv\Scripts\activate
      ```

3. Instale as dependências:

    ```bash
    pip install plotly pandas plotly-express streamlit seaborn matplotlib flask
    ```

4. [Clique aqui](https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps) para baixar a base de dados.

5. Extraia o arquivo Google-Playstore.csv.zip

6. Copie o arquivo **Google-Playstore.csv** para dentro do diretório assets, localizado dentro do projeto.

7.  Dentro do diretório principal da aplicação, rode o comando abaixo para gerar uma nova base de dados chamada **playstore.csv**, ela conterá apenas os 50.000 apps mais instalados da base de dados, limitando o tamanho da base original, conseguimos impedir travamentos por falta de memória.
    ```
    python3 converter_base_de_dados.py
    ```

## Executando a Aplicação

1. Certifique-se de que o arquivo playstore.csv está no diretório assets.

2. Em um terminal, inicie a API com o seguinte comando:

    ```python
    python3 app.py
    ```

3. Em outro terminal, execute o script main.py com o Streamlit:

    ```python
    streamlit run main.py
    ```

4. Acesse a aplicação no seu navegador através do endereço indicado pelo Streamlit (geralmente <http://localhost:8501>).

## Exemplo de Uso

A aplicação apresenta opção para seleção de categoria de app que irá obter informação automaticamente da API. 
