import math
import os
import json

import dash
from dash import dcc, html

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

app = dash.Dash(__name__)
server = app.server

soql_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
        '$select=spc_common,created_at,health,boroname,tree_id,latitude,longitude,steward').replace(' ', '%20')
df = pd.read_json(soql_url)

df = df.dropna(subset=['health'])
df['steward'] = df['steward'].replace('None', np.nan)

fig2 = px.histogram(df[df['steward'].notnull()], x='health', color='steward')
fig1 = px.histogram(df, x="boroname", color="health", color_discrete_map={'Good': 'green', 'Poor': 'red', 'Fair': 'blue'})

fig3 = px.scatter_geo(df,
                    lat='latitude',
                    lon='longitude',
                    hover_name="tree_id",
                    color='health')

fig3.update_geos(fitbounds="locations", visible=False)
fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app.layout = html.Div(children=[
    html.H1(children='NYC Trees'),

    html.Div(children='Proportion of trees are in good, fair, or poor health'),

    dcc.Graph(id='by_species', figure=fig1),
    dcc.Graph(id='bh', figure=fig2),
    dcc.Graph(id='geo', figure=fig3)
])


if __name__ == '__main__':
    app.run_server(debug=True)
