import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://devgan.in/index.php?q=murder&a=0"

# Send an HTTP GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all div elements with class "search"
    search_divs = soup.find_all('div', class_='search')

    for div in search_divs:
        # Find all text elements within the current div
        text_elements = div.stripped_strings

        # Initialize variables to hold content
        section_name = ""
        section_content = ""

        # Iterate through the text elements
        for text in text_elements:
            if "IPC" in text:
                # If "IPC" is found, it's a new section
                section_name = text
            else:
                # Otherwise, append the text to the section content
                section_content += " " + text

        # Print the section name and content
        if section_name:
            print(section_name, section_content)

else:
    print("Failed to retrieve the web page.")

# Close the HTTP response
response.close()
