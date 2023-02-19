import requests
from bs4 import BeautifulSoup
from collections import namedtuple
from base import process_and_add_if_not_exists

Podcast = namedtuple('Podcast', ['url', 'username', 'password', 'category'])
p = Podcast('https://rumble.com/user/AmazingPolly/',   'Polly',          '38e0f5f3ef49c677f3d47ca5e03c05b3', 13)                  # Amazing Polly     53.9K

def scrape_rumble_most_recent_videos_first_page(url, category, username, password):
    print(f'scrape_rumble_most_recent_videos_first_page : {url}')

    # Download page HTML with requests
    response = requests.get(url)
    page_content = response.content

    # Load HTML from response content with Beautiful Soup
    soup = BeautifulSoup(page_content, "html.parser")

    # Find all the video entries on the page
    video_entries = soup.find_all("li", class_="video-listing-entry")

    # Loop through the video entries and extract the links
    for video_entry in reversed(video_entries):
        print(f'*** processing {video_entry}')
        video_link = video_entry.find("a", class_="video-item--a")["href"]
        video_url = "https://rumble.com" + video_link
        process_and_add_if_not_exists(video_url, category, username, password)
        break

# Iterate over the array of named tuples
video_json = scrape_rumble_most_recent_videos_first_page(p.url, p.category, p.username, p.password)
