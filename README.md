# Expense-Tracker


A web-based application to help users track and manage their expenses efficiently. The Expense Tracker allows users to add, view, edit, and categorize expenses, and provides summarized expense reports based on categories.


# Features

Add Expenses: Quickly add expenses with details such as title, amount, category, and date.

Edit and Delete Expenses: Update or delete existing expenses.

Group by Category: View a categorized summary of expenses to understand spending patterns.

User-Friendly Interface: Simple and intuitive UI for easy navigation and usage.

Database Persistence: Stores data in SQLite to ensure expenses are retained between sessions.


# Technologies Used

Python: The core programming language for the back-end logic.

Flask: A lightweight framework to build the web application and handle routing.

SQLite: Database to store and manage expense records.

HTML/CSS: Front-end technologies for creating a responsive and user-friendly interface.

Jinja2: Templating engine for rendering HTML pages.


# Setup & Installation
**Prerequisites**

Ensure you have Python 3.6+ and pip installed.

**Clone the repository:**

git clone https://github.com/your-username/Expense-Tracker.git
cd Expense-Tracker

**Create a virtual environment (optional, but recommended):**

python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

**Install dependencies:**

pip install -r requirements.txt

**Run the application:**

python app.py
Open your browser and navigate to http://127.0.0.1:5000 to view the app.

# Database Setup

The application uses an SQLite database. If expenses.db does not exist, it will be created automatically when you start the app.


# Usage

**Adding an Expense**

Go to the "Add Expense" page.

Fill in the details for the expense: title, amount, category, and date.

Click "Add Expense" to save.

**Viewing and Grouping Expenses**

Visit the "Group by Category" page to see expenses categorized by type.

Use the "Go Back" button to return to the main page.

**Editing and Deleting Expenses**

Use the options in the expense list to edit or delete an entry.

