import pandas as pd
import json
import requests
import streamlit as st

url = "https://api.makcorps.com/auth"
header = {'Content-Type':'application/json'}
obj = {"username":"ryanderson94","password":"Mother_fucker1"}

request = requests.post(url=url, json = obj, headers=header)

response = json.loads(request.text)
access_token = response['access_token']

authorization_key = 'JWT ' + access_token

booking_header = {}

booking_header['Authorization'] = authorization_key

booking_url = "https://api.makcorps.com/free/"
st.text(booking_header)

st.title("**Welcome to Block A Room**")
st.subheader("*Creation of Team 1*")

# Indicate the city you would like to visit
city = st.text_input('Which city would you like to search?')
start_date = st.date_input('Trip Start Date')
end_date = st.date_input('Trip End Date')
concatenated_url = booking_url + city
st.text(concatenated_url)

hotel_list = []
hotel_prices = {}
hotel_values = {}

if st.button('Search'):
    booking_request = requests.get(url = concatenated_url, headers = booking_header)

data = booking_request.json()
data = data['Comparison']
last_hotel = data[-2][0]['hotelName']

i = 0
n = 0
k = 1

while data[i][0]['hotelName'] != last_hotel:
    hotel_list.append(data[i][0]['hotelName'])
    
    while k < 6:
        if type(data[i][1][n][f'price{k}']) == str:
            hotel_prices[f'Vendor {k}'] = data[i][1][n][f'vendor{k}']
            hotel_prices[f'Price {k}'] = float(data[i][1][n][f'price{k}']) + float(data[i][1][n][f'tax{k}'])
        k += 1
        n += 1
    
    hotel_values[data[i][0]['hotelName']] = hotel_prices
    hotel_prices = {}
    i += 1
    k = 1
    n = 0

if st.button('Display List'):
    hotel_values_df = pd.DataFrame.from_dict(hotel_values)
    st.dataframe(hotel_values_df)