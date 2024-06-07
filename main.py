import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def clear_folder(folder_name):
    for filename in os.listdir(folder_name):
        file_path = os.path.join(folder_name, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def download_images_and_extract_text(url, folder_name, max_images=6):
    # Create folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    else:
        # Clear the folder if it exists
        clear_folder(folder_name)

    # Request the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract and print text content
    text_content = soup.get_text()
    print("Extracted Text Content:")
    print(text_content)

    # Find all image tags
    img_tags = soup.find_all('img')

    # Extract image URLs
    img_urls = [urljoin(url, img['src']) for img in img_tags if 'src' in img.attrs]

    # Download and save images with incremented names, limit to max_images
    img_count = 0
    for img_url in img_urls:
        if img_count >= max_images:
            break
        # Check if the URL is an image
        img_response = requests.get(img_url, stream=True)
        if 'image' in img_response.headers.get('Content-Type', ''):
            img_count += 1
            img_name = f"img{img_count}.jpg"
            with open(os.path.join(folder_name, img_name), 'wb') as img_file:
                for chunk in img_response.iter_content(1024):
                    img_file.write(chunk)

    print(f"Downloaded {img_count} images to {folder_name}")

# Example usage
url = 'https://timesofindia.indiatimes.com/entertainment/hindi/bollywood/news/munjya-actress-sharvari-says-her-role-is-a-big-surprise-factor-in-the-horror-comedy-film/articleshow/110422953.cms'
# url = 'https://www.nytimes.com/athletic/5513075/2024/05/24/mlb-umpire-angel-hernandez-reputation/?source=nyt_sports'
# url = 'https://younglbrownh.medium.com/how-to-scrape-images-from-a-website-with-python-dbb3cb4d50e4'
folder_name = "static"
download_images_and_extract_text(url, folder_name)


# Example usage
# article_url = 'https://www.nytimes.com/athletic/5513075/2024/05/24/mlb-umpire-angel-hernandez-reputation/?source=nyt_sports'
# url = 'https://timesofindia.indiatimes.com/entertainment/hindi/bollywood/news/munjya-actress-sharvari-says-her-role-is-a-big-surprise-factor-in-the-horror-comedy-film/articleshow/110422953.cms'