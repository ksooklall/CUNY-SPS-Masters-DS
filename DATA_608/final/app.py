import dash
import pandas as pd
import plotly.express as px
import geopandas as gpd

"""
Plot count by county for each disease
"""

#geojson_url = urlopen('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/Geography-resources/MODZCTA_2010_WGS1984.geo.json')

#geojson = json.load(geojson_url)

gdf = gpd.read_file('MODZCTA_2010.shp', SHAPE_RESTORE_SHX='YES')
gdf['MODZCTA'] = gdf['MODZCTA'].astype(int)
df = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/totals/data-by-modzcta.csv')

df = gdf.merge(df, right_on = 'MODIFIED_ZCTA', left_on = 'MODZCTA')
df.to_crs('EPSG:4326', inplace=True)


import pdb; pdb.set_trace()
fig = px.choropleth(df_merge_recent_count,
                    geojson=df_merge_recent_count.geometry,  # use geometry of df to map
                    locations=df_merge_recent_count.index,   # index of df
                    color='Weekly Count',                    # identify representing column
                    hover_name='NEIGHBORHOOD_NAME',          # identify hover name
                    animation_frame='Week Number ',          # identify date column
                    color_continuous_scale = 'purples',      # select prefer color scale
                    range_color=[0,100],                     # set range of color bar
                    center={'lat': 40.7128, 'lon': 74.0060}, # set centerpoint of map
                    title='NYC COVID Count October 2020',    # title map
                    width=1400,                              # set size
                    height=1050
                     )
fig.show()
