# RoverxOpenAI 



## Overview

RoverxOpenAI is your cosmic companion for exploring Mars!  🚀With this project, you can ask for photos from different Mars rovers, and OpenAI will help fetch them using the NASA Mars Rover Photos API. It's like chatting with a friendly astronaut who’s ready to share cool photos of the Red Planet. Just ask for a rover’s images from a specific date, and you'll get them back like you're on a mission to Mars.

## Features

- Fetch Mars rover photos from NASA's API
- Use OpenAI’s function calling to fetch data based on your queries
- Simple and easy-to-use interface to get photos from the rovers

## Prerequisites

Before running the project, make sure you’ve got the following:

- Python 3.6 or higher
- OpenAI API credentials (Azure setup or standard OpenAI)
- NASA API key (to grab the Mars rover photos)

## Installation

### 1. Clone the repo:

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

Interact with your friendly astronaut bot! It’ll ask you for the rover name (e.g., Curiosity) and the date (e.g., 2022-12-01) to fetch the photos.

## Functionality Overview

### `get_mars_photos`

This function grabs images from NASA’s Mars Rover Photos API based on the rover name and date you provide. It returns a list of image URLs that you can use to view the photos.

## OpenAI Integration

The OpenAI integration is what makes this fun! Chat with the bot like you're having a conversation with an astronaut. You can ask for photos from any rover on any date, and OpenAI will process your request and call the `get_mars_photos` function to get the images.

### Example Query

**User:** "Hey, Captain! Can you show me some photos from the Curiosity rover on 2022-12-01?"

**Astronaut Bot:** "Roger that! Let me send you some cool shots from Mars. Hold on, astronaut!" 🌌🚀

**Response:** A list of URLs to Mars Rover photos taken on that date.

## Files

- **Rover_bot.py:** The main script that interacts with the API and OpenAI.
- **nasa-api-key.json:** This contains your NASA API key (DO NOT push this to GitHub!).
- **requirements.txt:** A list of Python dependencies for the project.

## License

This project is licensed under the MIT License – see the LICENSE file for more details.tails.