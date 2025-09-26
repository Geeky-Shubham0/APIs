# Weather API

A simple and efficient weather API built with FastAPI that provides current weather information for cities worldwide using the OpenWeatherMap API.

## Features

- 🌤️ Get current weather data for any city
- 🌡️ Temperature in Celsius 
- 💧 Humidity levels
- 🌩️ Weather condition descriptions
- ⚡ Fast API responses with FastAPI
- 🔍 Simple RESTful endpoint

## Prerequisites

- Python 3.7+
- OpenWeatherMap API key (get one free at [OpenWeatherMap](https://openweathermap.org/api))

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd weather
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Get your API key from [OpenWeatherMap](https://openweathermap.org/api) and update the `api_key` variable in `weatherAPI.py`

## Security Considerations

**⚠️ Important Security Note:** The current implementation has the API key hardcoded in the source code, which is not recommended for production use.

### Recommended Security Practices:

1. **Use Environment Variables:**
   ```bash
   # Set environment variable (Windows PowerShell)
   $env:OPENWEATHER_API_KEY="your_api_key_here"
   
   # Set environment variable (Windows Command Prompt)
   set OPENWEATHER_API_KEY=your_api_key_here
   
   # Set environment variable (Linux/Mac)
   export OPENWEATHER_API_KEY="your_api_key_here"
   ```

2. **Update your code to use environment variables:**
   ```python
   import os
   from fastapi import FastAPI
   import requests

   app = FastAPI()

   api_key = os.getenv("OPENWEATHER_API_KEY")
   if not api_key:
       raise ValueError("OPENWEATHER_API_KEY environment variable is required")
   ```

3. **Use a `.env` file for local development:**
   - Install python-dotenv: `pip install python-dotenv`
   - Create a `.env` file in your project root:
     ```
     OPENWEATHER_API_KEY=your_api_key_here
     ```
   - Add `.env` to your `.gitignore` file
   - Load environment variables in your code:
     ```python
     from dotenv import load_dotenv
     load_dotenv()
     ```

4. **Never commit API keys to version control**

## Usage

### Starting the Server

Run the FastAPI server using uvicorn:

```bash
uvicorn weatherAPI:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

FastAPI automatically generates interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### API Endpoints

#### Get Weather Information

**GET** `/weather/{city}`

Returns current weather information for the specified city.

**Parameters:**
- `city` (path parameter): Name of the city to get weather for

**Example Request:**
```bash
curl http://localhost:8000/weather/London
```

**Example Response:**
```json
{
  "city": "London",
  "temperature": 18.5,
  "humidity": 65,
  "condition": "scattered clouds"
}
```

**Error Response:**
```json
{
  "error": "City not found"
}
```

## Example Usage

### Using curl
```bash
# Get weather for New York
curl http://localhost:8000/weather/New%20York

# Get weather for Tokyo  
curl http://localhost:8000/weather/Tokyo

# Get weather for Paris
curl http://localhost:8000/weather/Paris
```

### Using Python requests
```python
import requests

response = requests.get("http://localhost:8000/weather/London")
weather_data = response.json()
print(f"Temperature in {weather_data['city']}: {weather_data['temperature']}°C")
```

### Using JavaScript fetch
```javascript
fetch('http://localhost:8000/weather/London')
  .then(response => response.json())
  .then(data => {
    console.log(`Temperature in ${data.city}: ${data.temperature}°C`);
    console.log(`Condition: ${data.condition}`);
  });
```

## Response Format

The API returns weather data in the following format:

| Field | Type | Description |
|-------|------|-------------|
| `city` | string | Name of the city |
| `temperature` | number | Temperature in Celsius |
| `humidity` | number | Humidity percentage |
| `condition` | string | Weather condition description |

## Error Handling

- Returns HTTP 200 with error message in JSON format when city is not found
- Invalid city names return `{"error": "City not found"}`

## Development

### Project Structure
```
weather/
├── weatherAPI.py      # Main FastAPI application
├── requirements.txt   # Python dependencies
└── README.md         # Project documentation
```

### Adding Features

To extend the API functionality, you can:
- Add more weather parameters (wind speed, pressure, etc.)
- Implement caching for better performance
- Add input validation and error handling
- Include weather forecasts
- Add authentication

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](../LICENSE).

## Credits

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Built with [FastAPI](https://fastapi.tiangolo.com/)