import requests
from bs4 import BeautifulSoup
import re

# URL of the target page
url = 'https://locconnect.com/example'

# Perform a GET request to the page
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Search for the script tag containing the link
script = soup.find('script', text=re.compile('conf_rew'))

# Extract the link from the script
link = None
if script:
    # Use regular expression to find the link within the script
    match = re.search(r"link: '([^']+)'", script.string)
    if match:
        # Assign the found link to the variable
        link = match.group(1)

# Print the bypassed link
print(f'Bypassed Link: {link}')
