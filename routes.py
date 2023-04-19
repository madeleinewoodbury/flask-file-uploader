from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required
from file_upload import upload_file
from forms import ImageForm
from models import Image
from app import db

routes = Blueprint('routes', __name__)

@routes.route('/home')
@login_required
def index():
    return render_template('home.html', user=current_user)

@routes.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = ImageForm()
    if form.validate_on_submit():
        file = form.file.data
        description = form.description.data

        if file.filename:
            try:
                res = upload_file(file)
                url = res['secure_url']
                id = res['asset_id']

                new_image = Image(id=id, 
                                  url=url, 
                                  description=description, 
                                  user=current_user.id)
                
                db.session.add(new_image)
                db.session.commit()
                return redirect(url_for('routes.index'))

            except Exception as err:
                print(err)

    return render_template('uploadFile.html', form=form)
