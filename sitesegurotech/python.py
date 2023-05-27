from .flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Processar o formulário de contato enviado pelo usuário
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']
        # Lógica adicional, como envio de e-mail ou salvamento no banco de dados
        return render_template('thankyou.html', nome=nome)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
