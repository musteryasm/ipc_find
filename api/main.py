from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_sections():
    # Get the 'q' parameter from the request
    q = request.args.get('q')

    if not q:
        return "Query parameter 'q' is required.", 400

    a = '0'  # Set 'a' to always be 0

    # Construct the URL with the provided 'q' and 'a'
    url = f"https://devgan.in/index.php?q={q}&a={a}"

    # Send an HTTP GET request
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        search_divs = soup.find_all('div', class_='search')

        sections = []

        for div in search_divs:
            text_elements = div.stripped_strings
            section_name = ""
            section_content = ""

            for text in text_elements:
                if "IPC" in text:
                    section_name = text
                else:
                    section_content += " " + text

            if section_name:
                sections.append({"section_name": section_name, "section_content": section_content})

        return jsonify(sections)
    else:
        return "Failed to retrieve the web page.", 500

if __name__ == '__main__':
    app.run(debug=True)
