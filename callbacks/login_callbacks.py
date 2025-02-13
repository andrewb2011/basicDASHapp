from dash import Input, Output, State, html

def register_login_callbacks(app):
    @app.callback(
        Output('login-message', 'children'),
        Input('login-button', 'n_clicks'),
        State('login-username', 'value'),
        State('login-password', 'value')
    )
    def handle_login(n_clicks, username, password):
        if n_clicks > 0:
            if username == "admin" and password == "password":  # Simple hardcoded check
                return html.Div("Login successful! Redirecting to Dashboard...", style={"color": "green"})
            else:
                return html.Div("Invalid username or password.", style={"color": "red"})
        return ""