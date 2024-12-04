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
    rover = rover.lower()
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
    {"role": "system", "content": "You are a helpful bot that provides Mars rover photos. If you cannot find something, check tools to call the functions available. Never say something is not available, try using functions first. Always call function"},
    {"role": "user", "content": "Give me photos from the Mars Curiosity for 2023-12-01."}
]


functions = [
    {
        "type": "function",  
        "function" : {
        "name": "get_mars_photos",
        "description": "Function that fetches photos from a specific Mars rover based on the input date, function should always be called if user asked for photos from mars rover, do not check the date range. User gives date and rover and will return pictures from mars rover on that date. Information is available from 2012 onwards.",
        "parameters": {
            "type": "object",
            "properties": {
                "rover": {"type": "string", "description": "The name of the Mars rover (e.g., Curiosity)"},
                "date": {"type": "string", "description": "The date to fetch photos from (format: YYYY-MM-DD)"}
            },
            "required": ["rover", "date"]
        }
    }
    }
]

response_openai = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    tools=functions,
    tool_choice="auto"
)

print(response_openai)
response_message = response_openai.choices[0].message
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
            print(second_response.choices[0].message)
else:
    print(response_message)