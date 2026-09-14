from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Cargar recetas con ingredientes exactos
try:
    with open('data/recetas.json', 'r', encoding='utf-8') as f:
        RECETAS = json.load(f)
except Exception as e:
    print(f"Error cargando recetas: {e}")
    RECETAS = []

# Sacar categorías y regiones únicas para los filtros
CATEGORIAS = sorted(list(set(r.get('categoria','') for r in RECETAS)))
REGIONES = sorted(list(set(r.get('region','') for r in RECETAS)))

@app.route('/')
def index():
    q = request.args.get('q', '').lower()
    categoria = request.args.get('categoria', '')
    region = request.args.get('region', '')

    filtradas = RECETAS

    if q:
        filtradas = [r for r in filtradas if q in r['nombre'].lower() or q in r['desc'].lower()]
    if categoria:
        filtradas = [r for r in filtradas if r.get('categoria') == categoria]
    if region:
        filtradas = [r for r in filtradas if r.get('region') == region]

    return render_template('index.html', 
                           recetas=filtradas, 
                           total=len(filtradas),
                           q=request.args.get('q',''),
                           categorias=CATEGORIAS,
                           regiones=REGIONES,
                           categoria_activa=categoria,
                           region_activa=region)

@app.route('/receta/<int:receta_id>')
def ver_receta(receta_id):
    receta = next((r for r in RECETAS if r['id'] == receta_id), None)
    if not receta:
        return "Receta no encontrada", 404
    return render_template('receta.html', receta=receta)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)