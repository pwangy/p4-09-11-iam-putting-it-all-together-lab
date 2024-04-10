from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from config import db, bcrypt


# incorporate bcrypt to create a secure password. Attempts to access the password_hash should be met with an AttributeError.
# constrain the user's username to be present and unique (no two users can have the same username).
# have many recipes.
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)
    bio = db.Column(db.String)

    def __repr(self):
        return f'<User {self.username}>'


# a recipe belongs to a user.
# id that is an integer type and a primary key.
# title that is a String type.
# instructions that is a String type.
# minutes_to_complete that is an Integer type.

# constrain the title to be present.
# constrain the instructions to be present and at least 50 characters long.

class Recipe(db.Model, SerializerMixin):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    instructions = db.Column(db.String, nullable=False)
    minutes_to_complete = db.Column(db.Integer)

    def __repr__(self):
        return f'<Recipe {self.id}: {self.title}>'