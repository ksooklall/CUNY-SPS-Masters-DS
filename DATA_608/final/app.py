import dash
import json
from urllib.request import urlopen
import pandas as pd
import plotly.express as px
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

geojson_url = urlopen('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/Geography-resources/MODZCTA_2010_WGS1984.geo.json')
geojson = json.load(geojson_url)

df = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/totals/data-by-modzcta.csv').assign(MODZCTA= lambda x: x['MODIFIED_ZCTA'].astype(str))

cdf = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/cases-by-day.csv', parse_dates=['date_of_interest'])
cdf = cdf.groupby(pd.Grouper(key='date_of_interest', freq='W-SAT'))['CASE_COUNT'].sum().reset_index()

idf = pd.read_csv('nyc_influenza.csv').assign(weekendingdate=lambda x: pd.to_datetime(x['weekendingdate']))

ci_df = cdf.merge(idf[['weekendingdate', 'count']], left_on='date_of_interest', right_on='weekendingdate', how='inner').\
    rename(columns={'CASE_COUNT': 'covid19','count' :'influenza', 'weekendingdate': 'week'}).\
    drop(['date_of_interest'], axis=1).\
    groupby('week').agg({'covid19': 'first', 'influenza': 'sum'}).\
    reset_index()

covid_df = ci_df[['week', 'covid19']]
influenza_df = ci_df[['week', 'influenza']]

cov_f1 = px.choropleth(df,
                    geojson=geojson,
                    locations='MODZCTA',
                    featureidkey='properties.MODZCTA',
                    projection='mercator',
                    color='PERCENT_POSITIVE',
                    hover_data=['NEIGHBORHOOD_NAME']
                    )
cov_f1.update_geos(fitbounds="locations", visible=False)
cov_f1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

cov_f2 = px.choropleth(df,
                    geojson=geojson,
                    locations='MODZCTA',
                    featureidkey='properties.MODZCTA',
                    projection='mercator',
                    color='COVID_CONFIRMED_DEATH_RATE',
                    hover_data=['NEIGHBORHOOD_NAME', 'POP_DENOMINATOR']
                    )

cov_f2.update_geos(fitbounds="locations", visible=False)
cov_f2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

inf_f1 = px.bar(idf.groupby(['weekendingdate', 'disease'])['count'].sum().reset_index(), x='weekendingdate', y='count', color='disease')
inf_f2 = px.bar(idf, x='weekendingdate', y='count', color='county')

ci_f = px.line(ci_df, x='week', y=['covid19', 'influenza'], title='Weekly virus cases')
cov_right = px.line(covid_df, x='week', y='covid19', title='Weekly Covid19 cases')
inf_right = px.line(influenza_df, x='week', y='influenza', title='Weekly Influenza cases', color_discrete_sequence=['red'])

app.layout = html.Div([
    dbc.Row([dbc.Col(html.Img(src=app.get_asset_url('covid-19.png'), style={'height': '100%', 'width': '75%'})),
             dbc.Col(html.H2('NYC Virus Tracker', style={'textAlign': 'center'}), width=4),
             dbc.Col(html.Img(src=app.get_asset_url('influenza.png'), style={'height': '100%', 'width': '75%'}))
             ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='inf_right', figure=inf_right)),
        dbc.Col(dcc.Graph(id='cv_right', figure=cov_right)),
        dbc.Col(dcc.Graph(id='ci', figure=ci_f))
    ]),
    dcc.Dropdown(options=['INFLUENZA', 'COVID-19'], value=['COVID-19'], id='dropdown', placeholder='Select a virus'),
    dbc.Row(
    [
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

