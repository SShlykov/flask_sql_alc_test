from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)


def add_test_users():
    usernames = ['user1', 'user2', 'user3', 'user4', 'user5']

    for username in usernames:
        existing_user = User.query.filter_by(username=username).first()
        if not existing_user:
            new_user = User(username=username)
            db.session.add(new_user)

    db.session.commit()


with app.app_context():
    db.create_all()
    add_test_users()
