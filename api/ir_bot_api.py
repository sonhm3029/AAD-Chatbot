from flask import request, jsonify, Blueprint

from middleware import authmiddleware
from constants import API, UPLOAD_FOLDER, MAX_FILE_LENGTH
from utils import allowed_file, getUniqueFileName, read_pdf_file

from werkzeug.utils import secure_filename
import os

irbot_bp = Blueprint("irbot", __name__)

@irbot_bp.route(API.IR_BOT.CHAT, methods=["POST"])
@authmiddleware
def chat():
    """API for handle chat"""
    name = request.get_json()["name"]
    
    return jsonify({
        "code": 200,
        "message": f"Hello {name}"
    })
    
    
@irbot_bp.route(API.IR_BOT.READ_DOC, methods=["POST"])
@authmiddleware
def read_doc():
    """API to parse uploaded PDF documents to text"""
    try:
        if 'docs' not in request.files:
            raise Exception("No file part!")
        
        file = request.files['docs']
        
        if file.filename == '':
            raise Exception("No selected file!")        
        # Save upload file
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename) 
            saved_folder = getUniqueFileName(UPLOAD_FOLDER)
            
            if not os.path.exists(saved_folder):
                os.makedirs(saved_folder)
            
            filepath = os.path.join(saved_folder, filename)
            
            file.save(filepath)
        
        pdf_data = read_pdf_file(filepath)
        
        print(len(pdf_data))
        
        return jsonify({
            "code": 200,
            "path": filepath
        })
            
    except Exception as e:
        return jsonify({
            "code": 400,
            "message": str(e) or "Smt wrong has been occured!"
        })
        