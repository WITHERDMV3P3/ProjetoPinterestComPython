#criar as rotas do site (links)

from flask import render_template, url_for
from pinterest import app
from flask_login import login_required

@app.route("/") # caminho do link do site e deve colocar o que deve ser colocado depois da barra do site tipo exemplo www.google.com/->br /// a / seria a rota principal do site
def homepage():
    return render_template("Paginainicial.html")  # o que voce quer passar na primeira pagina


@app.route("/perfil/<usuario>") #para criar link dinamico de diversos usuarios é só colocar entre <>
@login_required #adicionar novos atributos dentro de uma função e assim ela nao deixa qualquer pessoa acessar se não estiver logada
def perfil(usuario):
    return render_template("perfil.html", usuario = usuario) #passar parametro para a tela .html para lá no html ele possa pegar por exemplo o nome do usuario