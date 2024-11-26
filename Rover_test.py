import json
import requests

def load_api_key(file_path="nasa-api-key.json"):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data["nasa_api_key"]

def fetch_mars_photos(api_key, rover="curiosity", earth_date="2023-12-01"):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos"
    params = {"earth_date": earth_date, "api_key": api_key}
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("photos", [])
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        return []

def display_photos(photos):
    if photos:
        print("Mars Rover Photos:")
        for idx, photo in enumerate(photos[:5]):
            print(f"{idx + 1}. {photo['img_src']}")
    else:
        print("No photos found for the given date.")

api_key = load_api_key()
photos = fetch_mars_photos(api_key)
display_photos(photos)