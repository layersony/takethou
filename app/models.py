from app import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String(255))
  firstname = db.Column(db.String(255))
  email = db.Column(db.String(255))
  age = db.Column(db.Integer)

  def __repr__(self) -> str:
      return f"{self.id} - {self.username}"
