
# Import the necessary module
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for handling the order
@app.route('/order', methods=['POST'])
def order():
    # Get the user's name, toy item, and quantity from the form
    name = request.form.get('name')
    toy_item = request.form.get('toy_item')
    quantity = request.form.get('quantity')

    # Validate the user's input
    if not name or not toy_item or not quantity:
        return render_template('index.html', error="Please fill out all fields.")

    return redirect(url_for('order_confirmation', name=name, toy_item=toy_item, quantity=quantity))

# Define the route for the order confirmation page
@app.route('/order_confirmation')
def order_confirmation():
    # Get the user's name, toy item, and quantity from the request arguments
    name = request.args.get('name')
    toy_item = request.args.get('toy_item')
    quantity = request.args.get('quantity')

    # Return the order confirmation page
    return render_template('order_confirmation.html', name=name, toy_item=toy_item, quantity=quantity)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
