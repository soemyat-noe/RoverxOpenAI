from openai import AzureOpenAI
import os
import requests
import json

client = AzureOpenAI(
    api_key=os.getenv("AZURE_KEY"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    api_version="2023-10-01-preview"
)

def get_mars_photos(rover, date):
    api_key = os.getenv("NASA_API_KEY")
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos"
    params = {
        "earth_date": date,
        "api_key": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        photos = data.get("photos", [])
        if photos:
            return [photo["img_src"] for photo in photos[:5]]  
        else:
            return ["No photos found for this date."]
    else:
        return [f"Error: {response.status_code} - {response.reason}"]

messages = [
    {"role": "system", "content": "You are a helpful bot that provides Mars rover photos."},
    {"role": "user", "content": "Give me photos from the Curiosity rover for 2023-12-01."}
]

tools = [
    {
        "type": "function",  
        "name": "get_mars_photos",
        "description": "Fetches photos from a Mars rover based on the date provided.",
        "parameters": {
            "type": "object",
            "properties": {
                "rover": {"type": "string", "description": "The name of the Mars rover (e.g., Curiosity)"},
                "date": {"type": "string", "description": "The date to fetch photos from (format: YYYY-MM-DD)"}
            },
            "required": ["rover", "date"]
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

response_message = response.choices[0].message
gpt_tools = response_message.tool_calls

if gpt_tools:
    available_functions = {
        "get_mars_photos": get_mars_photos
    }
    messages.append(response_message)

    for gpt_tool in gpt_tools:
        function_name = gpt_tool.function.name
        function_to_call = available_functions.get(function_name)

        if function_to_call:
            function_parameters = json.loads(gpt_tool.function.arguments)
            try:
                function_response = function_to_call(**function_parameters)
            except Exception as e:
                function_response = f"Error calling function: {e}"

            messages.append({
                "tool_call_id": gpt_tool.id,
                "role": "tool",
                "name": function_name,
                "content": json.dumps(function_response) 
            })

            second_response = client.chat.completions.create(
                model="gpt-4",
                messages=messages
            )
            print(second_response.choices[0].message.content)
else:
    print(response_message.content)