import httpx
from core.operations.api.format_response import format_response
    
def run_api(api_key, url):
    api_key = str(api_key).strip()
    url = str(url).strip()
    
    try:
        response = httpx.get( # sends an HTTP GET request
            url, # The address of the API endpoint to which the request is sent.
            headers={ # HTTP headers that are sent to the server along with a request.
                # Authorization data is transmitted here.

                # Bearer is an authorization scheme that indicates to the server that an access token follows.
                "Authorization": f"Bearer {api_key}" 
            },
            timeout=8 # Maximum waiting time.
        )
        response.raise_for_status() # Check the HTTP response status

    except httpx.HTTPError as error:
        print(f"ERROR: {error}")
        return None

    return format_response(response)