import dash
from dash import dcc, html

app = dash.Dash(__name__)
server = app.server


app.layout = html.Div([
    html.H3("Helló Világ Dash app!"),
    dcc.Graph(
        figure={
            "data": [{"x": [1, 2, 3], "y": [4, 1, 2], "type": "line"}],
            "layout": {"title": "Egyszerű grafikon"}
        }
    )
])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

