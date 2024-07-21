from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a real secret key

# Define the form class
class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1, max=120)])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = MyForm()
    if form.validate_on_submit():
        # Process form data
        name = form.name.data
        age = form.age.data
        return redirect(url_for('success', name=name, age=age))
    return render_template('form.html', form=form)

@app.route('/success')
def success():
    name = request.args.get('name')
    age = request.args.get('age')
    return f'Success! Name: {name}, Age: {age}'

if __name__ == '__main__':
    app.run(debug=True)
