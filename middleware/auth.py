from functools import wraps
from flask import request, abort

import os

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            if not "Ivirsekey" in request.headers:
                return {
                    "message": "Authentication token is missing!",
                    "data": None,
                    "error": "Unauthorized"
                }, 400
            token = request.headers["Ivirsekey"]
            true_token = os.environ["API_KEY"]
            print(true_token)
            if token != true_token:
                return {
                    "message": "Invalid Authentiacation token!",
                    "data": None,
                    "error": "Unauthorized"
                }
        except Exception as e:
            return {
                "message": str(e),
                "code": 500
            }, 500
        return f(*args, **kwargs)
    return decorated