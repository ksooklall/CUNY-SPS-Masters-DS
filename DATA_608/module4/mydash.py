import math
import os
import json

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = dash.Dash()
server = app.server

nycmap = json.load(open('nyc_neighborhoods.geojson'))
drop_cols = ['stump_diam', 'status', 'spc_latin']
df = pd.read_csv('2015_Street_Tree_Census_-_Tree_Data.csv', nrows=1000).drop(drop_cols, axis=1)
df['created_at'] = pd.to_datetime(df['created_at'])
df = df.dropna(subset=['health'])
df['nhealth'] = df['health'].map({'Poor': 0.33, 'Fair': 0.66, 'Good': 1})
df['lon'] = df['longitude'].map(math.radians)
df['lat'] = df['latitude'].map(math.radians)
df['coord'] = list(zip(df['lat'], df['lon']))

fig = px.bar(df, x="borough", y="nhealth", color="spc_common")
fig2 = px.histogram(df, x="borough", color="health", color_discrete_map={'Good': 'green', 'Poor': 'red', 'Fair': 'blue'})
#fig3 = go.Figure(data=go.Choropleth(locations=df['coord'], locationmode='USA-states'))
#fig3.update_layout(mapbox_center = {"lat": 37.0902, "lon": -95.7129})

fig3 = go.Figure(data=go.Scattergeo(lat=df['latitude'], lon=df['longitude'], geojson=nycmap))

app.layout = html.Div(children=[
    html.H1(children='NYC Trees'),

    html.Div(children='Proportion of trees are in good, fair, or poor health'),

    dcc.Graph(id='by_species', figure=fig),
    dcc.Graph(id='bh', figure=fig2),
    dcc.Graph(id='geo', figure=fig3)
])


if __name__ == '__main__':
    app.run_server(debug=True)
