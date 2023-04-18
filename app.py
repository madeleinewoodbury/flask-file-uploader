from flask import Flask, jsonify
from config import cloudinary, SECRET

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET

@app.route('/')
def index():
    try:
        data = cloudinary.uploader.upload(file='images/dog.jpeg', 
                                          public_id='dog_test_3',
                                          folder='test')
        
        res = jsonify(data)
        res.status_code = 200
        return res
        
    except Exception as err:
        print(type(err), err)

