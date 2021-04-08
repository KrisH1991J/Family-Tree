from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

# class Grandparent(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(250), nullable=False)
#     last_name = db.Column(db.String(250), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))
#     parent = db.relationship(Parent)
#     child_id = db.Column(db.Integer, db.ForeignKey('child.id'))
#     child = db.relationship(Child)

# class Parent(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(250), nullable=False)
#     last_name = db.Column(db.String(250), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     grandparent_id = db.Column(db.Integer, db.ForeignKey('grandparent.id'))
#     grandparent = db.relationship(Grandparent)
#     child_id = db.Column(db.Integer, db.ForeignKey('child.id'))
#     child = db.relationship(Child)

# class Child(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(250), nullable=False)
#     last_name = db.Column(db.String(250), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     grandparent_id = db.Column(db.Integer, db.ForeignKey('grandparent.id'))
#     grandparent = db.relationship(Grandparent)
#     parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))
#     parent = db.relationship(Parent)