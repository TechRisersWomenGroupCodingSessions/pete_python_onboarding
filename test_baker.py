import pytest
from  baker import cake

# STEP 1: write the production code to ensure the test passes. 
def test_returns_0_if_no_ingredients_available():
    available = {}
    recipe = {"flour": 400}
    max_cakes = cake(available, recipe)
    assert max_cakes == 0

# STEP 2: now it's time to write your own tests.