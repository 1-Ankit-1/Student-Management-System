from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  course TEXT,
                  marks INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    data = c.fetchall()
    conn.close()
    return render_template('index.html', students=data)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        course = request.form['course']
        marks = request.form['marks']

        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute("INSERT INTO students(name, course, marks) VALUES (?, ?, ?)",
                  (name, course, marks))
        conn.commit()
        conn.close()
        return redirect('/')

    return render_template('add.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
