# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("output.csv")

fig = px.line(df, x='Date', y='Sales', color='Region')

app.layout = html.Div(children=[
    html.H1(children='Sales Graph of Pink Morsel'),

    html.Div(children='''
        Sales visualization in line chart of Pink Morsel region wise.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
