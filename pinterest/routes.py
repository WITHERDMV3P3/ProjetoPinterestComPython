#criar as rotas do site (links)

from flask import render_template, url_for, redirect
from pinterest import app, database,bcrypt
from flask_login import login_required, login_user, logout_user,current_user
from pinterest.forms import Formulariologin,FormularioCriarConta
from pinterest.models import Usuario, Foto


@app.route("/", methods = ["GET","POST"]) # caminho do link do site e deve colocar o que deve ser colocado depois da barra do site tipo exemplo www.google.com/->br /// a / seria a rota principal do site
def homepage():
    formulacriologin = Formulariologin() # isso é uma variavel para a tela de login
    if formulacriologin.validate_on_submit():
        usuario = Usuario.query.filter_by(email = formulacriologin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formulacriologin.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", usuario=usuario.nomeusuario))  # redirecionar para a tela de perfil
    return render_template("Paginainicial.html", form=formulacriologin)  # o que voce quer passar na primeira pagina

@app.route("/criarconta", methods = ["GET","POST"])
def criarconta():
    formulariocriarconta = FormularioCriarConta()
    if formulariocriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formulariocriarconta.senha.data) #criar criptografia na senha do usuario para nao ficar visivel no banco de dados
        usuario = Usuario(nomeusuario = formulariocriarconta.nomeusuario.data, email = formulariocriarconta.email.data, senha = senha)
        database.session.add(usuario)
        database.session.commit() #para criar uma seção e enviar os dados do usuario para o banco de dados
        login_user(usuario, remember=True ) #sistema de lembrete de login do usuario
        return redirect(url_for("perfil", usuario = usuario.nomeusuario)) # redirecionar para a tela de perfil
    return render_template("criarconta.html", form=formulariocriarconta)


@app.route("/perfil/<usuario>") #para criar link dinamico de diversos usuarios é só colocar entre <>
@login_required #adicionar novos atributos dentro de uma função e assim ela nao deixa qualquer pessoa acessar se não estiver logada
def perfil(usuario):
    return render_template("perfil.html", usuario = usuario) #passar parametro para a tela .html para lá no html ele possa pegar por exemplo o nome do usuario

@app.route("/sair")
@login_required
def sair():
    logout_user() #deslogar o usuario ao clicar em sair na tela inicial
    return redirect(url_for("homepage"))

#TODO PAREI NA AULA 12
