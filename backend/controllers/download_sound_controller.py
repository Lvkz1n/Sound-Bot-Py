import os
from flask_restx import Namespace, Resource, fields
from flask import jsonify, Blueprint, request, send_file, Response
from services.download_sound_service import DownloadSoundService

download_sound_bp:Blueprint = Blueprint('download',__name__)
api = Namespace("Sound", description="Download Sound")

@api.route('/download')
class DownloadSoundController(Resource):
    @api.response(201, "Download success!")
    @api.response(404, "URL not found")
    @api.response(408, "Time exceeded when download the audio")
    @api.response(400, "Some unhandled error occurred")
    @download_sound_bp.route('/download/', methods={'POST', 'OPTIONS'})
    def post(self):
        content = request.json


        sound = DownloadSoundService().downloadMusic(content["url"], content{"type"})

        if content["type"] == "music":
            mimetype = "audio/wav"
        elif content ["type"] == "video":
            mimetype = "video/mp4"
        else:
            return jsonify({"message": "invalid type provide"}), 400
        

        try:
            with open(sound, 'rb') as f:
                file_data = f.read()

                response = Response(file_data, mimetype=mimetype, headrs={
                   'Content-Disposition': f'attachment; filename={os.path.basename(sound)}' 
                })