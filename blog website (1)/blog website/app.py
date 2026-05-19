from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

# SECRET KEY
app.secret_key = "supersecretkey"

# DATABASE SETUP
def init_db():

    conn = sqlite3.connect('blog.db')
    c = conn.cursor()

    # USERS TABLE
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # POSTS TABLE
    c.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

init_db()

# HOME PAGE
@app.route('/')
def index():

    conn = sqlite3.connect('blog.db')
    c = conn.cursor()

    c.execute("SELECT * FROM posts ORDER BY id DESC")

    posts = c.fetchall()

    conn.close()

    return render_template(
        'index.html',
        posts=posts,
        username=session.get('username')
    )

# REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect('blog.db')
        c = conn.cursor()

        try:

            c.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )

            conn.commit()

        except:

            return "Username already exists"

        conn.close()

        return redirect('/login')

    return render_template('register.html')

# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('blog.db')
        c = conn.cursor()

        c.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = c.fetchone()

        conn.close()

        if user and check_password_hash(user[2], password):

            session['username'] = username

            return redirect('/')

        else:

            return "Invalid username or password"

    return render_template('login.html')

# LOGOUT
@app.route('/logout')
def logout():

    session.pop('username', None)

    return redirect('/')

# CREATE POST
@app.route('/create', methods=['GET', 'POST'])
def create():

    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':

        title = request.form['title']
        content = request.form['content']

        conn = sqlite3.connect('blog.db')
        c = conn.cursor()

        c.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            (title, content)
        )

        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('create.html')

# VIEW POST
@app.route('/post/<int:id>')
def post(id):

    conn = sqlite3.connect('blog.db')
    c = conn.cursor()

    c.execute(
        "SELECT * FROM posts WHERE id=?",
        (id,)
    )

    post = c.fetchone()

    conn.close()

    return render_template('post.html', post=post)

# EDIT POST
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    if 'username' not in session:
        return redirect('/login')

    conn = sqlite3.connect('blog.db')
    c = conn.cursor()

    if request.method == 'POST':

        title = request.form['title']
        content = request.form['content']

        c.execute(
            "UPDATE posts SET title=?, content=? WHERE id=?",
            (title, content, id)
        )

        conn.commit()
        conn.close()

        return redirect('/')

    c.execute(
        "SELECT * FROM posts WHERE id=?",
        (id,)
    )

    post = c.fetchone()

    conn.close()

    return render_template('edit.html', post=post)

# DELETE POST
@app.route('/delete/<int:id>')
def delete(id):

    if 'username' not in session:
        return redirect('/login')

    conn = sqlite3.connect('blog.db')
    c = conn.cursor()

    c.execute(
        "DELETE FROM posts WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/')

# RUN APP
if __name__ == '__main__':
    app.run(debug=True)