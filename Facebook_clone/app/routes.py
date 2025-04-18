from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import RegistrationForm, LoginForm, PostForm
from app.models import User, Post, FriendRequest
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Account created! You can log in now.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('home.html', form=form, posts=posts)

@app.route('/send_request/<int:user_id>')
@login_required
def send_request(user_id):
    req = FriendRequest(sender_id=current_user.id, receiver_id=user_id)
    db.session.add(req)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/accept_request/<int:req_id>')
@login_required
def accept_request(req_id):
    req = FriendRequest.query.get_or_404(req_id)
    if req.receiver_id == current_user.id:
        req.status = 'accepted'
        sender = User.query.get(req.sender_id)
        current_user.friends.append(sender)
        db.session.commit()
    return redirect(url_for('home'))
