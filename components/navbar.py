from dash import html
import dash_bootstrap_components as dbc

def navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Login", href="/login")),
            dbc.NavItem(dbc.NavLink("Register", href="/register")),
            dbc.NavItem(dbc.NavLink("Dashboard", href="/dashboard")),
        ],
        brand="My App",
        brand_href="/",
        color="primary",
        dark=True,
    )