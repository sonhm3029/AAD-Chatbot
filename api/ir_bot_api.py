from flask import request, jsonify

def regsiterRoute(app):
    @app.route("/ir-bot", methods=["POST"])
    def chat():
        """API for handle chat"""
        name = request.get_json()["name"]
        
        return jsonify({
            "message": f"Hello {name}"
        })