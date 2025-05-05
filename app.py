from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Ma'lumotlar bazasini sozlash
def init_db():
    with sqlite3.connect('portfolio.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS projects 
                    (id INTEGER PRIMARY KEY, title TEXT, description TEXT, image_url TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS blog 
                    (id INTEGER PRIMARY KEY, title TEXT, content TEXT, date TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS contacts 
                    (id INTEGER PRIMARY KEY, name TEXT, email TEXT, message TEXT, date TEXT)''')
        conn.commit()

# Ma'lumotlar bazasini ishga tushirish
init_db()

# Asosiy sahifa
@app.route('/')
def home():
    return render_template('index.html')

# Portfolio sahifasi
@app.route('/portfolio')
def portfolio():
    with sqlite3.connect('portfolio.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM projects")
        projects = c.fetchall()
    return render_template('portfolio.html', projects=projects)

# Blog sahifasi
@app.route('/blog')
def blog():
    with sqlite3.connect('portfolio.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM blog ORDER BY date DESC")
        posts = c.fetchall()
    return render_template('blog.html', posts=posts)

# Bog'lanish sahifasi
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with sqlite3.connect('portfolio.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO contacts (name, email, message, date) VALUES (?, ?, ?, ?)",
                     (name, email, message, date))
            conn.commit()
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)