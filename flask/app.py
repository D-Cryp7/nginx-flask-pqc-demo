from flask import Flask, request, jsonify
from crypto import Signer

app = Flask(__name__)
signer = Signer()

@app.get("/")
def index():
    return (
        "Hola! Este es un servidor Flask donde puedes firmar y verificar firmas digitales con PQC!\n"
    )

@app.post("/sign")
def sign_message():
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "Falta 'message'"}), 400

    signature = signer.sign(message.encode())
    return jsonify({
        "signature": signature.hex()
    })

@app.post("/verify")
def verify_signature():
    data = request.get_json()
    message = data.get("message")
    signature_hex = data.get("signature")

    if not all([message, signature_hex]):
        return jsonify({"error": "Faltan campos"}), 400

    try:
        valid = signer.verify(message.encode(), bytes.fromhex(signature_hex))
        return jsonify({"valid": valid})
    except Exception as e:
        return jsonify({"valid": False, "error": str(e)})
