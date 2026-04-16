from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("./formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

app = Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'padding': '40px', 'fontFamily': 'sans-serif'}, children=[
    
    html.H1(
        children='Pink Morsel Sales Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '10px'}
    ),

    html.Div(
        children='Select a region to filter the data:',
        style={'textAlign': 'center', 'fontWeight': 'bold', 'color': '#7f8c8d', 'marginBottom': '20px'}
    ),

    html.Div(style={'textAlign': 'center', 'marginBottom': '40px'}, children=[
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            inline=True,
            inputStyle={"margin-right": "5px", "margin-left": "20px"}
        )
    ]),

    html.Div(style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px', 'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'}, children=[
        dcc.Graph(id='sales-line-chart')
    ])
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        title=f"Pink Morsel Sales: {selected_region.capitalize()} Region",
        line_shape="spline", # Makes the line look smoother
        render_mode="svg"
    )
    
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_color='#2c3e50',
        margin=dict(l=40, r=40, t=60, b=40)
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)