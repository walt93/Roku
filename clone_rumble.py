import os
import sys
import requests
from bs4 import BeautifulSoup
from podcasts import podcasts

from base import (
    download_video,
    upload_video,
    check_if_encoded,
    scrape_rumble_video_page
)

# user_url is a url to the user's home page on Rumble
# e.g. https://rumble.com/TRUreporting or https://rumble.com/c/c1673813 or https://rumble.com/user/MrTruthBomb2
def scrape_all_rumble_videos(user_url):
    # Extract the last page number from the paginator array
    page_num = int(
        BeautifulSoup(requests.get(user_url).content, "html.parser")
        .find("nav", class_="paginator")
        .find_all("a")[-1]["href"]
        .split("=")[-1]
    )

    # Iterate through all the pages in reverse order
    for page in range(page_num, 0, -1):
        page_url = f"{user_url}?page={page}"
        page_content = requests.get(page_url).content
        soup = BeautifulSoup(page_content, "html.parser")
        print(f"***page_url = {page_url}")
        video_entries = soup.find("ol").find_all(
            "li", class_="video-listing-entry"
        )
        print(f"video_entries = {video_entries}")

        # Iterate through all the video entries on the page in reverse order
        for entry in reversed(video_entries):
            video_url = (
                f"https://rumble.com{entry.find('a', class_='video-item--a')['href']}"
            )
            print(f"scraping {video_url}")
            result = scrape_rumble_video_page(video_url)


def process_element(v):
    print(f"*** scraping {v.username}")
    j = scrape_rumble_most_recent_video_info(v.url)
    encoded = check_if_encoded(j["title"], j["uploadDate"])
    print(f"*** encoded = {encoded}")
    if encoded is False:
        print(f'*** Downloading from {j["url"]} to /tmp')
        video_path = download_video(j["url"], "/tmp")
        print(
            f"*** Uploading from {video_path} as {v.username} to category {v.category}"
        )
        upload_video(
            video_path,
            j["title"],
            "",
            j["description"],
            v.category,
            v.username,
            v.password,
            j["uploadDate"],
        )
        print(f"*** Removing temp file {video_path}")
        os.remove(video_path)


# Get the command line arguments
if len(sys.argv) != 2:
    print("Usage: python3 clone_rumble.py index (-1 for all)")
    for index, elem in enumerate(podcasts):
        print(f"    {index} {elem.username}")
    sys.exit(1)

index = int(sys.argv[1])

if index == -1:
    # Iterate over the array of named tuples
    for elem in podcasts:
        scrape_all_rumble_videos(elem.url)
elif index < len(podcasts):
    elem = podcasts[index]
    scrape_all_rumble_videos(elem.url)
else:
    print(f"{index} is out of bounds (-1 || 0..{len(podcasts)})")
