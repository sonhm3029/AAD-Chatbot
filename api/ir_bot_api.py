from flask import request, jsonify, Blueprint

irbot_bp = Blueprint("irbot", __name__)

@irbot_bp.route("/chat", methods=["POST"])
def chat():
    """API for handle chat"""
    name = request.get_json()["name"]
    
    return jsonify({
        "message": f"Hello {name}"
    })
        