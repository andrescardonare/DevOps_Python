from flask import Flask, request, jsonify, render_template
import os
import sys

# Package directory (this folder)
package_dir = os.path.dirname(__file__)

# Ensure package_dir is on sys.path when running the module as a script
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# Import Dictionary using a package-relative import when possible
try:
    from . import Dictionary
except Exception:
    # Fallback when executed in some contexts
    from hashmap import Dictionary

# Use the hashmap package directory as the templates folder so everything
# is self-contained inside the hashmap/ folder. index.html sits next to this file.
templates_path = package_dir
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
