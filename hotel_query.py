import pandas as pd
import requests
import streamlit as st

url = "https://api.makcorps.com/auth"
header = {'Content-Type':'application/json'}
obj = {"username":"randerson1994","password":"Password123"}

request = requests.post(url=url, json = obj, headers=header)

booking_url = "https://api.makcorps.com/free/"
city = 'vancouver'
concatenated_url = booking_url + city
booking_header = {'Authorization':'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjA0MTYzMTYsImlhdCI6MTY2MDQxNDUxNiwibmJmIjoxNjYwNDE0NTE2LCJpZGVudGl0eSI6MTQ5MX0.xVFmDb84hnRFDoaAJr3PRwaOnbhV0Dz37QCMTWiYLRw'}

booking_request = requests.get(url = concatenated_url, headers=booking_header)

data = booking_request.json()
data = data['Comparison']
data

booking_request_df = pd.DataFrame.from_dict(data)
print(booking_request_df)
