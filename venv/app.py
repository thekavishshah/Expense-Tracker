from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64))
    amount = db.Column(db.Float)
    date = db.Column(db.String(64))
    description = db.Column(db.String(256))

    def to_json(self):
        return {
            "id": self.id,
            "category": self.category,
            "amount": self.amount,
            "date": self.date,
            "description": self.description
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    expense = Expense(category=data['category'], amount=data['amount'],
                      date=data['date'], description=data['description'])
    db.session.add(expense)
    db.session.commit()
    return jsonify(expense.to_json()), 201

@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([e.to_json() for e in expenses])

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
