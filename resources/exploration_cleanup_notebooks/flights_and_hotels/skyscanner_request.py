# Make necessary imports
import os
import requests
import json
from dotenv import load_dotenv

# Load .env environment variables
load_dotenv()

# Set RAPID API key
my_rapid_api_key = os.getenv("RAPID_API_KEY")


# Define function to use skyscanner API

def skyscanner_api(market_country, departure_date, return_date, departure_airport, destination_airport, locale_skyscanner, currency):

    base_url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/"
    request_url= base_url + f"{market_country}/{currency}/{locale_skyscanner}/{departure_airport}-sky/{destination_airport}-sky/{departure_date}"

    querystring = {"inboundpartialdate":return_date}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': my_rapid_api_key
    }

    response = requests.request("GET", request_url, headers=headers, params=querystring)

    return response.json()