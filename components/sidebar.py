from dash import html
import dash_bootstrap_components as dbc

def sidebar():
    return html.Div(
        [
            html.H2("Menu", className="display-4", style={"color": "white", "textAlign": "center"}),
            html.Hr(style={"borderTop": "1px solid white"}),
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact", style={"color": "white"}),
                    dbc.NavLink("Login", href="/login", active="exact", style={"color": "white"}),
                    dbc.NavLink("Register", href="/register", active="exact", style={"color": "white"}),
                    dbc.NavLink("Dashboard", href="/dashboard", active="exact", style={"color": "white"}),
                ],
                vertical=True,
                pills=True,
                style={"marginTop": "20px"},
            ),

            html.Div(
                dbc.Button("Logout", id="logout-button", color="danger", style={"width": "100%", "display": "none"}),
                style={"marginTop": "auto", "padding": "20px"},
            ),
        ],
        style={
            "position": "fixed",
            "top": 0,
            "left": 0,
            "bottom": 0,
            "width": "25%",
            "padding": "20px",
            "backgroundColor": "blue",
            "display": "flex",
            "flexDirection": "column",
        },
    )