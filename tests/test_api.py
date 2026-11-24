# Import all api functions.
from core.operations.api import run_api

print("===============================")
print("\nRunning tests in test_api.py\n")

# --- TESTS FOR RUN API ---
def test_run_api(mocker):
    """
    'mocker' is a fixture from the `pytest-mock` plugin; it allows you to replace functions and objects during testing.
    """

    mocker.patch("builtins.input", return_value="1") # each time input() is called, it automatically returns "1"
    result = run_api(
        "key_test_1", # api_key
        "https://httpbin.org/bearer" # url
    )

    expected = {
        "authenticated": True, # the server has confirmed the presence of a valid Bearer token.
        "token": "key_test_1" # the token we provided.
    }

    assert result == expected