from flask import Flask
from flask import Blueprint
from controller import status,history
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, origin=['localhost','jphacks.github.io'], allow_headers=['Content-Type', 'Authorization'],
     methods=['GET', 'POST', 'PUT', 'DELETE'])


app.register_blueprint(status.app, url_prefix = '/api')
app.register_blueprint(history.app, url_prefix = '/api')

if __name__ == '__main__':
    app.run(debug=True)
