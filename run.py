from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/ws')
def ws():
    respuesta="respuesta"
    return jsonify({'parametro':respuesta})


if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=5000,debug=True)
    app.run(debug=True)