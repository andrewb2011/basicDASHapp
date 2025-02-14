from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client


# Initialize Supabase Client

URL = os.environ.get("SUPABASE_URL")
KEY = os.environ.get("SUPABASE_KEY")

if not URL or not KEY:
    raise ValueError("Supabase credentials are missing! Check your .env file.")

supabase = create_client(URL, KEY)

def fetch_users():
    """Fetch all users from the database and print them to the terminal."""
    try:
        # Fetch data from the 'test_user' table
        response = supabase.table("test_user").select("*").execute()
        
        # Check if data was fetched
        if response.data:
            print("Fetched rows:")
            for row in response.data:
                print(row)  # Print each row to the terminal
        else:
            print("No rows found in the 'test_user' table.")
        
        return response.data  # Return the fetched data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

