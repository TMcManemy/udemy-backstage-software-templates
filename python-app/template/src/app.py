from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify({
        'host': socket.gethostname(),
        'env': '${{values.evn_name}}',
        'app_name':'${{values.app_nname}}'
        })

@app.route('/api/v1/health')

def health():
    return jsonify({
        'status': 'up'
        }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
