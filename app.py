from flask import Flask, current_app
from flask import render_template
app = Flask(__name__)


@app.route('/')
@app.route('/view1')
@app.route('/view2')
@app.route('/view3')
def index():
    return current_app.send_static_file('index.html')
    #return render_template('index.html', name=name)

# @app.route('/view1')
# def view1(view=''):
#     return current_app.send_static_file('index.html')

# @app.route('/view2')
# def view2(view=''):
#     return current_app.send_static_file('src/my-view2.html')

# @app.route('/view3')
# def view3(view=''):
#     return current_app.send_static_file('src/my-view3.html')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#        return "POST"
#        # do_the_login()
#     # else:
#     #     #show_the_login_form()

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)