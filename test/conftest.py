import pytest
from api.models import Recipe
from api import db, app
@pytest.fixture
def  testing_client(scope='module'):
   
    db.create_all()
    recipe = Recipe('Butter Chicken', 'Chicken, Yogurt, Butter Chicken Spices, Onion, Garlic, Tomatoes, Butter', 'Cut the chicken into cubes. Marinate chicken with yogurt, minced garlic and butter chicken spices. Rest in fridge for 30 min. Put a pan on medium-high heat and cook the chicken 80%. Take the chicken out, and put butter on the pan. Cook the tomatoes, onions and garlic together. Blend it all up, then add the chicken. Add yogurt and let it simmer for 10 min on low heat.')
    db.session.add(recipe)
    db.session.commit()
    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()