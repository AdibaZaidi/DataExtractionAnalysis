from bs4 import BeautifulSoup
import requests
import pandas as pd

# Read the Excel file
input_data = pd.read_excel('Input.xlsx')

# Extract URLs and URL_IDs
urls = input_data['URL']
url_ids = input_data['URL_ID']

for url, url_id in zip(urls, url_ids):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract article text
    article_text = ""
    article_paragraphs = soup.find_all('p')  # Adjust this based on the HTML structure
    for paragraph in article_paragraphs:
        article_text += paragraph.get_text() + '\n'

    # Save the extracted article to a text file
    with open(f'{url_id}.txt', 'w', encoding='utf-8') as file:
        file.write(article_text)
