from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify, request
from flask_restful import Api
# from resources.user import (Signup, Login, Secure, GetUser, UpdateUser)
from resources.predictDisease import PredictDisease
# from resources.medicine import Medicine
# from resources.remedies import AyurvedicRemedies
# from resources.AyurvedicDoshas import AyurvedicDoshas
# from mongo_engine import db
# from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os
from englisttohindi.englisttohindi import EngtoHindi

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config["JWT_SECRET_KEY"] = "all_stackers_going_to_win_hackathon"

# jwt = JWTManager(app)

# DB_URI = os.getenv("FLASK_MONGODB_URI")

# app.config["MONGODB_HOST"] = DB_URI

# db.init_app(app)


api.add_resource(PredictDisease, "/predictDisease")

@app.route('/translate', methods=['GET'])
def translate_text():
    try:
        

        return "hello world"

    except Exception as e:
        return "bad"






# @app.route('/translate', methods=['POST'])
# def translate_text():
#     try:
#         # Get the text from the POST request
#         data = request.get_json()
#         text_to_translate = data['text']

#         # Translate the text using EngtoHindi
#         translator = EngtoHindi(text_to_translate)
#         translation = translator.convert

#         return jsonify({'translation': translation})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
