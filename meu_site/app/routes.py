from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

# Configuração do MySQL
db_host = 'localhost'
db_user = 'gabriel'
db_password = 'Jupiter1?'
db_name = 'mydatabase'

def get_db_connection():
    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        db=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

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
        
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO contatos (email, nome, assunto) VALUES (%s, %s, %s)", (email, subject, description))
            connection.commit()
        finally:
            connection.close()

        return 'sucesso'
    return render_template('contato.html')

# rota usuários para listar todos os usuário no banco de dados.
@app.route('/users')
def users():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM contatos")
            requestsDetails = cursor.fetchall()
    finally:
        connection.close()

    return render_template("users.html", requestsDetails=requestsDetails)

if __name__ == '__main__':
    app.run(debug=True)
