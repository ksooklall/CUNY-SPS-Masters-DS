import pandas as pd
from sodapy import Socrata

def _get_data():
    endpoint='https://health.data.ny.gov/resource/jr8b-6gh6.csv'
    df = pd.read_csv(endpoint)

    df.to_csv('nyc_influenza.csv', index=False)
    return df


def get_influenza_data():
    # Influenza Laboratory-Confirmed Cases

    client = Socrata('health.data.ny.gov', '0BzBtm6k3yC5kdWuUsISd69Hw')
    result= client.get('jr8b-6gh6', limit=5000)
    nyc = {'QUEENS': 'Queens', 'KINGS': 'Brooklyn', 'NEW YORK': 'Manhattan', 'RICHMOND', 'Staten Island', 'BRONX': 'Bronx'}

    # Filter for NYC
    df = pd.DataFrame.from_records(result).query('region == "NYC"')

    # Added latitude and longitude columns
    df[['latitude', 'longitude']] = pd.DataFrame(data=[i for i in df['geocoded_column'].map(lambda x: [x['latitude'], x['longitude']])], columns=['latitude', 'longitude'])
    df.to_csv('influenza.csv', index=False)
    import pdb; pdb.set_trace()

def covid_virus_data():
    data = {'hosp_death':'https://raw.githubusercontent.com/nychealth/coronavirus-data/master/latest/hosp_death_last28days-by-modzcta.csv',
            'antibody': 'https://raw.githubusercontent.com/nychealth/coronavirus-data/master/totals/antibody-by-modzcta.csv',
            'caserate': 'https://raw.githubusercontent.com/nychealth/coronavirus-data/master/totals/data-by-modzcta.csv'}
    df = pd.read_csv(data)
    pass


def covid_vaccine_data():
    data = {'allages': 'https://raw.githubusercontent.com/nychealth/covid-vaccine-data/main/people/coverage-by-modzcta-allages.csv'}

if __name__ == '__main__':
    df = get_influenza_data()
