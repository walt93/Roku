import os
import subprocess
import sys

# from sh import rclone
import requests
from RokuFunctions import (
    createOutput,
    reserveTopChronological,
    loadProgramId,
    loadCategory,
    loadCategoryB,
    writeOutput,
)


def build_conspyre_tv():
    op = createOutput("Conspyre·TV", "conspyre.tv", "news.conspyre.tv")

    # prepareAllCategory()

    loadProgramId(op, "Featured", 58493, False)  # Featured content
    loadProgramId(op, "Just Added", 58474, False)

    # Alphabetical podcasters
    reserveTopChronological(op, "Recent Transmissions")
    loadCategoryB(op, "Altered State", "altered-state", True)
    loadCategoryB(op, "Amazing Polly", "amazing-polly", True)
    loadCategoryB(op, "Big Dig Energy", "big-dig-energy", True)
    loadCategoryB(op, "Brad & Abbey Show", "brad-abbey-show", True)
    loadCategoryB(op, "Craig Mason's Reasonable TV", "craig-mason-s-reasonable-tv", True)
    loadProgramId(op, "Disclosure Hub Hits", 59975, False)
    loadCategory(op, "Enthéos Shines Fan Channel", "entheos-shines-fan-channel", False)
    loadCategoryB(op, "Jordan Sather", "jordan-sather", True)
    loadCategoryB(op, "JustInformed Talk", "justinformed-talk", True)
    loadCategoryB(op, "Logical Brad TV", "logical-brad-tv", True)
    loadCategory(op, "M3thods", "m3thods", True)
    loadCategoryB(op, "Nemos News Network", "nemos-news-network", True)
    loadCategoryB(op, "SGT Report", "sgtreport", True)
    loadCategoryB(op, "Tore Says", "tore-says", True)
    loadCategoryB(op, "TRUreporting", "trureporting", True)

    loadProgramId(op, "Music", 61758, False)  # Music
    loadCategory(op, "Lisa Mei Crowley", "lisa-mei-crowley", False)
    loadProgramId(op, "Severe Anon", 103090, False)

    # Alphabetical categories
    loadProgramId(op, "5G", 59660, False)  # SHARED
    loadProgramId(op, "9/11", 59662, False)  # SHARED
    loadProgramId(op, "Adair, David", 60321, False)
    loadProgramId(op, "Alt. Anthropology", 61754, False)  # SHARED
    loadProgramId(op, "Assange, Julian", 58473, False)  # SHARED
    loadProgramId(op, "Bernard, Ronald", 59685, False)
    loadProgramId(op, "CIA", 60325, False)  # SHARED
    loadProgramId(op, "Cooper, William", 59686, False)  # SHARED
    loadProgramId(op, "Cult of the Medics", 59688, False)  # SHARED
    loadProgramId(op, "Dark, The", 60328, False)  # SHARED
    loadCategory(op, "Detox Project, The", "detox-project", False)
    loadProgramId(op, "Disclosure Hub Hits", 59975, False)  # SHARED
    loadCategory(op, "Disclosure Library", "disclosure-library", False)
    loadProgramId(op, "Disney", 59689, False)
    loadProgramId(op, "Dysfunction, Election", 114334, False)
    loadCategory(op, "Egypt", "egypt", False)
    loadProgramId(op, "Epstein, Jeffrey", 59693, False)  # SHARED
    loadCategory(op, "Fall of the Cabal", "fall-of-the-cabal", False)  # SHARED
    loadProgramId(op, "Finders, The", 59694, False)  # SHARED
    loadProgramId(op, "Freemasons", 59695, False)  # SHARED
    loadProgramId(op, "Gates, Bill", 59696, False)
    loadProgramId(op, "General", 74211, False)  # SHARED
    loadProgramId(op, "Geoengineering", 59697, False)  # SHARED
    loadProgramId(op, "Giants", 59698, False)  # SHARED
    loadProgramId(op, "Great Reset", 59699, False)  # SHARED
    loadProgramId(op, "Gunderson, Ted", 59835, False)  # SHARED
    loadCategory(op, "Healing from GMOs", "healing-from-gmos", False)
    loadProgramId(op, "Health, General", 59700, False)  # SHARED
    loadCategory(op, "Illuminati", "illuminati", False)
    loadCategory(op, "IPOT1776", "ipot1776", True)
    loadProgramId(op, "ITNJ Judicial Commission", 60403, False)  # SHARED
    loadCategory(op, "Jacob, Frank", "frank-jacob", False)
    loadCategory(op, "JFK", "jfk", False)  # SHARED
    loadCategory(op, "Lazar, Bob", "bob-lazar", False)  # SHARED
    loadCategory(op, "Marrs, Jim", "jim-marrs", False)  # SHARED
    loadCategory(op, "Maxwell, Jordan", "jordan-maxwell", False)  # SHARED
    loadCategory(op, "Megaliths", "megalithic-sites", False)
    loadCategory(op, "Meyer, Stanley", "stanley-meyer", False)
    loadProgramId(op, "Mind Control", 60416, False)  # SHARED
    loadProgramId(op, "Mouthy Buddha", 60411, False)  # SHARED
    loadProgramId(op, "MrTruthBomb", 69786, False)  # SHARED
    loadCategory(op, "Mystery Babylon Radio", "mystery-babylon-radio-archive", False)
    loadProgramId(op, "NASA", 60419, False)  # SHARED
    loadProgramId(op, "ORME", 60420, False)  # SHARED
    loadCategory(op, "Pizzagate", "pizzagate", False)
    loadCategory(op, "Project Camelot", "project-camelot", False)
    loadProgramId(op, "Pizzagate", 60421, False)  # SHARED
    loadProgramId(op, "Remote Viewing", 60905, False)  # SHARED
    loadProgramId(op, "Schneider, Philip", 60906, False)  # SHARED
    loadProgramId(op, "Shackleford, Rusty (Pedo Island drone footage)", 61761, False)  # SHARED
    loadCategory(op, "Springmeier, Fritz", "fritz-springmeier", False)
    loadCategory(op, "SRA", "sra", False)
    loadProgramId(op, "Tartaria", 61755, False)  # SHARED
    loadCategory(op, "Tellinger, Michael", "michael-tellinger", False)
    loadCategory(op, "Tesla, Nikola", "nikola-tesla", False)
    loadCategory(op, "Truth About Cancer, the", "the-truth-about-cancer", False)
    loadProgramId(op, "TRUTHISKNOWLEDGE", 106372, False)
    loadProgramId(op, "Tyrrany & Eugenics (Jana Esp)", 61757, False)  # SHARED
    loadProgramId(op, "Thunderbolts Project", 61759, False)  # SHARED
    loadProgramId(op, "UFOs", 61763, False)  # SHARED

    # pepe is dead. but a vhost remains. long live pepe.
    print("*** writing output file conspyre-tv.json")
    writeOutput(op, "/tmp/conspyre/conspyre-tv.json")

    print("*** copying conspyre-tv.json to b-json bucket")
    try:
        os.chdir("/tmp/conspyre/")
        storage_uploader = "/home/ubuntu/Roku/storageuploader.py"
        access_key = "d45b9990-462a-4670-ae1c2a514db7-2f89-40f6"
        subprocess.call(
            [
                "python3",
                storage_uploader,
                "--storagezone",
                "b-json",
                "--accesskey",
                access_key,
                "./",
            ]
        )
    except subprocess.CalledProcessError as err:
        print(f"Error: {str(err)}")
        sys.exit(0)

    print("*** purging conspyre-tv.json from b-json pullzone")
    try:
        url = "https://api.bunny.net/purge?url=https%3A%2F%2Fb-json.b-cdn.net%2Fconspyre-tv.json&async=true"
        headers = {
            "AccessKey": "f7af3654-961e-427b-a337-d39dad813f1b",
            "Content-Type": "application/json",
        }
        response = requests.post(url, headers=headers)
        print("Status Code:", response.status_code)
        print("Headers:", response.headers)
        print("Response Body:", response.content)
    except requests.exceptions.RequestException as err:
        print(f"Error: {str(err)}")
        sys.exit(0)


# Do it. Build the channel.
build_conspyre_tv()
