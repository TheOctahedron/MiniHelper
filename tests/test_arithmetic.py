import pytest 

# Import all arithmetic functions.
from core.operations.arithmetic import plus, minus, multiply, divide, raise_to_power, percent

print("===============================")
print("\nRunning tests in test_arithmetic.py\n")


# --- TESTS FOR DIVIDE ---
@pytest.mark.parametrize("a, b, expected", [
 (5, 2, 2.5),
 (-5, -2, 2.5),
 (-5, 2, -2.5), 
 (1.5, 3, 0.5)
])
def test_divide(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)


# --- TESTS FOR MINUS ---
@pytest.mark.parametrize("a, b, expected", [
 (5, 3, 2),
 (-5, -3, -2),
 (-5, 3, -8), 
 (1.5, 3.5, -2)
])
def test_minus(a, b, expected):
    assert minus(a, b) == pytest.approx(expected)


# --- TESTS FOR MULTIPLY ---
@pytest.mark.parametrize("a, b, expected", [
 (5, 3, 15),
 (-5, -3, 15),
 (-5, 3, -15), 
 (1.5, 3.5, 5.25)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == pytest.approx(expected)


# --- TESTS FOR PERCENT ---
@pytest.mark.parametrize("a, b, expected", [
 (50, 3, 1.5),
 (-50, -3, 1.5),
 (-50, 3, -1.5), 
 (10.5, 3.5, 0.3675)
])
def test_percent(a, b, expected):
    assert percent(a, b) == pytest.approx(expected)


# --- TESTS FOR PLUS ---
@pytest.mark.parametrize("a, b, expected", [
 (5, 3, 8),
 (-5, -3, -8),
 (-5, 3, -2), 
 (1.5, 3.5, 5)
])
def test_plus(a, b, expected):
    assert plus(a, b) == pytest.approx(expected)


# --- TESTS FOR RAISE TO POWER ---
@pytest.mark.parametrize("a, b, expected", [
 (5, 3, 125),
 (-5, -3, -0.008),
 (-5, 3, -125), 
 (1.5, 3.5, 4.133513940946613)
])
def test_raise_to_power(a, b, expected):
    assert raise_to_power(a, b) == pytest.approx(expected)


# --- TESTS FOR STRING VALUES (for argparse) ---
def test_plus_with_strings():
    # Simulating argparse passing strings instead of floats
    assert plus("5", "3") == pytest.approx(8)