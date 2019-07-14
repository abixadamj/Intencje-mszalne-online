from flask import Flask, jsonify, request, url_for, redirect, session, render_template


app = Flask(__name__)

# zmienne konfiguracyjne
# app.config['DEBUG'] = True
# app.config['TESTING'] = True

#lub lepiej:

app.config.update(
    TESTING=True,
    DEBUG=True,
    SECRET_KEY=b'_5#y23478659283746592374dsfgsdf2L"F4Q8z\n\xec]/'
)


@app.route('/')
def start():
    # TODO Coś tu ładnego zrobić
    return render_template('intencje_mszalne.html')


@app.route('/login', methods = ['POST'])
def login():
    login = request.form['login']
    haslo = request.form['haslo']
    # FIXME chyba brakuje sprawdzania w bazie
    session['login'] = login
    return render_template('intencje_mszalne_login.html', nazwa=login)

if __name__ == "__main__":
    app.run()