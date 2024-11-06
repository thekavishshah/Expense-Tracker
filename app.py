from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Route to display expenses
@app.route('/')
def index():
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    c.execute('SELECT * FROM expenses')
    expenses = c.fetchall()
    conn.close()
    return render_template('index.html', expenses=expenses)

# Route to add an expense
@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        title = request.form['title']
        amount = float(request.form['amount'])
        category = request.form['category']
        date = request.form['date']
        
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)',
                  (title, amount, category, date))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    return render_template('add_expense.html')

# Route to delete an expense
@app.route('/delete/<int:expense_id>')
def delete_expense(expense_id):
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    c.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Route to display expenses grouped by category
@app.route('/group_by_category')
def group_by_category():
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    c.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    grouped_expenses = c.fetchall()
    conn.close()
    return render_template('group_by_category.html', grouped_expenses=grouped_expenses)

@app.route('/edit/<int:expense_id>', methods=['GET', 'POST'])
def edit_expense(expense_id):
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    if request.method == 'POST':
        title = request.form['title']
        amount = float(request.form['amount'])
        category = request.form['category']
        date = request.form['date']
        
        c.execute('UPDATE expenses SET title = ?, amount = ?, category = ?, date = ? WHERE id = ?',
                  (title, amount, category, date, expense_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        c.execute('SELECT * FROM expenses WHERE id = ?', (expense_id,))
        expense = c.fetchone()
        conn.close()
        return render_template('edit_expense.html', expense=expense)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
