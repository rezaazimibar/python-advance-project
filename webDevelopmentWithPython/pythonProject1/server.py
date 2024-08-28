from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username.upper(), post_id=post_id)


@app.route('/<string:username>')
def all_pages(username, post_id=None):
    return render_template(username, name=username, post_id=post_id)


@app.route('/<username>/submit_form', methods=["POST", "GET"])
def submit_form(username=None):
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        return redirect('/thankyou.html')
    else:
        return "some thing went wrong try again"
