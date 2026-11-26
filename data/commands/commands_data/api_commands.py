from core import run_api, exchange_rate

API_COMMANDS = {
    "run_api": {"command_function": run_api, 
        "args_need": "2 (api_key: str, url: str)",
        "description": "Uses httpx to send a GET request with a Bearer token and returns the formatted API response."},

        
    "exchange_rate": {"command_function": exchange_rate, 
        "args_need": "0",
        "description": "shows EUR, GBP, and RUB exchange rates."},
}