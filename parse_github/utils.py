import requests


def get_csv():
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'

    r = requests.get(url)
    r.raise_for_status()

    return r.text
