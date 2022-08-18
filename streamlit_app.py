import pandas as pd
import requests
import streamlit as st

# Search Location by City Name
location_search_url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"
hotel_search_url = "https://booking-com.p.rapidapi.com/v1/hotels/search"
headers = {
	"X-RapidAPI-Key": "fb5b528af4mshb57de5533dbee6fp1285bfjsn290be06d9c2a",
	"X-RapidAPI-Host": "booking-com.p.rapidapi.com"
}

st.title("**Welcome to Block A Room**")
st.subheader("*Creation of Team 1*")

# Room input details
city = st.text_input('Which city would you like to search?')
col1top, col2top = st.columns(2)
with col1top:
    checkin_date = st.date_input('Check-In')
with col2top:
    checkout_date = st.date_input('Check-Out')

col1bottom, col2bottom = st.columns(2)
with col1bottom:
    adults_number = st.number_input('Number of Adults', min_value = 1, step=1)
with col2bottom:
    room_number = st.number_input('Number of Rooms', min_value = 1, step=1)

# Format the values
adults_number = str(adults_number)
room_number = str(room_number)
checkin_date = str(checkin_date)
checkout_date = str(checkout_date)

# Create Location Query Dictionary
location_querystring = {
    "locale":"en-gb",
    "name":city
}

# Search Locations
if st.button('Set Location'):
    location_response = requests.request("GET", url=location_search_url, headers=headers, params=location_querystring)

    # Obtain Destination Id
    location_data = location_response.json()
    destination_id = location_data[0]['dest_id']

    # Create Hotel Query Dictionary
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

st.text(destination_id)

# Search hotels
if st.button('Search'):
    hotel_response = requests.request("GET", url = hotel_search_url, headers=headers, params=hotel_search_querystring)


if st.button('Display Dataframe'):
    hotel_data = hotel_response.json()
    hotel_list = []
    price_list = []

    i = 0
    while i < 20:
        hotel_list.append(hotel_data['result'][i]['hotel_name'])
        price_list.append(hotel_data['result'][i]['price_breakdown']['all_inclusive_price'])
        i += 1

    final_hotel_list = [hotel_list, price_list]

    hotel_price_df = pd.DataFrame(final_hotel_list).transpose()
    hotel_price_df.columns = ['Hotel Name', 'Price']
    hotel_price_df.set_index('Hotel Name')

st.dataframe(hotel_price_df)
