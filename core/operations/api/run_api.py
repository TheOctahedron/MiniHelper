import httpx
from core.operations.api.format_response import format_response
    
def run_api(a, b):
    API_KEY = str(a)
    URL = str(b)

    try:
        response = httpx.get( # sends an HTTP GET request
            URL, # The address of the API endpoint to which the request is sent.
            headers={ # HTTP headers that are sent to the server along with a request.
                # Authorization data is transmitted here.

                # Bearer is an authorization scheme that indicates to the server that an access token follows.
                "Authorization": f"Bearer {API_KEY}" 
            },
            timeout=8 # Maximum waiting time.
        )
        response.raise_for_status() # Check the HTTP response status

    except httpx.HTTPError as e:
        print(f"ERROR: {e}")
        return None

    return format_response(response)