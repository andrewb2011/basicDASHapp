from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc  # For better styling
from layouts.homepage import homepage_layout
from layouts.login import login_layout
from layouts.register import register_layout
from layouts.dashboard import dashboard_layout
from callbacks.login_callbacks import register_login_callbacks
from callbacks.register_callbacks import register_register_callbacks
from callbacks.dashboard_callbacks import register_dashboard_callbacks
from components.navbar import navbar
from components.sidebar import sidebar


# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Define the app layout with dcc.Location and a container for the page content
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Tracks the URL
    dcc.Store(id='login-state', data={'is_logged_in': False}),  # Store login state
    sidebar(),
    #navbar(),
    html.Div(id='page-content')  # Container for the page content
])

# Register callbacks
register_login_callbacks(app)
register_register_callbacks(app)
register_dashboard_callbacks(app)

# Callback to update the page content based on the URL
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/':
        return homepage_layout
    elif pathname == '/login':
        return login_layout
    elif pathname == '/register':
        return register_layout
    elif pathname == '/dashboard':
        return dashboard_layout
    else:
        return dbc.Container([
            dbc.Row(dbc.Col(html.H1("404: Page Not Found", className="text-center mt-4"))),
            dbc.Row(dbc.Col(html.P(f"The path '{pathname}' was not recognized.", className="text-center"))),
            dbc.Row(dbc.Col(dcc.Link('Go back to Homepage', href='/', className="btn btn-link d-block text-center"))),
        ], fluid=True)



# Run the app
if __name__ == '__main__':
    app.run(debug=True)