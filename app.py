import dash
from dash import dcc, html
import pytz
from datetime import datetime
import random
import dash.dependencies as dd

# Dash app initialization
app = dash.Dash(__name__)
server = app.server

# Function to get the current time in a specific timezone
def get_current_time_in_timezone(tz_name):
    tz = pytz.timezone(tz_name)
    return datetime.now(tz)

# List of capital cities and their corresponding timezones
timezones = {
    "New York": "America/New_York",
    "Amsterdam": "Europe/Amsterdam",
    "Brasilia": "America/Sao_Paulo",
    "Tokyo": "Asia/Tokyo",
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "Berlin": "Europe/Berlin",
    "Ottawa": "America/Toronto",
    "Moscow": "Europe/Moscow",
    "Canberra": "Australia/Sydney",
    "Budapest": "Europe/Budapest",
    "Vienna": "Europe/Vienna",
    "Madrid": "Europe/Madrid",
    "Brussels": "Europe/Brussels",
    "Buenos Aires": "America/Argentina/Buenos_Aires",
    "Washington": "America/New_York"  # Washington is in the same timezone as New York
}

# Function to generate a random color for each city card
def random_color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

# Dash layout
app.layout = html.Div([
    html.H1("Current Times in World Capitals", style={'textAlign': 'center', 'color': 'white', 'padding': '20px'}),
    
    # Dropdown menu for selecting cities
    html.Div([
        dcc.Dropdown(
            id='city-dropdown',
            options=[{'label': city, 'value': city} for city in timezones.keys()],
            multi=True,  # Allow multiple selections
            value=['New York', 'London'],  # Default selected cities
            style={'width': '50%', 'margin': '0 auto', 'color': 'black'}
        )
    ], style={'padding': '20px'}),
    
    # Display selected cities and their times in circular cards
    html.Div(id='city-cards-container', style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center', 'padding': '20px'})
], style={'backgroundColor': 'black', 'minHeight': '100vh'})


# Callback to update city cards based on dropdown selection
@app.callback(
    dd.Output('city-cards-container', 'children'),
    [dd.Input('city-dropdown', 'value')]
)
def update_city_cards(selected_cities):
    city_cards = []
    
    for city in selected_cities:
        current_time = get_current_time_in_timezone(timezones[city])

        # Format time with seconds
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

        city_cards.append(
            html.Div([
                html.H3(city, style={'color': 'white', 'textAlign': 'center'}),
                html.P(formatted_time, style={'fontSize': '18px', 'color': 'white', 'textAlign': 'center'})
            ], style={
                'display': 'inline-block', 
                'width': '150px', 
                'height': '150px', 
                'borderRadius': '50%',  # Circular card
                'textAlign': 'center',
                'backgroundColor': random_color(),
                'padding': '20px',
                'margin': '10px',
                'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.2)'
            })
        )
    
    return city_cards


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
