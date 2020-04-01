from flask import Flask, render_template, request, redirect
import flask_excel as excel

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
# @app.route('/components.html')
# def compo():
#     return render_template('components.html')
#
# @app.route('/contact.html')
# def cont():
#     return render_template('contact.html')
#
# @app.route('/index.html')
# def home():
#     return render_template('index.html')

# or

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.csv', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database2 = excel.make_response_from_array(
            [["email", {email}], ["subject", {subject}], ["message", {message}]], "csv", file_name="database.csv")
        return database2


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'


if __name__ == '__main__':
    excel.init_excel(app)
    app.run()
