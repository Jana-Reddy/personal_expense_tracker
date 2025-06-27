from flask import Flask, render_template, request, redirect
from db import init_db, add_expense, get_expenses

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    expenses = get_expenses()
    return render_template("index.html", expenses=expenses)

@app.route('/add', methods=['POST'])
def add():
    date = request.form['date']
    category = request.form['category']
    description = request.form['description']
    amount = float(request.form['amount'])
    add_expense(date, category, description, amount)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
