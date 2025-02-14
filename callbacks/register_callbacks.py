from dash import Input, Output, State, html, dcc
from database import supabase

def register_register_callbacks(app):
    @app.callback(
    Output('register-message', 'children'),
    Output('redirect-to-login', 'pathname'),  # Add this output for redirect
    Input('register-button', 'n_clicks'),
    State('register-username', 'value'),
    State('register-password', 'value'),
    #State('url', 'pathname'),
    allow_duplicates = True
    )
    def handle_registration(n_clicks, username, password):
        if n_clicks > 0:
            if username and password: 
                # checks if usename is already registerd in database
                response = supabase.table("test_user").select("username").eq("username", username).execute()
                if response.data:
                    print("user already exists")
                    return html.Div("Username already exists. Please choose another one.", style={"color": "red"}), None

                try:
                    insert_response = supabase.table("test_user").insert({"username": username, "password": password}).execute()
                    print(insert_response)
                    print("User registered Sucessfully")
                    
                     #Redirect to login page after successful registration
                    return html.Div("Registration successful! You can now login.", style={"color": "green"}), '/login'
                    

                    # Check if insertion was successful
                    # if insert_response. == 200:  # 201 is for successful creation
                    #     print("Supabase response data:", insert_response.data)
                    #     # Redirect to login page after successful registration
                    #     return html.Div("Registration successful! You can now login.", style={"color": "green"}), '/login'
                    # else:
                    #     print("Supabase response data:", insert_response.data)
                    #     return html.Div("An error occurred during registration. Please try again.", style={"color": "red"}), None
                
                except Exception as e:
                    # Handle any exceptions that occur during the insert operation
                    print("Error occurred during insert:", e)
                    return html.Div("An unexpected error occurred during registration. Please try again.", style={"color": "red"}), None
                


                return html.Div("Registration successful! You can now login.", style={"color": "green"}), None
            else:
                return html.Div("Please enter a username and password.", style={"color": "red"}), None
        return "", None