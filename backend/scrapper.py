import csv
from selenium import webdriver
import time
import os
import requests
import base64

def download_images(query, folder_path):
    os.makedirs(f'{folder_path}/images', exist_ok=True)
    # Start a new Chrome session
    driver = webdriver.Chrome()

    # Open Google
    driver.get("https://www.google.com")

    # Find the search bar and type the query
    search_box = driver.find_element("css selector", 'textarea[jsname="yZiJbe"]')
    search_box.send_keys(query)
    search_box.submit()

    # Click on the Images tab
    images_tab = driver.find_element("link text", "Images")
    images_tab.click()
    time.sleep(3)

    # Get current and new heights
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new images to load
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Get links of all the images
    image_links = driver.find_elements("css selector", 'div[jsname="DeysSe"] img')

    urls = []

    for index, link in enumerate(image_links, start=1):
        try:
            img_url = link.get_attribute('src')
            alt_text = link.get_attribute('alt')

            if img_url and img_url.startswith(('http', 'data:')):  # Check if the URL is valid
                file_name = os.path.join(f"{folder_path}/images", f"image_{index}.jpg")

                if img_url.startswith('http'):  # Download regular HTTP/HTTPS images
                    response = requests.get(img_url)
                    with open(file_name, 'wb') as file:
                        file.write(response.content)
                        print(f"Downloaded: {file_name}")
                elif img_url.startswith('data:'):  # Decode and save base64 images
                    img_data = img_url.split(',')[1]
                    img_data = base64.b64decode(img_data)
                    with open(file_name, 'wb') as file:
                        file.write(img_data)
                        print(f"Downloaded: {file_name}")

                urls.append({'Image_URL': f'./images/image_{index}.jpg', 'Alt_Text': alt_text})
        except Exception as e:
            print(f"Exception occurred: {str(e)}")
    
    # Save the image URLs and alt text to a CSV file
    with open(f'{folder_path}/image_urls.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Image_URL', 'Alt_Text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for url_info in urls:
            writer.writerow(url_info)

    # Close the browser window
    driver.quit()

# URL of the Google search page
google_query = "images of grapes with Alternaria rot"
# Folder path where images will be saved
download_folder = 'grapes'

# Create a folder if it doesn't exist
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Call the function to scrape images
download_images(google_query, download_folder)
