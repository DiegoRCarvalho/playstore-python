from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

def carregar_dados():
    df = pd.read_csv("assets/playstore.csv", sep=",", decimal=".")
    return df

@app.route('/dados', methods=['GET'])
def obter_dados():
    df = carregar_dados()
    dados_json = df.to_dict(orient='records')
    return jsonify(dados_json)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)