import os
import sys
from collections import namedtuple
import requests
from bs4 import BeautifulSoup

from base import download_video, upload_video, check_if_encoded, scrape_rumble_video_page

Podcast = namedtuple('Podcast', ['url', 'username', 'password', 'category'])
array = [
    Podcast('https://rumble.com/trureporting/',        'TRUreporting',   'ed5d449d4d7054e74f5794f826cb82c4', 1),                   # TRUReporting      31.7K
    Podcast('https://rumble.com/justinformedtalk/',    'JustInformed',   'ef4f790f03eda3fa6f052be53bea2ccf', 2),                   # JustInformed Talk 24.7K
    Podcast('https://rumble.com/bigdigenergy/',        'SomeBitchIKnow', 'f886b00263d6e14b04805e3f5d5e14bb', 7),                   # Big Dig Energy    5.39K (Rumble) 210K Gab
    Podcast('https://rumble.com/sarahwestall/',        'Sarah',          '566b535e67eb02fefbae72634475f318', 17),                  # Sarah Westall     19K
    Podcast('https://rumble.com/sgtreport/',           'SGTReport',      'd905e97368d3b9b4adab71f50c790724', 14),                  # SGTReport         91.3K
    Podcast('https://rumble.com/user/AmazingPolly/',   'Polly',          '38e0f5f3ef49c677f3d47ca5e03c05b3', 13),                  # Amazing Polly     53.9K
    Podcast('https://rumble.com/c/c-321935',           'Dustin',         '49634d8a1b8cbf5015b7f5712715c1ee', 8),                   # Dustin Nemos      13.8K
    Podcast('https://rumble.com/search/video?q=altered%20state&date=this-week', 'BradCGZ', '5343736cbfa3adbfb9d7962a3c439d34', 5), # Altered State
    Podcast('https://rumble.com/c/JordanSather',       'Jordan',         'f7f67c40dc7a794785e0bbc82a2564ff', 10),                  # Jordan Sather     41.5K
    Podcast('https://rumble.com/c/c-1673813',          'Sherronna',      '6db20d1cccd0afb83e61a43310d18e63', 17)                   # America's Mom     418
]

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

def process_element(v):
    print(f'*** scraping {v.username}')
    j = scrape_rumble_most_recent_video_info(v.url)
    encoded = check_if_encoded(j["title"], j["uploadDate"])
    print(f'*** encoded = {encoded}')
    if encoded is False:
        print(f'*** Downloading from {j["url"]} to /tmp')
        video_path = download_video(j["url"], "/tmp")
        print(f'*** Uploading from {video_path} as {v.username} to category {v.category}')
        upload_video(video_path, j["title"], "", j["description"], v.category, v.username, v.password, j["uploadDate"])
        print(f'*** Removing temp file {video_path}')
        os.remove(video_path)

# Get the command line arguments
if len(sys.argv) != 2:
    print("Usage: python my_program.py index")
    sys.exit(1)

index = int(sys.argv[1])

if index == -1:
    # Iterate over the array of named tuples
    for elem in array:
        process_element(elem)
elif index < len(array):
    elem = array[index]
    process_element(elem)
else:
    print(f'{index} is out of bounds (-1 || 0..{len(array)})')
