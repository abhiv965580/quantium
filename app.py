# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
data = pd.read_csv("output.csv")
data = data.sort_values(by='Date')


def line_chart(data):
    fig = px.line(data, x='Date', y='Sales', title='Sales of Pink Morsel')
    return fig


visualizer = dcc.Graph(
    id='visualizer',
    figure=line_chart(data)
)
header = html.H1(
    "Region Wise Pink Morsel Chart",
    id="header"
)
reg_picker = dcc.RadioItems(
    ['north', 'east', 'west', 'south', 'all'],
    'north',
    id='reg_picker',
    inline=True
)


@app.callback(
    Output(visualizer, 'figure'),
    Input(reg_picker, 'value')
)
def graph_updation(reg):
    if reg == 'all':
        trim_data = data
    else:
        trim_data = data[data['Region'] == reg]
    fig = line_chart(trim_data)
    return fig


app.layout = html.Div(
    [
        header,
        visualizer,
        reg_picker
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
