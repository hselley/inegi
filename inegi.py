import requests
import json

# Replace with your actual API token and the specific indicator/DENUE endpoint
api_token = "YOUR_INEGI_API_TOKEN"
indicator_id = "2070001" # Example indicator ID (e.g., INPC)
state_code = "09" # Example state code (e.g., Mexico City)

# Construct the API URL for an indicator
url = f"https://www.inegi.org.mx/app/api/indicadores/v1/Indicador/{indicator_id}/00000/{state_code}/json/{api_token}"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
    data = response.json()

    # Process the data (example: print the series)
    if data and 'Series' in data:
        for series_item in data['Series']:
            print(f"Indicator: {series_item['INDICADOR']}")
            for obs in series_item['OBSERVACIONES']:
                print(f"  Date: {obs['FECHA']}, Value: {obs['OBSERVACION']}")
    else:
        print("No series data found or unexpected API response structure.")

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON response: {e}")