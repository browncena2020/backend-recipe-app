from api import db


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredients = db.Column(db.Text, nullable=False)
    favorite = db.Column(db.Boolean, nullable=False, default=False)
    name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)
    instructions = db.Column(db.Text, nullable=False)

    def __init__(self, name, ingredients, instructions,  favorite, rating):
        self.name = name
        self.favorite = favorite
        self.rating = rating
        self.ingredients = ingredients
        self.instructions = instructions
