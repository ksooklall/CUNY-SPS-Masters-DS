import pandas as pd
from sodapy import Socrata

def get_influenza_data():
    # Influenza Laboratory-Confirmed Cases
    #

    client = Socrata('health.data.ny.gov', '0BzBtm6k3yC5kdWuUsISd69Hw')
    result= client.get('jr8b-6gh6', limit=10000)
    #nyc = {'QUEENS': 'Queens', 'KINGS': 'Brooklyn', 'NEW YORK': 'Manhattan', 'RICHMOND', 'Staten Island', 'BRONX': 'Bronx'}

    # Filter for NYC
    df = pd.DataFrame.from_records(result).query('region == "NYC"').drop(['region'], axis=1).iloc[:, :-5]

    # Added latitude and longitude columns
    df[['latitude', 'longitude']] = pd.DataFrame(data=[i for i in df['geocoded_column'].map(lambda x: [x['latitude'], x['longitude']])], columns=['latitude', 'longitude'])
    df.to_csv('nyc_influenza.csv', index=False)
    return df


if __name__ == '__main__':
    df = get_influenza_data()
