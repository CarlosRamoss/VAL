import streamlit as st
import requests
import pandas as pd



# Define function to retrieve VA facilities data for a given state
def get_va_facilities_data(state):
    url = f'https://sandbox-api.va.gov/services/va_facilities/v0/facilities?state={state}&per_page=50&page=1'
    headers = {'apikey': '2CVtH06KEgy6gwUfZC5YH6rDYbBXNcWu'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']
        df = pd.json_normalize(data)
    else:
        df = pd.DataFrame()
    return df

# Create a title
st.title('VA Facilities by State')

# Create a dropdown menu to select state
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA',
          'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
          'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
selected_state = st.selectbox('Select a state', states)

# Retrieve VA facilities data for selected state
df = get_va_facilities_data(selected_state)

# Display DataFrame
if not df.empty:
    st.write(df)
else:
    st.write('No VA facilities data available for selected state.')









