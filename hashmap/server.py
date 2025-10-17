from flask import Flask, request, jsonify, render_template
import os
import sys

# Compute project root and ensure it's on sys.path so imports work when this
# file is executed directly (python hashmap/server.py) or via the package (python -m hashmap.server)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import Dictionary from package
from hashmap import Dictionary

# Use absolute templates path so flask can find the index.html regardless of CWD
templates_path = os.path.join(project_root, 'templates')
app = Flask(__name__, template_folder=templates_path)
dict_instance = Dictionary(20)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')
    result = dict_instance.add(key, value)
    return jsonify({'result': result})

@app.route('/lookup', methods=['GET'])
def lookup():
    key = request.args.get('key')
    result = dict_instance.lookup(key)
    return jsonify({'result': result})

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')
    result = dict_instance.update(key, value)
    return jsonify({'result': result})

@app.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    key = data.get('key')
    result = dict_instance.delete(key)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
