from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("./formatted_data.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales ($)"}
)

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50', 'fontFamily': 'Arial'}
    ),

    html.Div(children='''
        An analysis of Soul Foods sales before and after the January 15, 2021 price increase.
    ''', style={'textAlign': 'center', 'marginBottom': '20px'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
