from flask import Flask,render_template,url_for
app = Flask(__name__)

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

if __name__=='__main__':
    app.run(debug=True)