import os
import sys
import requests
from bs4 import BeautifulSoup
from podcasts import podcasts

from base import (
    download_video,
    upload_video,
    check_if_encoded,
    scrape_rumble_video_page,
)

def scrape_rumble_most_recent_video_info(url):
    print("*** scrape_rumble_most_recent_video_info {url}")

    # Download page HTML with requests
    response = requests.get(url)
    page_content = response.content

    # Load HTML from response content with Beautiful Soup
    soup = BeautifulSoup(page_content, "html.parser")

    # Find the first video on the page
    video_entry = soup.find("li", class_="video-listing-entry")
    video_link = video_entry.find("a", class_="video-item--a")["href"]
    video_url = "https://rumble.com" + video_link

    return scrape_rumble_video_page(video_url)


def process_element(vid):
    print(f"*** scraping {vid.username}")
    j = scrape_rumble_most_recent_video_info(vid.url)
    encoded = check_if_encoded(j["title"], j["uploadDate"])
    print(f"*** encoded = {encoded}")
    if encoded is False:
        print(f'*** Downloading from {j["url"]} to /tmp')
        video_path = download_video(j["url"], "/tmp")
        print(
            f"*** Uploading from {video_path} as {vid.username} to category {vid.category}"
        )
        upload_video(
            video_path,
            j["title"],
            "",
            j["description"],
            vid.category,
            vid.username,
            vid.password,
            j["uploadDate"],
        )
        print(f"*** Removing temp file {video_path}")
        os.remove(video_path)


# Get the command line arguments
if len(sys.argv) != 2:
    print("Usage: python3 scrape_rumble.py index (-1 for all)")
    for index, elem in enumerate(podcasts):
        print(f"    {index} {elem.username}")
    sys.exit(1)

index = int(sys.argv[1])

if index == -1:
    # Iterate over the array of named tuples
    for elem in podcasts:
        process_element(elem)
elif index < len(podcasts):
    elem = podcasts[index]
    process_element(elem)
else:
    print(f"{index} is out of bounds (-1 || 0..{len(podcasts)})")
