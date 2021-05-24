import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import numpy as np

test_date = '2021-05-21 11:13:00'

taxiFareApiUrl = 'http://localhost:8000/predict'

'''
'''

st.markdown('''
Hello, welcome to the Taxi Fare prediction!
''')

'''

'''

pickup_datetime = st.text_input('What date and what time?',
                                value='2021-05-21 11:13:00')
pickup_longitude = st.number_input('What is your pickup longitude?',
                                   value = "1")
pickup_latitude = st.number_input('What is your pickup latitude?', value="1")
dropoff_longitude = st.number_input('What is your dropoff longitude?',
                                    value="2")
dropoff_latitude = st.number_input('What is your dropoff latitude?', value="2")
passenger_count = st.number_input('What is your passenger count', value="1")

url = 'https://taxifare.lewagon.ai/predict'

if taxiFareApiUrl == 'https://taxifare.lewagon.ai/predict':

    st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
    )

params = {
    "pickup_datetime": pickup_datetime,
        "pickup_longitude": float(pickup_longitude),
            "pickup_latitude": float(pickup_latitude),
            "dropoff_longitude": float(dropoff_longitude),
            "dropoff_latitude": float(dropoff_latitude),
            "passenger_count": int(passenger_count)
}

'''
3. Let's call our API using the `requests` package...
'''
r = requests.get(url, params=params).json()

st.write(r["prediction"])
