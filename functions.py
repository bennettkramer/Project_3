import pandas as pd
import json
import requests
from dotenv import load_dotenv
import os

# Load dotenv file

load_dotenv()
booking_api_key = os.getenv('API_KEY')
headers = {
"X-RapidAPI-Key": booking_api_key,
"X-RapidAPI-Host": "booking-com.p.rapidapi.com"
}


def get_location(city):
    location_search_url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"
    location_querystring = {
    "locale":"en-gb",
    "name":city
    }

    location_response = requests.request("GET", url=location_search_url, headers=headers, params=location_querystring)

    # Obtain Destination Id
    location_data = location_response.json()
    destination_id = location_data[0]['dest_id']

    return destination_id


def get_hotels(destination_id, checkin_date, checkout_date, adults_number, room_number):
    hotel_search_url = "https://booking-com.p.rapidapi.com/v1/hotels/search"

    hotel_search_querystring = {
    "checkin_date":checkin_date,
    "checkout_date":checkout_date,
    "units":"metric",
    "dest_id":destination_id,
    "dest_type":"city",
    "locale":"en-gb",
    "adults_number":adults_number,
    "order_by":"popularity",
    "filter_by_currency":"USD",
    "room_number":room_number,
    "include_adjacency":"true"
    }

    hotel_response = requests.request("GET", url = hotel_search_url, headers = headers, params = hotel_search_querystring)

    return hotel_response

# TAO:
# Take the get_hotels function and input all the information as depicted by the booking. Then you will need to use the following line of code
# to parse out the price you're looking for:
# hotel_data = hotel_response.json()
# hotel_data['result'][i]['price_breakdown']['all_inclusive_price']