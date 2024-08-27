from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<username>/<int:postid>')
def hello_world(username=None, postid=None):
    return render_template('./index.html', name=f'hello ms/mss {username},', mymy=postid)


@app.route('/<username>')
def url_func(username=None):
    return render_template('./index.html', name=username)


@app.route('/blog')
def blog_func():
    return 'this is a blog page that created with function in python'


@app.route('/blog/tec')
def tec_func():
    return 'mobile app and technology'
