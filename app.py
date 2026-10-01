import sqlite3

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


def consultar_jugadores(consulta, parametros=()):
    with sqlite3.connect('nominas.db') as conn:
        conn.row_factory = sqlite3.Row
        return conn.execute(consulta, parametros).fetchall()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buscar_seleccion')
def buscar_seleccion():
    seleccion = request.args.get('seleccion', '').strip()
    jugadores = consultar_jugadores(
        'SELECT * FROM jugadores WHERE seleccion = ?', (seleccion,)
    )
    return render_template(
        'index.html',
        jugadores_seleccion=jugadores,
        msg_seleccion=None if jugadores else 'No se encontraron jugadores para esa selección.',
    )


@app.route('/buscar_jugador')
def buscar_jugador():
    apellido = request.args.get('apellido', '').strip()
    jugadores = consultar_jugadores(
        'SELECT * FROM jugadores WHERE jugador LIKE ?', (f'%{apellido}%',)
    )
    return render_template(
        'index.html',
        jugadores_apellido=jugadores,
        msg_apellido=None if jugadores else 'No se encontraron jugadores.',
    )


@app.route('/buscar_equipo')
def buscar_equipo():
    equipo = request.args.get('equipo', '').strip()
    jugadores = consultar_jugadores(
        'SELECT * FROM jugadores WHERE equipo LIKE ?', (f'%{equipo}%',)
    )
    return render_template(
        'index.html',
        jugadores_equipo=jugadores,
        msg_equipo=None if jugadores else 'No se encontraron jugadores para ese equipo.',
    )


@app.route('/agregar_jugador', methods=['POST'])
def agregar_jugador():
    jugador = (
        request.form.get('seleccion'),
        request.form.get('jugador'),
        request.form.get('posicion'),
        request.form.get('edad'),
        request.form.get('equipo'),
    )
    with sqlite3.connect('nominas.db') as conn:
        conn.execute(
            '''
            INSERT INTO jugadores (seleccion, jugador, posicion, edad, equipo)
            VALUES (?, ?, ?, ?, ?)
            ''',
            jugador,
        )
    return redirect(url_for('index', msg_exito='Jugador creado exitosamente'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)