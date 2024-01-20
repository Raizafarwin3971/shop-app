from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/smartrolly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/fashion')
def fashion():
    return render_template('fashion.html')

@app.route('/jewellery')
def jewellery():
    return render_template('jewellery.html')

@app.route('/watches')
def watches():
    return render_template('watches.html')

@app.route('/electronic')
def accessories():
    return render_template('electronic.html')

if __name__ == '__main__':
    app.run(debug=True)