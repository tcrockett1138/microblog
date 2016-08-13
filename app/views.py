from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])
