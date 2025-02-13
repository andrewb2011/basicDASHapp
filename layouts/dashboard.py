from dash import html, dcc
import dash_bootstrap_components as dbc

dashboard_layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Dashboard Page", className="text-center mt-4"))),
    dbc.Row(dbc.Col(html.Div(id="dashboard-content", className="text-center"))),
    dbc.Row(dbc.Col(dcc.Link('Go back to Homepage', href='/', className="btn btn-link d-block text-center"))),
], fluid=True)