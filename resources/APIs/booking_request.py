# Make necessary imports

import os
import requests
import json
from dotenv import load_dotenv

# Load .env environment variables
load_dotenv()

# Set RAPID API key
my_rapid_api_key = os.getenv("RAPID_API_KEY")


# Define function to use  BOOKING.COM API

def booking_api(city, locale):

    url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"

    querystring = {"name": {city},"locale": {locale}}

    headers = {
        'x-rapidapi-host': "booking-com.p.rapidapi.com",
        'x-rapidapi-key': my_rapid_api_key
    }

    location_endpoint_response = requests.request("GET", url, headers=headers, params=querystring)

    return location_endpoint_response.json()