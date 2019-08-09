from . import db
from flask_login import UserMixin


#User class
class User(UserMixin, db.Model):

    __tablename__ = 'users'