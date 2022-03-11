import dash
import json
from urllib.request import urlopen
import pandas as pd
import plotly.express as px
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])


geojson_url = urlopen('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/Geography-resources/MODZCTA_2010_WGS1984.geo.json')
geojson = json.load(geojson_url)

df = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/totals/data-by-modzcta.csv').assign(MODZCTA= lambda x: x['MODIFIED_ZCTA'].astype(str))

inf_f1 = px.choropleth(df,
                    geojson=geojson,
                    locations='MODZCTA',
                    featureidkey='properties.MODZCTA',
                    projection='mercator',
                    color='PERCENT_POSITIVE',
                    hover_data=['NEIGHBORHOOD_NAME']
                    )
inf_f1.update_geos(fitbounds="locations", visible=False)
inf_f1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

inf_f2 = px.choropleth(df,
                    geojson=geojson,
                    locations='MODZCTA',
                    featureidkey='properties.MODZCTA',
                    projection='mercator',
                    color='COVID_CONFIRMED_DEATH_RATE',
                    hover_data=['NEIGHBORHOOD_NAME']
                    )
inf_f2.update_geos(fitbounds="locations", visible=False)
inf_f2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})



app.layout = html.Div([
    dcc.Dropdown(options=['INFLUENZA', 'COVID-19'], value=['INFLUENZA'], id='dropdown', placeholder='Select a virus'),
    dbc.Row([
        dbc.Col(dcc.Graph(id='graph-left', figure={}), width=6),
        dbc.Col(dcc.Graph(id='graph-right', figure={}), width=6)
    ])
])


@app.callback(Output('graph-left', 'figure'),
              Output('graph-right', 'figure'),
              [Input('dropdown', 'value')])
def update_graph(dropdown):
    if dropdown == 'INFLUENZA':
        return inf_f1, inf_f2
    else:
        return cov_f1, cov_f2


if __name__ == '__main__':
    app.run_server(debug=True)

