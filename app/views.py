from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Foo'}  # fake user
    posts = [                   # fake array of posts
        {
            'author': {'nickname': 'Clown'},
            'body': 'Funny how??  Funny ha ha?  Funny like a clown?'
        },
        {
            'author': {'nickname': 'Ethos'},
            'body': 'For every bottle of me, Starbucks will donate 5 cents because that is all they can afford from selling $5 cups of coffee'
        }
    ]
    return render_template('index.html',
                        title='Home',
                        user=user,
                        posts=posts)

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
