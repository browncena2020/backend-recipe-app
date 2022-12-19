from api import app
import pytest

def test_create_recipe(testing_client):
    response = testing_client.post('/recipe', json={
        'name': 'Butter Chicken',
        'ingredients': 'Chicken, Yogurt, Butter Chicken Spices, Onion, Garlic, Tomatoes, Butter',
        'instructions': 'Cut the chicken into cubes. Marinate chicken with yogurt, minced garlic and butter chicken spices. Rest in fridge for 30 min. Put a pan on medium-high heat and cook the chicken 80%. Take the chicken out, and put butter on the pan. Cook the tomatoes, onions and garlic together. Blend it all up, then add the chicken. Add yogurt and let it simmer for 10 min on low heat.'
    })
    assert response.status_code == 200

def test_get_recipes(testing_client):
    response = testing_client.get('/recipe')
    assert response.status_code == 200
   
def test_get_recipe(testing_client):
    response = testing_client.get('/recipe/1')
    assert response.status_code == 200
    assert response.json == {
        'id': 1,
        'name': 'Butter Chicken',
        'ingredients': 'Chicken, Yogurt, Butter Chicken Spices, Onion, Garlic, Tomatoes, Butter',
        'instructions': 'Cut the chicken into cubes. Marinate chicken with yogurt, minced garlic and butter chicken spices. Rest in fridge for 30 min. Put a pan on medium-high heat and cook the chicken 80%. Take the chicken out, and put butter on the pan. Cook the tomatoes, onions and garlic together. Blend it all up, then add the chicken. Add yogurt and let it simmer for 10 min on low heat.'
    }

