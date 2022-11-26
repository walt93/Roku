import datetime
from datetime import date
from datetime import timedelta
from dateutil.parser import parser

import json
import urllib.request
from urllib.request import urlopen, Request
from enum import Enum

maxCategories = 100		# 15 on Roku Direct Publisher
maxCount = 150			# 40 on Roku Direct Publisher
maxVideos = 10000		# 1000 on Roku Direct Publisher

makeRecent = False
recentVideoDate = ""
reserveIndex = -1

#
# Usage:
#
# 1. Client gets an output by calling createOutput with the name of the Roku Channel
# 2. Client calls curlJsonDict up to 14 times, to add a category from a single-category JSON
# 3. Client calls writeOutput to emit the merged Roku JSON file
#
# def buildClassicConspiracy():
# 	output = createOutput("Conspyre: Classic Conspiracy")

# 	curlJsonDict(output, "General",					"most_popular",  "https://conspyre.tv/roku.json?catName=conspyre-classic-conspiracy")
# 	curlJsonDict(output, "Cooper, William",			"most_popular",  "https://conspyre.tv/roku.json?catName=videos")
# 	curlJsonDict(output, "Griffin, G. Edward",		"most_popular",  "https://conspyre.tv/roku.json?catName=g-edward-griffin")
# 	curlJsonDict(output, "Gunderson, Ted",			"most_popular",  "https://conspyre.tv/roku.json?catName=ted-gunderson")
# 	curlJsonDict(output, "Hoagland, Richard",		"most_popular",  "https://conspyre.tv/roku.json?catName=richard-hoagland")
# 	curlJsonDict(output, "Marrs, Jim",				"most_popular",  "https://conspyre.tv/roku.json?catName=jim-marrs")
# 	curlJsonDict(output, "Mystery Babylon Radio",	"chronological", "https://conspyre.tv/roku.json?catName=mystery-babylon-radio-archive")
# 	curlJsonDict(output, "Maxwell, Jordan",			"most_popular",  "https://conspyre.tv/roku.json?catName=jordan-maxwell")
# 	curlJsonDict(output, "Project Camelot",			"most_popular",  "https://conspyre.tv/roku.json?catName=project-camelot")
# 	curlJsonDict(output, "Springmeier, Fritz",		"most_popular",  "https://conspyre.tv/roku.json?catName=fritz-springmeier")
# 	curlJsonDict(output, "Tsarion, Michael",		"most_popular",  "https://conspyre.tv/roku.json?catName=michael-tsarion")

# 	writeOutput(output, "conspyre-classic-conspiracy.json")

# 1. Client gets an output by calling createOutput with the name of the Roku Channel
def createOutput(providerName, baseUrl):
	print("Building channel " + providerName)
	print("Creating output.")
	output = {}
	output["providerName"] = providerName
	output["language"] = "en"
	output["lastUpdated"] = datetime.datetime.now().isoformat()
	output["movies"] = []
	output["playlists"] = []
	output["categories"] = []
	output["liveFeeds"] = []
	output["shortFormVideos"] = []
	output["series"] = []
	output["tvSpecials"] = []
	output["ids"] = []
	output["recentVideos"] = {}
	output["baseUrlProgram"] = "https://" + baseUrl + "/roku.json?program_id="
	output["baseUrlCategory"] = "https://" + baseUrl + "/roku.json?catName="
	return output

# 1.5 client calls reserveTopChronological to reserve a slot for most recent videos}
def reserveTopChronological(output, name):
	makeRecent = True

	playlist = {}
	playlistName = name.lower().replace(" ", "")
	playlist["name"] = playlistName
	playlist["itemIds"] = []

	print(f"playlist = {playlist}")
	category = {}
	category["name"] = name
	category["playlistName"] = playlistName
	category["order"] = "manual"
	print(f"category = {category}")

	print(f"reserveIndex = {reserveIndex}")
	reserveIndex = len(output["playlists"])
	print(f"reserveIndex = {reserveIndex}")
	output["playlists"].append(playlist)	#append playlist
	output["categories"].append(category)	#append category

	recentVideoDate = date.today() - timedelta(days = 14)
	return

def fillTopChronological(output, maxCount):
	return

# 2. Client calls curlJsonDict to add a category from a single-category JSON
# name = How your category appears in Roku Direct Publisher
# order = "chronological | most_popular | most_recent"
# url = comes from AVideo site / category
def loadProgramId(output, name, id):
	url = output["baseUrlProgram"] + str(id)
	print(f"loading {url}")
	curlJsonDict(output, name, "manual", url, False)

def appendProgramId(output, name, id):
	url = output["baseUrlProgram"] + str(id)
	curlJsonDict(output, name, "manual", url, True)

def loadCategory(output, name, category):
	url = output["baseUrlCategory"] + category
	curlJsonDict(output, name, "manual", url, False)

def curlJsonDict(output, name, order, url, append):
	#Set a user agent, else 403
	r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

	response = urlopen(r).read()
	values = json.loads(response)

	# lace up the playlist name (AVideo returns 'all' for playlists)
	values["categories"][0]["name"] = name
	values["categories"][0]["order"] = order
	
	playlistName = name.lower().replace(" ", "")
	values["categories"][0]["playlistName"] = playlistName
	values["playlists"][0]["name"] = playlistName
	mergeOutput(values, output, "movies", append)	#hardcode schema for now
	count = len(values["movies"])
	if count == 0:
		print("***********************************************************************************")
		print(f"*** WARNING {name} contains {count} movies. {url}")
		print("***********************************************************************************")
	elif count > maxCount:
		print("***********************************************************************************")
		print(f"*** WARNING {name} contains {count} movies. {maxCount} max. {url}")
		print("***********************************************************************************")
	else:
		print(f"Creating playlist \"{name}\" ({url}). Contains {str(count)} movies.")
	return values

# 3. Client calls writeOutput to emit the merged Roku JSON file
def writeOutput(output, filename):
	output["ids"] = None				# don't publish our temporary variables
	output["baseUrlProgram"] = None
	output["baseUrlCategory"] = None

	shortFormCount = len(output["shortFormVideos"])
	seriesCount = len(output["series"])
	tvSpecialsCount = len(output["tvSpecials"])
	liveFeedsCount = len(output["liveFeeds"])
	moviesCount = len(output["movies"])
	categoriesCount = len(output["categories"])

	if shortFormCount == 0:
		output.pop("shortFormVideos", None)
	else:
		print(f"shortFormVideos have {moviesCount}")
	if seriesCount == 0:
		output.pop("series", None)
	else:
		print(f"series have {seriesCount}")
	if tvSpecialsCount == 0:
		output.pop("tvSpecials", None)
	else:
		print(f"tvSpecials have {tvSpecialsCount}")
	if liveFeedsCount == 0:
		output.pop("liveFeeds", None)
	else:
		print(f"liveFeeds have {liveFeedsCount}")

	if moviesCount > maxVideos:
		print("*****************************************************************")
		print(f"*** WARNING: {filename} has {moviesCount} movies, which is >{maxVideos} 🤦‍♂️")
		print("*****************************************************************")
	else:
		print(f"Channel has {moviesCount} movies.")
	if categoriesCount > maxCategories:
		print("*****************************************************************")
		print(f"*** WARNING: this channel has {categoriesCount} categories, which is >{maxCategories} 🤦‍♂️")
		print(f"*** {filename}")
		print("*****************************************************************")
	else:
		print(f"Channel has {categoriesCount} categories.")
	print("Serializing.")
	json_object = json.dumps(output, indent=4)

	print(f"Writing output to: {filename}")
	with open(filename, "w") as outfile:
		outfile.write(json_object)

	print("Fin.")

########################################################################################################################
# Private methods

def mergeOutput(dict, output, schema, append):
	d1 = date.today() - timedelta(days = 14)
	for m in dict["movies"]:						#iterate incoming movies
		m["thumbnail"] = m["thumbnail"].replace("_roku", "")	# roku jpeg doesn't work some % of the time, but, we always seem to have a thumbnail - let's just use it
		if not m["id"] in output["ids"]:			#skip if we've already processed this ID
			if len(m["shortDescription"]) == 0:		#fix empty description
				m["shortDescription"] = output["providerName"] + ": " + dict["categories"][0]["name"]
				m["longDescription"] = m["shortDescription"]	
			output["ids"].append(m["id"])			#save id
			output[schema].append(m)				#append to movies list
			d2 = parser().parse(m["releaseDate"])
			print(f"reserveIndex = {reserveIndex}")
			if d1 < d2.date():
				output["playlists"][reserveIndex].append(m["id"])

	if append == True:
		#append just the ids to the playlist

		output["playlists"][-1]['itemIds'] += dict["playlists"][0]['itemIds']
	else:
		output["playlists"] += dict["playlists"]		#append playlist
		output["categories"] += dict["categories"]		#append category

