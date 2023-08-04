"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL ='https://tinyurl.com/demo-cupcake'

class Cupcake(db.Model):
    __tablename__='cupcakes'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    flavor = db.Column(db.Text, nullable=True)
    size = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    image = db.Column(db.Text, nullable=True, default=DEFAULT_IMAGE_URL)
    def cupcakedict(self):
        return {'id':self.id, 'flavor':self.flavor, 'size':self.size, 'rating': self.rating, 'image':self.image}


def connect_db(app):
    db.app = app
    db.init_app(app)