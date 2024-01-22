from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/smartrolly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255))  
    featured = db.Column(db.Integer, default=0)

class Order(db.Model):
    order_id = db.Column(db.String(50), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    product = db.relationship('Product', foreign_keys='Order.product_id', backref='orders')

class Payment(db.Model):
    payment_id = db.Column(db.String(50), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    product = db.relationship('Product', foreign_keys='Payment.product_id', backref='payments')
    user = db.relationship('User', foreign_keys='Payment.user_id', backref='payments')


@app.route('/')
def home():
    with open('products.json', 'r') as file:
        products_data = json.load(file)
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

@app.route('/electronics')
def electronics():
    return render_template('electronics.html')

@app.route('/view_product/<int:product_id>')
def view_product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('view_product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)