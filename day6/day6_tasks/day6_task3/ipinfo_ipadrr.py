# Create a program to show you ipaddress. Use ipinfo.io.

import ipinfo, json
from decouple import config

if __name__ == "__main__":
    # API token is used to authenticate you with ipinfo API
    access_token = config('access_token')
    handler = ipinfo.getHandler(access_token)

    # method accepts an IP address as an optional, 
    # positional argument. If no IP address is specified,
    # the API will return data for the IP address 
    # from which it receives the request.
    details = handler.getDetails()

    print(f"Your ip adrress os: {details.ip}")

    print("Mode details about you:")
    print(json.dumps(details.all, indent=4))
