import os
import requests

# import mysql
import subprocess
import mysql.connector
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime, timedelta
from collections import namedtuple

Podcast = namedtuple("Podcast", ["url", "username", "password", "category"])
array = [
    Podcast(
        "https://rumble.com/trureporting/",
        "TRUreporting",
        "ed5d449d4d7054e74f5794f826cb82c4",
        1,
    ),  # TRUReporting      31.7K
    Podcast(
        "https://rumble.com/justinformedtalk/",
        "JustInformed",
        "ef4f790f03eda3fa6f052be53bea2ccf",
        2,
    ),  # JustInformed Talk 24.7K
    Podcast(
        "https://rumble.com/bigdigenergy/",
        "SomeBitchIKnow",
        "f886b00263d6e14b04805e3f5d5e14bb",
        7,
    ),  # Big Dig Energy    5.39K (Rumble) 210K Gab
    Podcast(
        "https://rumble.com/sarahwestall/",
        "Sarah",
        "566b535e67eb02fefbae72634475f318",
        17,
    ),  # Sarah Westall     19K
    Podcast(
        "https://rumble.com/sgtreport/",
        "SGTReport",
        "d905e97368d3b9b4adab71f50c790724",
        14,
    ),  # SGTReport         91.3K
    Podcast(
        "https://rumble.com/user/AmazingPolly/",
        "Polly",
        "38e0f5f3ef49c677f3d47ca5e03c05b3",
        13,
    ),  # Amazing Polly     53.9K
    Podcast(
        "https://rumble.com/c/c-321935", "Dustin", "49634d8a1b8cbf5015b7f5712715c1ee", 8
    ),  # Dustin Nemos      13.8K
    Podcast(
        "https://rumble.com/search/video?q=altered%20state&date=this-week",
        "BradCGZ",
        "5343736cbfa3adbfb9d7962a3c439d34",
        5,
    ),  # Altered State
    Podcast(
        "https://rumble.com/c/JordanSather",
        "Jordan",
        "f7f67c40dc7a794785e0bbc82a2564ff",
        10,
    ),  # Jordan Sather     41.5K
    Podcast(
        "https://rumble.com/c/c-1673813",
        "AmericasMom",
        "6db20d1cccd0afb83e61a43310d18e63",
        17,
    ),  # America's Mom     418
]


#
# Download the video file into the specified directory using yt-dlp;
# if it is not a mp4 file already, transcode/package as a mp4.
#
def download_video(url, directory):
    try:
        output_template = os.path.join(directory, "%(title)s.%(ext)s")
        subprocess.run(
            [
                "yt-dlp",
                "-S",
                "res,ext:mp4:m4a",
                "--recode",
                "mp4",
                "-o",
                output_template,
                url,
            ],
            check=True,
        )
        video_info = (
            subprocess.check_output(
                ["yt-dlp", "--get-filename", "-o", output_template, url]
            )
            .decode()
            .strip()
        )
        video_path = os.path.join(directory, video_info)
        return video_path
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return NULL


#
# Upload a video file to the AVideo encoder for news.conspyre.tv
#
def upload_video(
    file_path,
    title,
    video_password,
    description,
    categories_id,
    username,
    password,
    created,
):
    url = f"https://news.conspyre.tv/plugin/MobileManager/upload.php?user={username}&pass={password}"
    file_key = "upl"

    with open(file_path, "rb") as f:
        files = {file_key: f}
        data = {
            "title": title,
            "video_password": video_password,
            "description": description,
            "categories_id": categories_id,
        }
        print(f"*** POST {url} files={files} data={data}")
        response = requests.post(url, files=files, data=data)
    print(f"response = {response}")
    return response


#
# Check if a video has already been encoded and uploaded to the platform.
#    Args:
#        video_name (str): The name of the video.
#        upload_date (str): The upload date of the video.
#
#    Returns:
#        bool: True if the video has already been encoded and uploaded, False otherwise.
#
def check_if_encoded(video_name, upload_date):
    # Open the database connection
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="dRSxpS3rDI_bsCrTyTngH43_two4nine3BX",
        database="news",
    )
    cursor = cnx.cursor()

    # fix the video name the way the AVideo platform does it, otherwise matching fails
    video_name = video_name.replace('"', "''")

    # Query the videos table for a matching video - we store the Rumble duration string directly into epg_link (note: we should actually set the created datetime to the correct value here and compare them as datetimes...)
    # cursor.execute("SELECT created FROM videos WHERE title=%s AND epg_link=%s", (video_name, upload_date))
    cursor.execute("SELECT created FROM videos WHERE title=%s", (video_name,))
    result = cursor.fetchone()

    # Close the database connection
    cnx.close()

    # If a matching record is found, the video has already been encoded and uploaded
    if result is not None:
        return True
    else:
        return False


def scrape_rumble_video_page(video_url):
    print(f"*** scrape_rumble_video_page {video_url}")

    # Load video page HTML with requests
    video_response = requests.get(video_url)
    video_content = video_response.content
    video_soup = BeautifulSoup(video_content, "html.parser")

    # Find the JSON-LD script tag
    json_script = video_soup.find("script", type="application/ld+json").string

    # Parse JSON-LD data
    video_data = json.loads(json_script)[0]  # Get first video asset in the array
    video_desc = video_data["description"]
    video_thumb = video_data["thumbnailUrl"]
    upload_date = datetime.fromisoformat(video_data["uploadDate"]).strftime("%d%m%y%H%M%S")
    video_duration = video_data["duration"]
    video_name = video_data["name"] + "." + upload_date

    print(f"upload_date = {upload_date} video_name = {video_name} video_duration={video_duration}")
    # Convert duration from PT format to HH:MM:SS
    dur = re.findall(r"\d+", video_duration)
    duration = timedelta(hours=int(dur[0]), minutes=int(dur[1]), seconds=int(dur[2]))
    video_duration = str(duration)

    print(f"*** upload_date = {upload_date} video_name = {video_name} video_duration={video_duration}")

    # Create JSON object with video data
    video_json = {
        "title": video_name,
        "description": video_desc,
        "thumbnailUrl": video_thumb,
        "uploadDate": upload_date,
        "duration": video_duration,
        "url": video_url,
    }
    print(json.dumps(video_json, indent=4))
    # Return JSON object
    return video_json  # json.dumps(video_json)


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
