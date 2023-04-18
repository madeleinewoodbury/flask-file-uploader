from flask import Flask, jsonify, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from config import cloudinary, SECRET
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET
app.config['UPLOAD_FOLDER'] = 'images'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
BASEDIR = os.path.abspath(os.path.dirname(__file__))
@app.route('/')
def index():
    return render_template('base.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    try:
        if request.method == 'POST':
            if 'file' not in request.files:
                return render_template('uploadFile.html')
            
            file = request.files['file']
            if file.filename and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
                filename = secure_filename(file.filename)
                filepath = os.path.join(BASEDIR, app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                data = cloudinary.uploader.upload(file=filepath,
                                                  use_filename=True,
                                                  unique_filename=False,
                                                  folder='test')

                for key, val in data.items():
                    print(f'{key}; {val}')
            
                os.remove(filepath)
            else:
                print('no filename')
            return redirect(url_for('index'))
        else:
            return render_template('uploadFile.html')
    except Exception as err:
        print(err)
