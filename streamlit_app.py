import pandas as pd
import requests
import streamlit as st

from functions import get_location, get_hotels

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


# Search Locations
if st.checkbox('Set Location'):
    destination_id = get_location(city)


# Search hotels
if st.checkbox('Search'):
    hotel_response = get_hotels(destination_id, checkin_date, checkout_date, adults_number, room_number)


if st.checkbox('Display Dataframe'):
    st.text('List Ordered by Popularity')
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

st.dataframe(hotel_price_df, 1200)
