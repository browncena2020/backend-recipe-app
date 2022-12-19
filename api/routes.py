
from api import db, app
from api.models import Recipe
from flask import request

@app.route('/recipe/<int:id>', methods=['PUT'])
def update_recipe(id):
  recipe = Recipe.query.get(id)
  data = request.json
  recipe.name = data['name']
  recipe.ingredients = data['ingredients']
  recipe.instructions = data['instructions']
  recipe.rating = data['rating']
  recipe.favorite = data['favorite']
  db.session.commit()
  return { 'success': True }

@app.route('/recipe', methods=['POST'])
def create_recipe():
  data = request.json
  #print(data)
  recipe = Recipe(name=data['name'], ingredients=data['ingredients'], instructions=data['instructions'], rating=data['rating'], favorite=data['favorite'])
  db.session.add(recipe)
  db.session.commit()
  return { 'id': recipe.id }

@app.route('/recipe/<int:id>', methods=['GET'])
def get_recipe(id):
  recipe = Recipe.query.get(id)
  return format_recipe(recipe)

@app.route('/recipe/<int:id>', methods=['DELETE'])
def delete_recipe(id):
  recipe = Recipe.query.get(id)
  db.session.delete(recipe)
  db.session.commit()
  return { 'success': True }


@app.route('/skull', methods=['GET'])
def skull():
    return '💀'
  
@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipe = Recipe.query.all()
    return {'recipe': [format_recipe(i) for i in recipe]}

def format_recipe(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions,
        'rating': recipe.rating,
        'favorite':recipe.favorite,
        
    }
