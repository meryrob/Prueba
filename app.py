from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/register', methods=['GET'])
def get_register_data():
    # Aquí deberías generar las opciones para la creación de credenciales
    # y enviarlas al frontend. Este es un ejemplo simplificado.
    options = {
        'publicKey': {
            'challenge': 'challenge de ejemplo', # Debería ser un valor aleatorio y seguro
            'rp': {
                'name': 'Ejemplo App'
            },
            'user': {
                'id': 'user-id-de-ejemplo', # Debería ser único para cada usuario
                'name': 'usuario@example.com',
                'displayName': 'Usuario Ejemplo'
            },
            'pubKeyCredParams': [{
                'type': 'public-key',
                'alg': -7
            }],
            'timeout': 60000,
            'authenticatorSelection': {
                'authenticatorAttachment': 'platform',
                'userVerification': 'discouraged'
            },
            'attestation': 'direct'
        }
    }
    return jsonify(options)

@app.route('/register', methods=['POST'])
def complete_register():
    data = request.json
    # Aquí deberías verificar la credencial y almacenarla si es válida
    # Este es un ejemplo simplificado.
    print('Datos de la credencial:', data)
    return jsonify({'status': 'success', 'message': 'Usuario registrado'})

@app.route('/login', methods=['GET'])
def get_login_data():
    # Aquí deberías generar las opciones para obtener una aserción
    # y enviarlas al frontend. Este es un ejemplo simplificado.
    options = {
        'publicKey': {
            'challenge': 'challenge de ejemplo', # Debería ser un valor aleatorio y seguro
            'allowCredentials': [{
                'type': 'public-key',
                'id': 'user-id-de-ejemplo' # Debería coincidir con el id registrado
            }],
            'timeout': 60000,
            'userVerification': 'discouraged'
        }
    }
    return jsonify(options)

@app.route('/login', methods=['POST'])
def complete_login():
    data = request.json
    # Aquí deberías verificar la aserción y permitir el inicio de sesión si es válida
    # Este es un ejemplo simplificado.
    print('Datos de la aserción:', data)
    return jsonify({'status': 'success', 'message': 'Inicio de sesión exitoso'})

if __name__ == '__main__':
    app.run(debug=True)
