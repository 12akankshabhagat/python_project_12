from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    # Example: Scraping YouTube data
    youtube_data = scrape_youtube()
       
    # Example: Scraping Amazon data
    amazon_data = scrape_amazon()

    return render_template('index.html', youtube_data=youtube_data, amazon_data=amazon_data)

def scrape_youtube():
    url = 'https://www.youtube.com'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Example: Scraping video titles
        video_titles = [a.text for a in soup.find_all('a', class_='yt-uix-tile-link')]
        return video_titles
    else:
        return ['Failed to retrieve YouTube data']

def scrape_amazon():
    url = 'https://www.amazon.com'
    headers = {
           'User-Agent': 'Your User Agent String'
       }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Example: Scraping product names
        product_names = [span.text for span in soup.find_all('span', class_='a-text-bold')]
        return product_names
    else:
        return ['Failed to retrieve Amazon data']

if __name__ == '__main__':
       app.run(host= "0.0.0.0" , port = 5004)
   
