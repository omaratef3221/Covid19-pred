import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np
import sys

covid19 = pd.read_csv('covid19.csv')

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer2 = SimpleImputer(missing_values=np.nan, strategy='mean')
# imputer3 = SimpleImputer(missing_values=np.nan, strategy='median')

covid19[['age']] = imputer.fit_transform(covid19[['age']])
# covid19[['date_onset_symptoms']] = imputer3.fit_transform(covid19[['date_onset_symptoms']])
# covid19[['date_admission_hospital']] = imputer3.fit_transform(covid19[['date_admission_hospital']])
covid19[['age']] = covid19[['age']].apply(np.ceil)
covid19['sex'].replace({"female": 1, "male": 2}, inplace=True)
covid19[['sex']] = imputer2.fit_transform(covid19[['sex']])
covid19[['sex']] = covid19[['sex']].apply(np.ceil)

covid19['fever'] = covid19['symptoms'].str.find('fever')
covid19.loc[covid19['fever'] >= 0, 'fever'] = 1
covid19.loc[covid19['fever'] < 0, 'fever'] = 0
covid19['fever'].fillna(0, inplace=True)

covid19['malaise'] = covid19['symptoms'].str.find('malaise')
covid19.loc[covid19['malaise'] >= 0, 'malaise'] = 1
covid19.loc[covid19['malaise'] < 0, 'malaise'] = 0
covid19['malaise'].fillna(0, inplace=True)

covid19['headache'] = covid19['symptoms'].str.find('headache')
covid19.loc[covid19['headache'] >= 0, 'headache'] = 1
covid19.loc[covid19['headache'] < 0, 'headache'] = 0
covid19['headache'].fillna(0, inplace=True)

covid19['chills'] = covid19['symptoms'].str.find('chills')
covid19.loc[covid19['chills'] >= 0, 'chills'] = 1
covid19.loc[covid19['chills'] < 0, 'chills'] = 0
covid19['chills'].fillna(0, inplace=True)

covid19['cough'] = covid19['symptoms'].str.find('cough')
covid19.loc[covid19['cough'] >= 0, 'cough'] = 1
covid19.loc[covid19['cough'] < 0, 'cough'] = 0
covid19['cough'].fillna(0, inplace=True)

covid19['fatigue'] = covid19['symptoms'].str.find('fatigue')
covid19.loc[covid19['fatigue'] >= 0, 'fatigue'] = 1
covid19.loc[covid19['fatigue'] < 0, 'fatigue'] = 0
covid19['fatigue'].fillna(0, inplace=True)

covid19.drop("symptoms", axis=1, inplace=True)
covid19.drop("country", axis=1, inplace=True)

cov = covid19.dropna(subset= ['date_onset_symptoms','date_admission_hospital','date_confirmation'])

cov.to_csv('covid19_Final.csv', index =False)
stats = cov.describe(include= 'all')
stats.to_csv('descriptive_stats.csv')