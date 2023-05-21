from bs4 import BeautifulSoup
import requests
import pytest
import pandas as pd
import time
import tweepy
import schedule
from scraping_monkeypox import html_information, get_cases_id, get_cases_status,\
 calculate_the_status, get_country_patient, building_dictionary, dataframe_cases, confirmed_cases_each_country


#URL
URL = 'https://docs.google.com/spreadsheets/d/1CEBhao3rMe-qtCbAgJTn5ZKQMRFWeAeaiXFpBY3gbHE/htmlview#'

# Authenticate to Twitter
auth = tweepy.OAuthHandler("68Gm3e0rPYRhD0dQ3yHKm4ZCT", "uxF8Kjb6QNUJpZht4aeSp6DrtzWxphS2g9LFF5Tw3ojkQLgk9p")
auth.set_access_token("1499229071305322503-eFqytC9DyasHg53c71ucJPy1pifzZs", "wZcDzs75fNN6au5AsZkHuuul0Pu7hGDVWA8B5KVzwEBiY")
api = tweepy.API(auth)

def main():


    html_data = html_information(URL)
    all_status = get_cases_status (html_data)
    number_status = calculate_the_status (all_status)


    #to get the [countries] with their [confirmed cases number] 
    cases_countries = confirmed_cases_each_country(html_data)

    # to build a Dataframe pandas from the data of cases_countries
    descending_cases = dataframe_cases(cases_countries)

    try:
        api.verify_credentials()
        print("Authentication Successful")
    except:
        print("Authentication Error")


    # #to print the [monkeypox cases]
    #schedule.every(24).hours.do(monkeypox_cases_world(number_status))


    #to print [top 10 countries] with most monkeypox in the world
    schedule.every(10).hours.do(country_cases_world(descending_cases))
    

    



    # while True:
    #     try:
    #         #to verify the code print correctly
    #         schedule.run_pending()
    #     except tweepy.TweepError as e:
    #         raise e
            
    
    


def monkeypox_cases_world(number_status):
    
    cases = (f'\
    [#monkeypox cases around the #world]\n\
    \nConfirmed cases: {number_status[0]}\nSuspected cases: {number_status[1]}\nDiscarded cases: {number_status[2]}')

    api.update_status(cases)
    time.sleep(5000)

    



def country_cases_world(descending_cases):
    x0 = descending_cases.iloc[0]['Country']
    y0 = descending_cases.iloc[0]['Cases']
    x1 = descending_cases.iloc[1]['Country']
    y1 = descending_cases.iloc[1]['Cases']
    x2 = descending_cases.iloc[2]['Country']
    y2 = descending_cases.iloc[2]['Cases']
    x3 = descending_cases.iloc[3]['Country']
    y3 = descending_cases.iloc[3]['Cases']
    x4 = descending_cases.iloc[4]['Country']
    y4 = descending_cases.iloc[4]['Cases']
    x5 = descending_cases.iloc[5]['Country']
    y5 = descending_cases.iloc[5]['Cases']
    x6 = descending_cases.iloc[6]['Country']
    y6 = descending_cases.iloc[6]['Cases']
    x7 = descending_cases.iloc[7]['Country']
    y7 = descending_cases.iloc[7]['Cases']
    x8 = descending_cases.iloc[8]['Country']
    y8 = descending_cases.iloc[8]['Cases']
    x9 = descending_cases.iloc[9]['Country']
    y9 = descending_cases.iloc[9]['Cases']
    x10 = descending_cases.iloc[10]['Country']
    y10 = descending_cases.iloc[10]['Cases']
        
    api.update_status(f'[Top #10 Countries with most #monkeypox cases]\n\
\n\
{x0} - {y0}\n\
{x1} - {y1}\n\
{x2} - {y2}\n\
{x3} - {y3}\n\
{x4} - {y4}\n\
{x5} - {y5}\n\
{x6} - {y6}\n\
{x7} - {y7}\n\
{x8} - {y8}\n\
{x9} - {y9}\n\
{x10} - {y10}\n\
') 

    time.sleep(5000)



if __name__=="__main__":
    main()

