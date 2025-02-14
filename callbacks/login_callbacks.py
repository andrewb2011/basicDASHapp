from dash import Input, Output, State, html, dcc
from database import supabase


def register_login_callbacks(app):
    @app.callback(
        [Output('login-message', 'children'),
         Output('login-state', 'data'),
         Output('url', 'pathname')],  # Redirect to dashboard on successful login
        Input('login-button', 'n_clicks'),
        State('login-username', 'value'),
        State('login-password', 'value'),
        State('login-state', 'data'),
        prevent_initial_call=True  # Prevent the callback from running on page load
    )
    def handle_login(n_clicks, username, password, login_state):
        # Ensure the callback only runs when the button is clicked
        if n_clicks is None or n_clicks == 0:
            return "", login_state, "/login"  # Default return values

        # Check if username or password is empty
        if not username or not password:
            return (
                html.Div("Please enter both username and password.", style={"color": "red"}),
                login_state,
                "/login"  # Stay on the login page
            )

        # Query Supabase users table
        try:
            response = supabase.table("test_user").select("*").eq("username", username).eq("password", password).execute()

            print("Supabase response data:", response.data)
            # Check if user exists
            if response.data and len(response.data) > 0:
                login_state['is_logged_in'] = True  # Update login state
                return (
                    html.Div("Login successful! Redirecting to Dashboard...", style={"color": "green"}),
                    login_state,
                    "/dashboard"  # Redirect to dashboard
                )
            else:
                return (
                    html.Div("Invalid username or password.", style={"color": "red"}),
                    login_state,
                    "/login"  # Stay on the login page
                )
        except Exception as e:
            return (
                html.Div(f"An error occurred: {str(e)}", style={"color": "red"}),
                login_state,
                "/login"  # Stay on the login page
            )


# def register_login_callbacks(app):
#     @app.callback(
#         [Output('login-message', 'children'),
#          Output('login-state', 'data'),
#          Output('url', 'pathname')],  # Redirect to dashboard on successful login
#         Input('login-button', 'n_clicks'),
#         State('login-username', 'value'),
#         State('login-password', 'value'),
#         State('login-state', 'data')
#         #prevent_initial_call=True  # Prevent function from running on page load
#     )
#     def handle_login(n_clicks, username, password, login_state):
#         # Show the error message only if the button is clicked and the fields are empty
#         if n_clicks > 0:
#             if not username or not password:
#                 return (
#                     html.Div("Please enter both username and password.", style={"color": "red"}),
#                     login_state,
#                     "/login"  # Stay on the login page
#                 )

#             # Query Supabase users table
#             response = supabase.table("test_user").select("*").eq("username", username).eq("password", password).execute()

#             # Check if user exists
#             if response.data and len(response.data) > 0:
#                 login_state['is_logged_in'] = True  # Update login state
#                 return (
#                     html.Div("Login successful! Redirecting to Dashboard...", style={"color": "green"}),
#                     login_state,
#                     "/dashboard"  # Redirect to dashboard
#                 )
#             else:
#                 return (
#                     html.Div("Invalid username or password.", style={"color": "red"}),
#                     login_state,
#                     "/login"  # Stay on the login page
#                 )

#         # Return empty message and stay on login page if no button click
#         # return "", login_state, "/login"