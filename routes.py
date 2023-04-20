from uuid import uuid4
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from file_upload import upload_file
from forms import ImageForm, GalleryForm
from models import Image, Gallery
from app import db

routes = Blueprint('routes', __name__)

@routes.route('/home')
@login_required
def index():
    galleries = Gallery.query.filter_by(user=current_user.id).all()
    return render_template('home.html', user=current_user, galleries=galleries)

@routes.route('/add-gallery', methods=['GET', 'POST'])
@login_required
def create_gallery():
    form = GalleryForm()
    if form.validate_on_submit():
        id = str(uuid4())
        title = form.title.data
        description = form.description.data

        new_gallery = Gallery(id=id, title=title, description=description, user=current_user.id)
        db.session.add(new_gallery)
        db.session.commit()
        return redirect(url_for('routes.index'))

    return render_template('addGallery.html', form=form)

@routes.route('/gallery')
@login_required
def gallery():
    id = request.args['id']
    gallery = Gallery.query.filter_by(id=id).first()
    return render_template('gallery.html', gallery=gallery)


@routes.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    gallery_id = request.args['id']
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
                                  gallery_id=gallery_id)
                
                db.session.add(new_image)
                db.session.commit()
                return redirect(url_for('routes.gallery', id=gallery_id))

            except Exception as err:
                print(err)
    

    return render_template('uploadFile.html', form=form, id=gallery_id)
