from dotenv import load_dotenv
import requests
import os

load_dotenv()

def buscar_alimento(query):
    # Requer uma api_key que pode ser obtida em https://fdc.nal.usda.gov/api-key-signup.html
    api_key = os.environ.get('API_KEY')
    base_url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={query}&dataType=Foundation&pageSize=21&api_key={api_key}"
    return requests.get(base_url).json()