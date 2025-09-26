from flask import Flask, request, jsonify, render_template
from hashmap import Dictionary

app = Flask(__name__, template_folder='templates')
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
    app.run(debug=True)
