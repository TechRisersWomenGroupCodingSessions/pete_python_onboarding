import pytest
from  baker import cake

# STEP 1: write the production code to ensure the test passes. 
def test_returns_0_if_no_ingredients_available():
    available = {}
    recipe = {"flour": 400}
    max_cakes = cake(available, recipe)
    assert max_cakes == 0

# STEP 2: now it's time to write your own tests.
def test_returns_2_cakes_if_double_apples():
    available = {"apples": 6}
    recipe = {"apples": 3}
    max_cakes = cake(available, recipe)
    assert max_cakes == 2

def test_returns_2_full_cakes():
    available =  {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    max_cakes = cake(available, recipe)
    assert max_cakes == 2

# def test_returns_0_if_incomplete_ingredients():
#     available =  {"sugar": 500, "flour": 2000, "milk": 2000}
#     recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
#     max_cakes = cake(available, recipe)
#     assert max_cakes == 0


