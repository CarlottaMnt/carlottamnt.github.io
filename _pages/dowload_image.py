import requests
from bs4 import BeautifulSoup
import urllib.parse
import os

def download_images(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image elements on the page
    image_elements = soup.find_all('img')

    # Create a directory to store the downloaded images
    os.makedirs('downloaded_images', exist_ok=True)

    # Download each image
    for index, img in enumerate(image_elements):
        # Get the source URL of the image
        src = img['src']

        # Generate a unique filename for each image
        filename = f'image{index}.jpg'

        # Download the image
        try:
            response = requests.get(src, stream=True)
            response.raise_for_status()
            with open(os.path.join('downloaded_images', filename), 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {filename}: {e}")

# Replace the URL below with your desired URL
url = "https://www.google.com/search?sa=X&rlz=1C1GCEB_enLU1023LU1023&sxsrf=AB5stBjj3FIqSo8f3jlkgDVfnzvSS6yIrw:1688395270736&q=download+age+60%2B+pictures&tbm=isch&source=univ&fir=BHE2vH1iyiOEjM%252CJHTsppko8TChyM%252C_%253BfLBuMqTpzsp5oM%252CtOf0Bvg4Mk2LlM%252C_%253B3VDdP8dRg6BFnM%252CJHTsppko8TChyM%252C_%253BjTBRjCoUzWk6wM%252CyNcKC1k2bxL1-M%252C_%253BnxmosQPJMIQF5M%252C90pVjk0nvj1Q3M%252C_%253B3j-yh_nSuOUsjM%252CTfJtwKDxixcK1M%252C_%253BpKmd_PYFuad39M%252CHzvgaYLCdokKGM%252C_%253B2F4P_9v7-HX1LM%252C90pVjk0nvj1Q3M%252C_%253BAeJhUr_Qnp9A_M%252CyNcKC1k2bxL1-M%252C_%253BMtkD4DaDpUuj8M%252CtOf0Bvg4Mk2LlM%252C_&usg=AI4_-kQRjE3FX1pEaUR7nIJASs6qFB7O0A&ved=