from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import LoginForm , RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY']='a418c5068de199be3fe075951117d80b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(20) , unique = True , nullable = False)
    email = db.Column(db.String(120) , unique = True , nullable = False)
    image_file = db.Column(db.String(20), nullable = False , default = 'default.jpg')
    password = db.Column(db.String(20) ,nullable = False)
    posts = db.relationship('Post',backref = 'author',lazy = True)

    def __repr__(self):
        return '{},{},{}'.format(self.username,self.email,self.image_file)

class Post(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(20) , nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False , default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable = False)

    def __repr__(self):
        return '{},{}'.format(self.title,self.date_posted)


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
    if form.validate_on_submit():
        if form.email.data=='anish@gmail.com' and form.password.data=='anish':
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html',title = 'Login',form = form)

@app.route("/register",methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('register.html',title = 'Register',form = form)

if __name__=='__main__':
    app.run(debug=True)