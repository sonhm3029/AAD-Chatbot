from flask import request, jsonify, Blueprint

from middleware import authmiddleware

irbot_bp = Blueprint("irbot", __name__)

@irbot_bp.route("/chat", methods=["POST"])
@authmiddleware
def chat():
    """API for handle chat"""
    name = request.get_json()["name"]
    
    return jsonify({
        "message": f"Hello {name}"
    })
        