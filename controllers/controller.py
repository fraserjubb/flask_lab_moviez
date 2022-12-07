from flask import render_template
from app import app
from models.orders_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title="orders", orders=orders)

@app.route('/orders/<order>')
def order(order):
    return render_template('order.html', title="order", order=orders[int(order)])
    


