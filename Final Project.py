# Final Project

import requests
import pandas as pd
import json

# api url to pull data from NASA
def pull_user_data():
    api_url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2023-01-01&end_date=2023-01-07&api_key=vCxBiACkHus3CsVjMd4q98zYTVnTKAUflCB1PQ2z'

    # request to the API
    response = requests.get(api_url)

    # check if the request was successful (status code 200)
    if response.status_code == 200:
        # JSON parses data from the response
        data = response.json()

        # create a Pandas DataFrame from the API response
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error: {response.status_code}")
        return None
 # if request wasn't sucessful it will give back an error

def main():
    # pull user data from the API
    user_data = pull_user_data()

    if user_data is not None:
        # show the DataFrame
        print(user_data)


if __name__ == "__main__":
    main()

# I had to do some outside research to understand things like the status code and embedding 
    # the api url
