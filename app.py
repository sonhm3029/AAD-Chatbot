from flask import Flask
from flask_cors import CORS

from dotenv import load_dotenv

from api import initRoute

load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024
CORS(app)

initRoute(app)

if __name__ == "__main__":
    app.run("0.0.0.0", port=8008, debug=True)