from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    name = request.form.get('name')
    birthdate_str = request.form.get('birthdate')
    
    try:
        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
        age = calculate_age_from_birthdate(birthdate)
        return jsonify({'name': name, 'age': age})
    except ValueError:
        return jsonify(error='Invalid date format'), 400

def calculate_age_from_birthdate(birthdate):
    today = datetime.now().date()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

if __name__ == '__main__':
    app.run(debug=True)
