from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define a simple route to render the index page
@app.route('/')
def index():
    return render_template('index.html')  # Frontend page, make sure it's in the templates folder

# Define the login/signup route
@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you would usually check if the username and password match what's in your database
        # For now, we will just redirect to the index page after submitting
        return redirect(url_for('index'))  # Redirect to the homepage after successful login
    return render_template('auth.html')  # Show the login page

# Define route for posting an item (could be for the "Lister" user)
@app.route('/post_item', methods=['GET', 'POST'])
def post_item():
    if request.method == 'POST':
        # Extract form data
        item_name = request.form['item_name']
        description = request.form['description']
        quantity = request.form['quantity']
        # Here you can add logic to save these details in the database
        # After successful posting, redirect to the index page
        return redirect(url_for('index'))
    return render_template('post_item.html')  # Show the post item page

if __name__ == '__main__':
    app.run(debug=True)
