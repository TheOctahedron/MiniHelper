from core import run_api

API_COMMANDS = {
    "run_api": {"command_function": run_api, 
        "args_need": "2 (a: str, b: str)",
        "description": "Based on httpx accepts args: 'a': API key, 'b': URL. sends a GET request and returns the formatted API response"},
}