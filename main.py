from flask import Flask, render_template
import json
import os

app = Flask(__name__)

try:
    with open('data/recetas.json', 'r', encoding='utf-8') as f:
        RECETAS = json.load(f)
except:
    RECETAS = []

@app.route('/')
def index():
    return render_template('index.html', recetas=RECETAS)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
