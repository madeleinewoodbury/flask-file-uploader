import os
from app import app
from werkzeug.utils import secure_filename
from config import cloudinary

BASEDIR = os.path.abspath(os.path.dirname(__file__))

def upload_file(file):
    filename = secure_filename(file.filename)
    filepath = os.path.join(BASEDIR, app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
        
    data = cloudinary.uploader.upload(file=filepath,
                                      use_filename=True,
                                      unique_filename=False,
                                      folder='flask-gallery')
    os.remove(filepath)
    return data


