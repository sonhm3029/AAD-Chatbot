from .ir_bot_api import irbot_bp

def initRoute(app):
    
    @app.route("/", methods=["GET"])
    def hello():
        return "<div style='width:100%;height:100vh;display:flex;justify-content:center;align-items:center;position:fixed;'>Ivirse AAD Chatbot!</div>"
    app.register_blueprint(irbot_bp, url_prefix="/ir-bot")