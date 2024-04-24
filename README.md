## Design for Toy Ordering Website using Flask

### HTML Files

- **index.html**: Displays a simple form where users can enter their name, toy item, and quantity they want to order.
- **order_confirmation.html**: Shows the order summary with the user's name, toy item, quantity, and a confirmation message.

### Routes

- **"/"**: Handles the GET request for the **index.html** page, displaying the form.
- **"/order"**: Processes the POST request sent from the **index.html** page. It validates the user's input and redirects to the **order_confirmation.html** page if the order is valid.
- **"/order_confirmation"**: Handles the GET request for **order_confirmation.html**, displaying the order summary.