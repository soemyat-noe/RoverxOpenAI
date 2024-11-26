# RoverxOpenAI 



## Overview

The RoverxOpenAI project allows users to interact with the Mars Rover photos API, fetching images from various Mars rovers based on specified dates. The project integrates OpenAI's function calling feature to process user queries and retrieve photos from the NASA Mars rover image database.

## Features

- Fetch Mars rover photos from NASA's API
- Use OpenAI's function calling to dynamically fetch data
- Simple interface for interacting with the rover photos API

## Prerequisites

Ensure the following are installed and configured before running the project:

- Python 3.6 or higher
- OpenAI API credentials (Azure configuration or standard OpenAI)
- NASA API key (for fetching Mars photos)

## Installation

### 1. Clone the repository:

```
git clone https://github.com/soemyat-noe/RoverxOpenAI.git
cd RoverxOpenAI
```

### 2. Set up a virtual environment:

```
virtualvenv venv
source venv/Scripts/activate  # For Windows
source venv/bin/activate  # For macOS/Linux
```

### 3. Install required dependencies:

```
pip install -r requirements.txt
```

### 4. Set up your API keys:

- Create a `nasa-api-key.json` file in the project root with the following content:

```
{
  "nasa_api_key": "YOUR_NASA_API_KEY"
}
```

- Set up your OpenAI Azure API Key and Endpoint:
  - **AZURE_KEY**: Your Azure API Key
  - **AZURE_ENDPOINT**: Your Azure Endpoint URL (e.g., `https://your-endpoint.openai.azure.com/`)

### 5. Run the project:

```
python Rover_bot.py
```

### 6. Interact with the system:

You will be prompted to input the rover name (e.g., Curiosity) and the date (e.g., 2022-12-01) to fetch photos from that date.

## Functionality Overview

### `get_mars_photos`

This function fetches images from the NASA Mars Rover Photos API based on the provided rover name and date. It returns a list of image URLs that you can use to display the Mars rover images.

### OpenAI Integration

The project integrates OpenAI’s function calling feature to process user input, like asking for photos from a specific rover on a particular date. OpenAI will handle the user’s query, determine if a function call is needed, and fetch the data using the `get_mars_photos` function.

## Example Query

User: "Give me photos from the Curiosity rover for 2022-12-01."

Response: A list of URLs of the Mars Rover photos that match the request.

## Files

- **Rover_bot.py**: Main script for interacting with the API and OpenAI.
- **nasa-api-key.json**: File containing your NASA API key (DO NOT push to GitHub).
- **requirements.txt**: Python dependencies required for the project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.