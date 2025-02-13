from dash import html
import dash_bootstrap_components as dbc

homepage_layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Homepage", className="text-center mt-4"))),
    dbc.Row(dbc.Col(html.P("Welcome to the Homepage!", className="text-center"))),
], fluid=True)