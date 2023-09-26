import requests
from flask import Flask, request, render_template

def simular_emprestimo(montante, periodo_meses):
    url = 'https://api-do-banco.com/simulacao-emprestimo'
    params = {
        'montante': montante,
        'periodo_meses': periodo_meses,
        'taxa_juros': 0.1,  # Taxa de juros de 10% (valor fictício)
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            resultado = response.json()
            return resultado
        else:
            print(f"Erro na API do Banco: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na conexão com a API do Banco: {e}")
        return None


montante_emprestimo = 10000
periodo_meses_emprestimo = 12

resultado_simulacao = simular_emprestimo(montante_emprestimo, periodo_meses_emprestimo)

if resultado_simulacao:
    print(f"Valor das parcelas: R${resultado_simulacao['valor_parcela']:.2f}")
    print(f"Total a pagar: R${resultado_simulacao['total_pagar']:.2f}")
else:
    print("Simulação indisponível no momento.")

app = Flask(__name__)


def simular_emprestimo(montante, periodo_meses):
   
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            montante_emprestimo = float(request.form['montante'])
            periodo_meses_emprestimo = int(request.form['periodo_meses'])
            resultado_simulacao = simular_emprestimo(montante_emprestimo, periodo_meses_emprestimo)

        if resultado_simulacao:
            return render_template('resultado_simulacao.html', resultado=resultado_simulacao)
        else:
            return "Simulação indisponível no momento."

    return render_template('formulario_simulacao.html')

if __name__ == '__main__':
    app.run(debug=True)
    


