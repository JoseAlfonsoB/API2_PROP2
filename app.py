from flask import Flask, render_template, request, jsonify
from tsp import hill_climbing

app = Flask(__name__)

# Coordenadas iniciales
coord = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754, -103.346253),
    'Monterrey': (25.691611, -100.321838),
    'QuintanaRoo': (21.163112, -86.802315),
    'Michohacan': (19.701400, -101.208297),
    'Aguascalientes': (21.876410, -102.264387),
    'CDMX': (19.432713, -99.133183),
    'QRO': (20.597194, -100.386670)
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ruta', methods=['POST'])
def calcular_ruta():
    global coord
    data = request.json
    nuevas = data.get('nuevas', [])

    for ciudad in nuevas:
        nombre = ciudad['nombre']
        lat = float(ciudad['lat'])
        lon = float(ciudad['lon'])
        coord[nombre] = (lat, lon)

    ruta, distancia_total = hill_climbing(coord)
    return jsonify({'ruta': ruta, 'distancia': distancia_total})

if __name__ == '__main__':
    app.run(debug=True)
