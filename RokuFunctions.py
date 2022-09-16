import datetime
import json
import urllib.request
from urllib.request import urlopen, Request
from enum import Enum

maxCategories = 100		# 15 on Roku Direct Publisher
maxCount = 150			# 40 on Roku Direct Publisher
maxVideos = 10000		# 1000 on Roku Direct Publisher

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
def createOutput(providerName):
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
	return output

# 1a. [Optional] call prepareAllCategory to prepare a category for "ALL" (only use for small channels <150 programs)
def prepareAllCategory():
	print("Creating playlist \"All\"")
	# create a playlist "All" with everything, sorted by most_recent
	tcat = {}
	tcat["name"] = "All"
	tcat["playlistName"] = "all"
	tcat["order"] = "most_recent"
	output["categories"].append(tcat)

	tpl = {}
	tpl["name"] = "all"
	tpl["itemIds"] = []
	output["playlists"].append(tpl)


# 2. Client calls curlJsonDict to add a category from a single-category JSON
# name = How your category appears in Roku Direct Publisher
# order = "chronological | most_popular | most_recent"
# url = comes from AVideo site / category
def curlJsonDict(output, name, order, url):
	#Set a user agent, else 403
	r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

	response = urlopen(r).read()
	values = json.loads(response)

	#print(f"response = {values}")

	values["categories"][0]["name"] = name
	values["categories"][0]["order"] = order
	mergeOutput(values, output, "movies")	#hardcode schema for now
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

	print("Writing output.")
	with open(filename, "w") as outfile:
		outfile.write(json_object)

	print("Fin.")

########################################################################################################################
# Private methods

def mergeOutput(dict, output, schema):
	output[schema] += dict["movies"]
	output["playlists"] += dict["playlists"]
	output["categories"] += dict["categories"]

	#Append every movie to the "all" playlist if it exists
	if output["playlists"][0]["name"] == "all":
		outputArray = output["playlists"][0]["itemIds"]
		itemIds = dict["playlists"][0]["itemIds"]
		outputArray += itemIds