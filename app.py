from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc  # For better styling
from layouts.homepage import homepage_layout
from layouts.login import login_layout
from layouts.register import register_layout
from layouts.dashboard import dashboard_layout
from callbacks.login_callbacks import register_login_callbacks
from callbacks.register_callbacks import register_register_callbacks
from callbacks.dashboard_callbacks import register_dashboard_callbacks

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define layouts for each page
# homepage_layout = dbc.Container([
#     dbc.Row(dbc.Col(html.H1("Homepage", className="text-center mt-4"))),
#     dbc.Row(dbc.Col(html.P("Welcome to the Homepage!", className="text-center"))),
#     dbc.Row(dbc.Col(dcc.Link('Go to Login', href='/login', className="btn btn-primary btn-lg d-block mx-auto my-2", style={"width": "200px"}))),
#     dbc.Row(dbc.Col(dcc.Link('Go to Register', href='/register', className="btn btn-secondary btn-lg d-block mx-auto my-2", style={"width": "200px"}))),
#     dbc.Row(dbc.Col(dcc.Link('Go to Dashboard', href='/dashboard', className="btn btn-info btn-lg d-block mx-auto my-2", style={"width": "200px"}))),
# ], fluid=True)

# login_layout = dbc.Container([
#     dbc.Row(dbc.Col(html.H1("Login Page", className="text-center mt-4"))),
#     dbc.Row(dbc.Col(
#         dbc.Card([
#             dbc.CardBody([
#                 dbc.Form([
#                     dbc.Row([
#                         dbc.Label("Username:", className="font-weight-bold"),
#                         dbc.Input(type="text", id="login-username", placeholder="Enter your username", className="mb-3"),
#                     ]),
#                     dbc.Row([
#                         dbc.Label("Password:", className="font-weight-bold"),
#                         dbc.Input(type="password", id="login-password", placeholder="Enter your password", className="mb-3"),
#                     ]),
#                     dbc.Button("Login", id="login-button", color="primary", className="w-100 mb-3"),
#                     html.Div(id="login-message", className="text-center"),  # To display login success/error messages
#                     dcc.Link('Go back to Homepage', href='/', className="btn btn-link d-block text-center"),
#                 ]),
#             ]),
#         ], className="shadow p-3 mb-5 bg-white rounded", style={"maxWidth": "400px", "margin": "auto"}),
#     )),
# ], fluid=True)

# register_layout = dbc.Container([
#     dbc.Row(dbc.Col(html.H1("Register Page", className="text-center mt-4"))),
#     dbc.Row(dbc.Col(
#         dbc.Card([
#             dbc.CardBody([
#                 dbc.Form([
#                     dbc.Row([
#                         dbc.Label("Username:", className="font-weight-bold"),
#                         dbc.Input(type="text", id="register-username", placeholder="Enter a username", className="mb-3"),
#                     ]),
#                     dbc.Row([
#                         dbc.Label("Password:", className="font-weight-bold"),
#                         dbc.Input(type="password", id="register-password", placeholder="Enter a password", className="mb-3"),
#                     ]),
#                     dbc.Button("Register", id="register-button", color="success", className="w-100 mb-3"),
#                     html.Div(id="register-message", className="text-center"),  # To display registration success/error messages
#                     dcc.Link('Go back to Homepage', href='/', className="btn btn-link d-block text-center"),
#                 ]),
#             ]),
#         ], className="shadow p-3 mb-5 bg-white rounded", style={"maxWidth": "400px", "margin": "auto"}),
#     )),
# ], fluid=True)

# dashboard_layout = dbc.Container([
#     dbc.Row(dbc.Col(html.H1("Dashboard Page", className="text-center mt-4"))),
#     dbc.Row(dbc.Col(html.Div(id="dashboard-content", className="text-center"))),
#     dbc.Row(dbc.Col(dcc.Link('Go back to Homepage', href='/', className="btn btn-link d-block text-center"))),
# ], fluid=True)

# Define the app layout with dcc.Location and a container for the page content
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Tracks the URL
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

# Callback for handling login
# @app.callback(
#     Output('login-message', 'children'),
#     Input('login-button', 'n_clicks'),
#     State('login-username', 'value'),
#     State('login-password', 'value')
# )
# def handle_login(n_clicks, username, password):
#     if n_clicks > 0:
#         if username == "admin" and password == "password":  # Simple hardcoded check
#             return html.Div("Login successful! Redirecting to Dashboard...", style={"color": "green"})
#         else:
#             return html.Div("Invalid username or password.", style={"color": "red"})
#     return ""

# Callback for handling registration
# @app.callback(
#     Output('register-message', 'children'),
#     Input('register-button', 'n_clicks'),
#     State('register-username', 'value'),
#     State('register-password', 'value')
# )
# def handle_registration(n_clicks, username, password):
#     if n_clicks > 0:
#         if username and password:  # Simple validation
#             return html.Div("Registration successful! You can now login.", style={"color": "green"})
#         else:
#             return html.Div("Please enter a username and password.", style={"color": "red"})
#     return ""

# Callback for updating the Dashboard content
# @app.callback(
#     Output('dashboard-content', 'children'),
#     Input('url', 'pathname')
# )
# def update_dashboard(pathname):
#     if pathname == '/dashboard':
#         return html.Div([
#             html.P("Welcome to your Dashboard!"),
#             html.P("Here you can view your data and analytics."),
#         ])
#     return ""

# Run the app
if __name__ == '__main__':
    app.run(debug=True)