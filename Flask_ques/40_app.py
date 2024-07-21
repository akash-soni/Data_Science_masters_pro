from flask import Flask, request, render_template

app = Flask(__name__)

# Route to display the form
@app.route('/')
def home():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    name = request.form['name']
    email = request.form['email']
    
    # Process the data (e.g., save to database, send email, etc.)
    # For this example, we'll just display the data
    return f'<h1>Form Submitted!</h1><p>Name: {name}</p><p>Email: {email}</p>'

if __name__ == '__main__':
    app.run(debug=True)