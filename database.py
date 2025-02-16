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



