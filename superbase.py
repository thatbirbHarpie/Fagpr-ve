from dotenv import load_dotenv
import os
import json
from supabase import create_client, Client

load_dotenv(dotenv_path=".env.local")

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

with open("result_data.json", "r", encoding="utf-8") as f:
    result = json.load(f)

data = supabase.table("results").insert({
    "original": result["original"],
    "transcribed": result["transcribed"],
    "score": result["score"]
}).execute()
