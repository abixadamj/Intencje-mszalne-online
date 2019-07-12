from flask import Flask

app = Flask(__name__)

@app.route('/')
def start():
    tekst = '''
    <h1> hello </h1> <hr>
    tutaj moja pierwsza strona - Adam
    '''
    return tekst

@app.route('/<name>')
def start2(name):
    tekst = '''
    <h1> hello </h1> <hr>
    tutaj moja pierwsza strona - Adaś <hr>
    '''
    tekst = tekst + str(name)

    return tekst