from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector, random

app = Flask(__name__)
app.secret_key = 'chave_flask_super_secreta'  # Necessário para usar session

def get_database_connection():
    try:
        db_config = {
            'user': 'python',
            'password': 'aula@123',
            'host': 'amigooculto.mysql.database.azure.com',
            'port': 3306,
            'database': 'amigooculto'
    }
        return db_config
    except mysql.connector.Error as err:
        print(f"Erro de conexão: {err}")
        return None


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/envelope', methods=['GET', 'POST'])
def envelope():
    if request.method == 'POST':
        
        # Inserir no banco
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        query = ""
        cursor.execute(query, (,))
        cnx.commit()
        cursor.close()
        cnx.close()

        # Após cadastrar, redireciona para página inicial ou outra
        return redirect(url_for('index'))
    else:
        return render_template('')


# Função para registrar os usuarios do amigo oculto.
def registrar_usuario(usuario, senha):
    try:
        cnx = get_database_connection()
        if not cnx:
            return False

        cursor = cnx.cursor()

        # Inserir o usuário no banco de dados
        query = "INSERT INTO usuario_secretaria (usuario, senha) VALUES (%s, %s)"
        cursor.execute(query, (usuario, senha))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar usuário: {err}")
        return False


if __name__ == '__main__' :
    app.run(debug=True)
