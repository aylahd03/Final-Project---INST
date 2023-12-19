# Final Project

import openaq
import pandas as pd
import matplotlib as plt

def openaq_data(api_key, city, parameter, date_from, date_to):
    aq_data = openaq.OpenAQ(api_key=api_key)
    
    #Getting the measurements we want from the api
    measurements = aq_data.measurements(city=city, parameter=parameter, date_form=date_from, date_to=date_to)
    
    # pulling the data we want to use in our visualization
    data = []
    for result in measurements['results']:
        row = {
            'date': result['date']['utc'],
            'value': result['value'],
            'unit': result['unit']  
        }
        data.append(row) 
   
    # Creating a data frame from what we've pulled
    data_frame = pd.DataFrame(data)
    data_frame['date'] = pd.to.datetime(data_frame['date'])
    
    return data_frame









