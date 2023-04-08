from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/consulta")
def consulta():
    url = 'https://lhfoc56a5ww3gwwznvo5bexktq0mmzms.lambda-url.us-east-1.on.aws/v1'
    max_attempts = 3  # número máximo de tentativas
    attempts = 0  # contador de tentativas
    data = None  # inicializar a variável de dados

    while attempts < max_attempts:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            break  # sai do loop se a solicitação tiver sucesso
        attempts += 1

    if data is not None:
        return render_template('consulta.html', data=data)
    else:
        return 'Erro ao obter dados da API após {} tentativas'.format(max_attempts)
       

if __name__ == "__main__":
    app.run(debug=True)
