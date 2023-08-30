import requests
from bs4 import BeautifulSoup
import nltk
import pandas as pd

# You might need to download NLTK resources if you haven't already
nltk.download('punkt')

# Read the Excel file containing URLs and URL_IDs
input_file = 'Output Data Structure.xlsx'
df_input = pd.read_excel(input_file)

data = []

for index, row in df_input.iterrows():
    url = row['URL']
    url_id = row['URL_ID']


    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        article_title = soup.find('title').get_text()  # Extract the article title
        article_text = soup.get_text()  # Extract the entire article text

        # Perform text analysis tasks using NLTK
        # Calculate the variables as described in the assignment

        # Store the calculated values in a dictionary
        analyzed_data = {

            'URL': url,
            'URL_ID': url_id,
            # Add other calculated variables here
        }
        data.append(analyzed_data)

# Create a DataFrame from the collected data
df_output = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_file = 'Output.xlsx'
df_output.to_excel(output_file, index=False)
