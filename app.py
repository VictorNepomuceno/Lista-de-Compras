from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__, template_folder="templates")

produtos = []
lista = ["Frutas", "Carne", "Leite", "Ovos"]

@app.route("/")
def index():
   return render_template("index.html", produtos=produtos, lista=lista)

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar.html")

@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome_produto = request.form.get("nome_produto")
    produtos.append(nome_produto)
    print(produtos)
    return redirect(url_for("index"))

@app.route("/deletar/")
def deletar():
    produtos.pop()
    lista.pop()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

