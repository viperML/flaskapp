from flask_login import UserMixin
from portfolio import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    premium = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.image_file}', '{self.premium}')"

