# Flask Blog Website

A complete blog website built using Python, Flask, SQLite, and HTML/CSS with full authentication and CRUD functionality.
# Features
User Registration
User Login & Logout
Password Hashing
Create Blog Posts
Edit Blog Posts
Delete Blog Posts
View All Posts
View Single Post
SQLite Database
Responsive UI using HTML & CSS
Technologies Used
Python 3
Flask
Flask-SQLAlchemy
Flask-Login
SQLite
HTML5
CSS3
# Project Structure
blog-website/
│
├── app.py
├── blog.db
├── requirements.txt
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── create.html
│   ├── edit.html
│   ├── post.html
│   ├── login.html
│   └── register.html
│
└── README.md
# Installation
1. Clone the repsitory:
git clone https://github.com/Riya-a11y-spec-svg/blog-website.git
2. Create Virtual Environment:
Windows
python -m venv venv
venv\Scripts\activate
Linux/Mac
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies:
pip install flask flask_sqlalchemy flask_login werkzeug

Or use:
pip install -r requirements.txt
4. Run the Application:
python app.py
6. Open in Browser
Server will start at:http://127.0.0.1:5000
Authentication Features
# Register
Users can create a new account using:
/register
Login

Existing users can login using:
/login
Logout

Users can logout securely using:
/logout
# Blog Features
Create Post
Authenticated users can create posts.

Edit Post
Users can edit existing blog posts.

Delete Post
Users can delete blog posts.

View Posts
Everyone can read published blog posts.

Database
The project uses SQLite database:
blog.db
Flask automatically creates the database on first run.

# Requirements
Create a requirements.txt file:
Flask
Flask-SQLAlchemy
Flask-Login
Werkzeug
# Author
Riya Parvin
# License
This project is open-source and free to use.
