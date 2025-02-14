from dash import Input, Output, State, html, dcc
from database import supabase

def register_register_callbacks(app):
    @app.callback(
    Output('register-message', 'children'),
    Input('register-button', 'n_clicks'),
    State('register-username', 'value'),
    State('register-password', 'value')
    )
    def handle_registration(n_clicks, username, password):
        if n_clicks > 0:
            if username and password:  
                return html.Div("Registration successful! You can now login.", style={"color": "green"})
            else:
                return html.Div("Please enter a username and password.", style={"color": "red"})
        return ""