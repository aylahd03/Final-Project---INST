# Final Project

import requests
import pandas as pd

def fetch_user_data():
    api_url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2023-01-01&end_date=2023-01-07&api_key=vCxBiACkHus3CsVjMd4q98zYTVnTKAUflCB1PQ2z'

    # Make a request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON data from the response
        data = response.json()

        # Create a Pandas DataFrame from the API response
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    # Fetch user data from the API
    user_data = fetch_user_data()

    if user_data is not None:
        # Display the DataFrame
        print(user_data)

        # Optionally, perform additional analysis or visualization here

if __name__ == "__main__":
    main()
