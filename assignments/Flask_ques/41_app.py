from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Route to display the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route to handle form submission and redirect
@app.route('/greet', methods=['GET'])
def greet_redirect():
    name = request.args.get('name')
    if name:
        return redirect(f'/greet/{name}')
    return redirect('/')

# Route to display a greeting message with the URL parameter
@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)