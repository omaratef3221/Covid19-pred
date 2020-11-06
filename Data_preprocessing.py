import pandas as pd
import numpy as np
covid_original1 = pd.read_csv('COVID19_open_line_list.csv', delimiter=',')
#Removing non important attributes from file 1
def cleandata():
    covid_original1.pop('city')
    covid_original1.pop('wuhan(0)_not_wuhan(1)')
    covid_original1.pop('longitude')
    covid_original1.pop('latitude')
    covid_original1.pop('geo_resolution')
    covid_original1.pop('lives_in_Wuhan')
    covid_original1.pop('travel_history_dates')
    covid_original1.pop('travel_history_location')
    covid_original1.pop('reported_market_exposure')
    covid_original1.pop('additional_information')
    covid_original1.pop('chronic_disease_binary')
    covid_original1.pop('chronic_disease')
    covid_original1.pop('date_death_or_discharge')
    covid_original1.pop('notes_for_discussion')
    covid_original1.pop('location')
    covid_original1.pop('admin1')
    covid_original1.pop('admin2')
    covid_original1.pop('admin3')
    covid_original1.pop('country_new')
    covid_original1.pop('source')
    covid_original1.pop('admin_id')
    covid_original1.pop('data_moderator_initials')
    covid_original1.pop('ID')
    covid_original1.pop('sequence_available')
cleandata()
covid_updated = covid_original1.dropna(subset= ['outcome']) #remove all rows that have NaN value
covid_updated.to_csv('covid19.csv')








#covid_original2 = pd.read_csv('latestdata.csv', delimiter=',', low_memory= False)
#def cleandata2():
#   covid_original2.pop('city')
#    covid_original2.pop('ID')
#    covid_original2.pop('longitude')
#    covid_original2.pop('latitude')
#    covid_original2.pop('geo_resolution')
#    covid_original2.pop('lives_in_Wuhan')
#    covid_original2.pop('travel_history_dates')
#    covid_original2.pop('travel_history_location')
#    covid_original2.pop('reported_market_exposure')
#    covid_original2.pop('additional_information')
#    covid_original2.pop('chronic_disease_binary')
#    covid_original2.pop('chronic_disease')
#    covid_original2.pop('date_death_or_discharge')
#    covid_original2.pop('notes_for_discussion')
#    covid_original2.pop('location')
#    covid_original2.pop('admin1')
#    covid_original2.pop('admin2')
#    covid_original2.pop('admin3')
#    covid_original2.pop('country_new')
#    covid_original2.pop('source')
#    covid_original2.pop('admin_id')
#    covid_original2.pop('data_moderator_initials')
#    covid_original2.pop('sequence_available')
#    covid_original2.pop('travel_history_binary')
#cleandata2()
#covid_updated2 = covid_original2.dropna(subset= ['outcome']) #remove all rows that have NaN value
#covid_updated2.to_csv('covid19_updated2.csv')
#merged = covid_updated.merge(covid_updated2)
#covid_all = [covid_original1,covid_original2]
#covid_all = pd.concat(covid_all,ignore_index= True)
#merged.to_csv('Covid19_All.csv')