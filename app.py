from flask import Flask,render_template, redirect, url_for, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tarea'

conexion = MySQL(app)

port = 80

@app.route('/')
def inicio():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM alumnos WHERE nombre = %s AND contrasena = %s"
        cursor.execute(sql, (nombre, contrasena))
        dato = cursor.fetchone()  
        cursor.close()
        if dato:
            return redirect(url_for('cv'))
        else:
            print("no existe usuario con esos datos")
    return render_template('login.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= port)