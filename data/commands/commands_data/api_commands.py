from core import run_api

API_COMMANDS = {
    "run_api": {"command_function": run_api, 
        "args_need": "2 (api_key: str, url: str)",
        "description": "Uses httpx to send a GET request with a Bearer token and returns the formatted API response."},
}