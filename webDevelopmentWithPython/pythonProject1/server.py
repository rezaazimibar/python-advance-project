import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username.upper(), post_id=post_id)


@app.route('/<string:username>')
def all_pages(username, post_id=None):
    return render_template(username, name=username, post_id=post_id)


def write_to_file(data):
    with open('database.txt', mode='a') as file:
        email = data['email']
        message = data['message']
        my_file = file.write(f'\n email is: ({email}),and the content is: ({message})')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a+') as file2:
        email = data['email']
        message = data['message']
        my_csv = csv.writer(file2, delimiter='|', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        my_csv.writerow([email, message])


@app.route('/<username>/submit_form', methods=["POST", "GET"])
def submit_form(username=None):
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'something went wrong'
    else:
        return "some thing went wrong try again"
