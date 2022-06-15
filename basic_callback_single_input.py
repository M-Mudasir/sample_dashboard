from gc import callbacks
from dash import dcc, Input, Output, html, Dash
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# app.layout = html.Div(children=[
#     html.Div([
#         html.Label("input your text: "),
#         dcc.Input(
#             id="input-text",
#             value="initial text",
#             type="text"
#         )
# ]),
#     html.Br(),
#     html.Div([
#         html.Label("output of your text: "),
#         html.Div(id="output-text")
# ])
# ]
# )
# @app.callback(
#     Output(
#         component_id="output-text",
#         component_property= "children"
#     ),
#     Input(
#          component_id="input-text",
#         component_property= "value"
#     )
# )
# def text_change(input_value):
#     return str(input_value)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        df['year'].min(),
        df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider'
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig

app.run_server(port= 4050, debug = True)