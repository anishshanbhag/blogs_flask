from flask import Flask,render_template,url_for,redirect
from forms import LoginForm , RegistrationForm
app = Flask(__name__)

app.config['SECRET_KEY']='a418c5068de199be3fe075951117d80b'

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