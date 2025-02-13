from dash import html, dcc
import dash_bootstrap_components as dbc

homepage_layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Homepage", className="text-center mt-4"))),
    dbc.Row(dbc.Col(html.P("Welcome to the Homepage!", className="text-center"))),
    dbc.Row(dbc.Col(dcc.Link('Go to Login', href='/login', className="btn btn-primary btn-lg d-block mx-auto my-2", style={"width": "200px"}))),
    dbc.Row(dbc.Col(dcc.Link('Go to Register', href='/register', className="btn btn-secondary btn-lg d-block mx-auto my-2", style={"width": "200px"}))),
    dbc.Row(dbc.Col(dcc.Link('Go to Dashboard', href='/dashboard', className="btn btn-info btn-lg d-block mx-auto my-2", style={"width": "200px"}))),
], fluid=True)
