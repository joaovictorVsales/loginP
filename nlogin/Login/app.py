from flask import Flask, render_template, request, redirect, url_for, session, make_response

app = Flask(__name__)
app.secret_key = 'Chave-secreta'

USUARIO_CORRETO = 'Camilo'
SENHA_CORRETA = 'Huxiaobestship'


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    mensagem = ""

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if username == USUARIO_CORRETO and password == SENHA_CORRETA:
            resposta = make_response(redirect(url_for('bem_vindo')))
            resposta.set_cookie("username", username, max_age=60*10)
            session['username'] = username
            return resposta
        else:
            mensagem = "Usuário ou senha incorreta. Tente novamente."
            return render_template('login.html', error=mensagem)


@app.route('/bem_vindo')
def bem_vindo():
    username = request.cookies.get('username')
    if not username:
        username = session.get('username')

    if username:
        return render_template('bem_vindo.html', username=username)
    else:
        return redirect(url_for('home'))


@app.route('/produto')
def produto():
    produtos = ['Maçã', 'Banana', 'Laranja']
    username = request.cookies.get('username')
    if not username:
        username = session.get('username')

    if username:
        return render_template('produto.html', username=username, produtos=produtos)
    else:
        return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    resposta = make_response(redirect(url_for('home')))
    resposta.set_cookie('username', '', expires=0)
    return resposta


if __name__ == '__main__':
    app.run(debug=True)
