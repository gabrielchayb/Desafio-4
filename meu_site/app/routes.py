from app import app
from flask import Flask, render_template, request, url_for, jsonify
from flask_mysqldb import MySQL

# conexão com o banco de dados
app.config['MYSQL_HOST'] = 'localhost' # 127.0.0.1
app.config['MYSQL_USER'] = 'luis'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'historico'

mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/quem-somos', methods=['GET','POST'])
def quemSomos():
    return render_template('quem-somos.html')

@app.route('/contato', methods=['GET','POST'])
def contato():
    if request.method == "POST":
        email = request.form.get('email')
        subject = request.form.get('subject')
        description = request.form.get('description')
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos(email, nome, assunto) VALUES (%s, %s, %s)", (email, subject, description))       
        mysql.connection.commit()        
        cur.close()

        return 'sucesso'
    return render_template('contato.html')

# rota usuários para listar todos os usuário no banco de dados.
@app.route('/users')
def users():
    cur = mysql.connection.cursor()

    requests = cur.execute("SELECT * FROM contatos")

    if requests > 0:
        requestsDetails = cur.fetchall()

        return render_template("users.html", requestsDetails=requestsDetails)
