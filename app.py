from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Thiago Carvalho | Ricardo Feu | Grupo - 24"

if __name__ == '__main__':
    app.run()