import httpx

from core.operations.api.format_response import format_response

def exchange_rate(*args):
    url = "https://api.frankfurter.dev/v2/rates?base=USD&quotes=EUR,GBP,RUB"

    response = httpx.get(url, timeout=8)
    response.raise_for_status()
    return format_response(response)