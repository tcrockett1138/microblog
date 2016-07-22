from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Foo'}  # fake user
    posts = [                   # fake array of posts
        {
            'author': {'nickname': 'Clown'},
            'body': 'Funny how??  Funny ha ha?  Funny like a clown'
        },
        {
            'author': {'nickname': 'Ethos'},
            'body': {'For every bottle of me, Starbucks will donate 5 cents because that is all they can afford from selling $5 cups of coffee'}
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)