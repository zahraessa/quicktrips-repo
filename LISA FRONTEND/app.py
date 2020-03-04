from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contactus', methods=['GET', 'POST'])
def contactus():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        messages = request.form.get('messages')
        return redirect(url_for('messagesent'))
    return render_template('contactus.html')


@app.route('/detail')
def detail():
    return render_template('detail.html')


@app.route('/emailsent')
def emailsent():
    return render_template('emailsent.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/forgetpw')
def forgetpw():
    return render_template('forgetpw.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/keyword')
def keyword():
    return render_template('keyword.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/messagesent')
def messagesent():
    return render_template('messagesent.html')


@app.route('/que')
def que():
    return render_template('que.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/useredit')
def useredit():
    return render_template('useredit.html')


@app.route('/usereditaddress')
def usereditaddress():
    return render_template('usereditaddress.html')


@app.route('/usereditemail')
def usereditemail():
    return render_template('usereditemail.html')


@app.route('/usereditname')
def usereditname():
    return render_template('usereditname.html')


@app.route('/usereditpassword')
def usereditpassword():
    return render_template('usereditpassword.html')


@app.route('/usereditphoto')
def usereditphoto():
    return render_template('usereditphoto.html')


@app.route('/usereditusername')
def usereditusername():
    return render_template('usereditusername.html')


@app.route('/userfavourite')
def userfavourite():
    return render_template('userfavourite.html')


@app.route('/userpage')
def userpage():
    return render_template('userpage.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
