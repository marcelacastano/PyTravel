# Make necessary imports

import os
import requests
import json
from dotenv import load_dotenv

# Load .env environment variables
load_dotenv()

# Set RAPID API key
my_rapid_api_key = os.getenv("RAPID_API_KEY")


# Define function to retrieve locations from BOOKING.COM API

def booking_hotels_api(dest_type, departure_date, return_date, nr_rooms, locale_booking, random_dest_id, nr_adults):
   

    url = "https://booking-com.p.rapidapi.com/v1/hotels/search"

    querystring = {"dest_type":dest_type,
        "checkin_date":departure_date,
        "room_number": nr_rooms,
        "checkout_date": return_date,
        "order_by":"popularity",
        "dest_id": random_dest_id,
        "adults_number":nr_adults,
        "units":"imperial",
        "filter_by_currency":"USD",
        "locale":locale_booking,
        "include_adjacency":"true",
        "categories_filter_ids":"free_cancellation:1"
        }

    headers = {
        'x-rapidapi-host': "booking-com.p.rapidapi.com",
        'x-rapidapi-key': my_rapid_api_key
    }

    hotels_endpoint_response = requests.request("GET", url, headers=headers, params=querystring)

    return hotels_endpoint_response.json()