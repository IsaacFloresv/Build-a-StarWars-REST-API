from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id_Planet = db.Column(db.Integer, primary_key=True)
    name_Planet = db.Column(db.String(120), unique=True, nullable=False)
    is_Exist = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id_Planet": self.id_Planet,
            "name_Planet": self.name_Planet,
            "Exist": self.is_Exist,
            # do not serialize the password, its a security breach
        }

class Favorite_Planet(db.Model):
    id_Planet = db.Column(db.Integer)
    id_User = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.id_User

    def serialize(self):
        return {
            "User": self.id_User,
            "Planet": self.id_Planet,
            # do not serialize the password, its a security breach
        }