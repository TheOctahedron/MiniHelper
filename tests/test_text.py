import pytest

# Import all arithmetic functions.
from core.operations.text import txt_lower, txt_reverse, txt_upper

print("===============================")
print("\nRunning tests in test_text.py\n")


# --- TESTS FOR TXT LOWER ---
@pytest.mark.parametrize("a, expected", [
 ("Octahedron", "octahedron"),
 ("octahedron", "octahedron"),
 ("OCTAHEDRON", "octahedron"), 
 ("OcTaHeDrOn", "octahedron")
])
def test_txt_lower(a, expected):
    assert txt_lower(a) == expected

# --- TESTS FOR TXT REVERSE ---
@pytest.mark.parametrize("a, expected", [
 ("Octahedron", "nordehatcO"),
 ("octahedron", "nordehatco"),
 ("OCTAHEDRON", "NORDEHATCO"), 
 ("OcTaHeDrOn", "nOrDeHaTcO")
])
def test_txt_reverse(a, expected):
    assert txt_reverse(a) == expected

# --- TESTS FOR TXT UPPER ---
@pytest.mark.parametrize("a, expected", [
 ("Octahedron", "OCTAHEDRON"),
 ("octahedron", "OCTAHEDRON"),
 ("OCTAHEDRON", "OCTAHEDRON"), 
 ("OcTaHeDrOn", "OCTAHEDRON")
])
def test_txt_upper(a, expected):
    assert txt_upper(a) == expected