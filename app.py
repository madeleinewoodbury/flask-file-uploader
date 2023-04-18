import cloudinary

from dotenv import load_dotenv
import os

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECRET'),
    secure=True
)

import cloudinary.uploader
import cloudinary.api

results = cloudinary.uploader.upload(file='images/dog.jpeg', 
                                     public_id='dog_test_2',
                                     folder='test')

for key, val in results.items():
    print(f'{key}: {val}')
