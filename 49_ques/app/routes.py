from flask import render_template, redirect, url_for, request, flash
from app import app, mongo, bcrypt
from app.forms import SignupForm, LoginForm

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        mongo.db.users.insert_one({'username': username, 'password': password})
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = mongo.db.users.find_one({'username': username})
        if user and bcrypt.check_password_hash(user['password'], password):
            return redirect(url_for('hello'))

        flash('Login failed. Check your username and/or password.', 'danger')

    return render_template('login.html', form=form)

@app.route('/hello')
def hello():
    return render_template('hello.html')
