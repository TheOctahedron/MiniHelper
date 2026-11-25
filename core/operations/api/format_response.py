def get_full_response(response):
    return {
        "status_code": response.status_code,
        "headers": dict(response.headers),
        "body": response.text
    }

def format_response(response):

    print("1. Json: response.json()")
    print("2. Text: response.text")
    print("3. Full: status_code, headers, body")
    response_format = input("\nWhat API response format is required? (1/2/3): ").strip()

    match response_format:
        case "1":
            try:
                return response.json() # Send it in JSON format.
            except ValueError as error:
                print(f"ERROR: {error}")
                print("Unknown format. Returning full response.")
                return get_full_response(response) # Send it in full format.
        
        case "2":
            return response.text # Send it in text format.
        case "3":
            return get_full_response(response) # Send it in full format.
        case _:
            print("Unknown format. Returning full response.")
            return get_full_response(response) # Send it in full format.