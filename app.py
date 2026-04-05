from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Tarea 1: 8 útiles escolares iniciales
productos = [
    {"id": 1, "nombre": "Cuaderno", "cantidad": 50, "precio": 2.50, "marca": "Norma"},
    {"id": 2, "nombre": "Lapiz HB", "cantidad": 100, "precio": 0.30, "marca": "Mirado"},
    {"id": 3, "nombre": "Borrador", "cantidad": 80, "precio": 0.50, "marca": "Pelikan"},
    {"id": 4, "nombre": "Boligrafo", "cantidad": 60, "precio": 0.80, "marca": "Kilometrico"},
    {"id": 5, "nombre": "Regla 30cm", "cantidad": 40, "precio": 1.20, "marca": "Artesco"},
    {"id": 6, "nombre": "Colores x12", "cantidad": 25, "precio": 4.50, "marca": "Crayola"},
    {"id": 7, "nombre": "Calculadora", "cantidad": 10, "precio": 15.00, "marca": "Casio"},
    {"id": 8, "nombre": "Pegante", "cantidad": 35, "precio": 1.10, "marca": "UHU"}
]

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/agregar', methods=['POST'])
def agregar():
    siguiente_id = max([p['id'] for p in productos]) + 1 if productos else 1
    # Tarea 2: Se incluye 'marca'
    nuevo_producto = {
        "id": siguiente_id,
        "nombre": request.form["nombre"],
        "cantidad": int(request.form["cantidad"]),
        "precio": float(request.form["precio"]),
        "marca": request.form["marca"]
    }
    productos.append(nuevo_producto)
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    global productos
    productos = [p for p in productos if p['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)