import requests

def get_top_regions():
    # API endpoint
    endpoint = "https://api.worldbank.org/v2/region?format=json"

    # Make a GET request to the API
    response = requests.get(endpoint)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract regions from the response
        regions = data[1]

        # Sort regions alphabetically by iso2code
        sorted_regions = sorted(regions, key=lambda x: x['iso2code'])

        # Output the names of the first 5 regions
        for region in sorted_regions[:5]:
            print(region['name'])
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    get_top_regions()
