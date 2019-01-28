from flask import Flask,render_template,url_for,redirect
from blogFlask import app,bcrypt,db
from blogFlask.forms import RegistrationForm,LoginForm 
from blogFlask.models import User,Post

posts = [
    {
        'author':'anish',
        'title':'anish page',
        'content':'First testing anish page',
        'date_posted':'20 April,2019'
    },
    {
        'author':'anil',
        'title':'anil page',
        'content':'First testing anil page',
        'date_posted':'21 April,2019'
    }
]

db.create_all()

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts = posts)

@app.route("/about")
def about():
    return render_template('about.html',title = 'about')

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    # if form.validate_on_submit():
    #     if form.email.data=='anish@gmail.com' and form.password.data=='anish':
    #         return redirect(url_for('home'))
    #     else:
    #         return redirect(url_for('login'))
    # add queries
    return render_template('login.html',title = 'Login',form = form)

@app.route("/register",methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',title = 'Register',form = form)

