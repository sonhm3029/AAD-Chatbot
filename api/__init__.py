from .ir_bot_api import regsiterRoute as irBotRegisterRoute

def initRoute(app):
    
    @app.route("/", methods=["GET"])
    def hello():
        return "<div style='width:100%;height:100vh;display:flex;justify-content:center;align-items:center;position:fixed;'>Ivirse AAD Chatbot!</div>"
    irBotRegisterRoute(app)
    