import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,
            template_folder='../frontend',  # Pointing to the frontend folder for templates (HTML files)
            static_folder='../frontend')    # Pointing to the frontend folder for static files (CSS, JS, images)
users = {}  # In-memory user storage for demonstration purposes
@app.route('/')
 


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you would typically check the login credentials against a database
        return redirect(url_for('index'))  # Redirect to the homepage after successful login
    return render_template('auth.html')  # Renders auth.html from frontend folder

def index():
    return render_template('index.html')

@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Implement the signup logic (store new user, etc.)
        if username in users:
            return "Username already exists. Please choose a different username.", 400
        # Store the new user's data
        users[username] = password
        return redirect(url_for('index'))  # Redirect to the homepage after signing up
    return render_template('signup.html')  # Renders signup.html from frontend folder


@app.route('/signin.html', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Implement the sign-in logic (authentication, etc.)
        return redirect(url_for('index'))  # Redirect to the homepage after signing in
    return render_template('signin.html')  # Renders signin.html from frontend folder



@app.route('/post_item.html', methods=['GET', 'POST'])
def post_item():
    if request.method == 'POST':
        item_name = request.form['item_name']
        description = request.form['description']
        quantity = request.form['quantity']
        # Handle item posting logic here (save to the database, etc.)
        return redirect(url_for('index'))  # Redirect to the homepage after posting the item
    return render_template('post_item.html')  # Renders postitem.html from frontend folder

@app.route('/request_item.html', methods=['GET', 'POST'])
def request_item():
    if request.method == 'POST':
        item_name = request.form['item_name']
        # Handle item request logic here
        return redirect(url_for('index'))  # Redirect to the homepage after requesting the item
    return render_template('requestitem.html')  # Renders requestitem.html from frontend folder

if __name__ == '__main__':
    app.run(debug=True)
