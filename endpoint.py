import requests
from bs4 import BeautifulSoup

# Send a GET request to the World Bank API endpoint
url = "https://api.worldbank.org/v2/region?format=json"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    regions_data = response.json()

    # Extract the relevant information (name and iso2code) for each region
    regions = [(region['iso2code'], region['name']) for region in regions_data[1]]

    # Sort the regions alphabetically by iso2code
    sorted_regions = sorted(regions, key=lambda x: x[0])

    # Display the first 5 entries in the sorted list
    for iso2code, name in sorted_regions[:5]:
        print(f"{iso2code}: {name}")

    # Save the output as an HTML file
    with open("index.html", "w") as html_file:
        # Create a simple HTML document with the sorted regions
        html_content = "<html><body><ul>"
        for iso2code, name in sorted_regions[:5]:
            html_content += f"<li>{iso2code}: {name}</li>"
        html_content += "</ul></body></html>"

        # Write the HTML content to the file
        html_file.write(html_content)

    print("Output saved as index.html")
else:
    # Print an error message if the request was not successful
    print(f"Error: Unable to retrieve data (status code: {response.status_code})")

