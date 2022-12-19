from api.models import Recipe
import pytest

def test_create_recipe():
    recipe = Recipe('Butter Chicken', 'Chicken, Yogurt, Butter Chicken Spices, Onion, Garlic, Tomatoes, Butter', 'Cut the chicken into cubes. Marinate chicken with yogurt, minced garlic and butter chicken spices. Rest in fridge for 30 min. Put a pan on medium-high heat and cook the chicken 80%. Take the chicken out, and put butter on the pan. Cook the tomatoes, onions and garlic together. Blend it all up, then add the chicken. Add yogurt and let it simmer for 10 min on low heat.')
    assert recipe.name == 'Butter Chicken'
    assert recipe.ingredients == 'Chicken, Yogurt, Butter Chicken Spices, Onion, Garlic, Tomatoes, Butter'
    assert recipe.instructions == 'Cut the chicken into cubes. Marinate chicken with yogurt, minced garlic and butter chicken spices. Rest in fridge for 30 min. Put a pan on medium-high heat and cook the chicken 80%. Take the chicken out, and put butter on the pan. Cook the tomatoes, onions and garlic together. Blend it all up, then add the chicken. Add yogurt and let it simmer for 10 min on low heat.'