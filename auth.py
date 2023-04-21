from flask import Blueprint, redirect, render_template, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from forms import RegisterForm, LoginForm
from models import User
from app import db
from uuid import uuid4

auth = Blueprint('auth', __name__)

def register_user(email, username, password, password2):
        if password != password2:
            raise Exception('Passwords must match')
        
        user = User.query.filter_by(email=email).first()
        if user:
            raise Exception('User already exist')
        
        id = str(uuid4())
        hash_password = generate_password_hash(password, method='sha256')
        new_user = User(id=id, email=email, username=username, password=hash_password)
        db.session.add(new_user)
        db.session.commit()

        return new_user
        

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        password2 = form.password2.data

        try:
            new_user = register_user(email, username, password, password2)
            login_user(new_user, remember=True)

            return redirect(url_for('routes.index'))
        except Exception as err:
            print(err)

    return render_template('register.html', form=form)

@auth.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        try:
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('routes.index'))
            else:
                print('Invalid credentials')
        except Exception as err:
            print(err)

    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))