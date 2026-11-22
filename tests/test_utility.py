import pytest, sys

# Import all utility functions.
from core.operations.utility import change_display_title, show_help

print("===============================")
print("\nRunning tests in test_utility.py\n")

# --- TESTS FOR CHANGE DISPLAY TITLE ---
def test_change_display_title():
    result = change_display_title()
    assert isinstance(result, str) # Check result is str
    assert "The display of title is" in result 
    change_display_title() # Returning to a previous state

# --- TESTS FOR CHANGE DISPLAY TITLE ---
def test_show_help():
    result = show_help("ALL")
    assert result == ""