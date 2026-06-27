import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data
df = px.data.iris()

# Sample figure
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Iris Dataset - Sepal Width vs Length")

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Sample Dashboard", style={'textAlign':'center'}),
    html.Div([
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)