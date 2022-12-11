from RokuFunctions import *

def buildColonyDev():
	output = createOutput("Burrow•Colony DEV", "conspyre.tv")

	#prepareAllCategory()

	#Featured content
	loadProgramId(output, "Burrow: Featured", 58493, False)
	loadProgramId(output, "Burrow: Just Added", 58474, False)
	reserveTopChronological(output, "Latest Podcasts")

	#Alphabetical podcasters
	loadCategory(output, "Amazing Polly", "amazing-polly", True)
	loadCategory(output, "Brad & Abbey Show", "brad-abbey-show", True)
	loadProgramId(output, "BradCGZ", 62937, True)
	loadCategory(output, "Corbett Report", "corbett-report", True)
	loadCategory(output, "Dark Journalist", "dark-journalist", True)
	loadCategory(output, "Dustin Nemos", "dustin-nemos", True)
	loadProgramId(output, "IPOT1776", 60413, True)
	loadCategory(output, "Jordan Sather", "jordan-sather", True)
	loadProgramId(output, "JustInformed Talk", 113460, True)
	loadCategory(output, "L", "l", True)
	loadCategory(output, "Lisa Mei Crowley", "lisa-mei-crowley", False)								
	loadProgramId(output, "M3thods", 59991, True)
	loadProgramId(output, "Music", 61758, False)
	loadProgramId(output, "Mouthy Buddha", 60411, True)
	loadCategory(output, "Patel Patriot", "patel-patriot", True)
	loadCategory(output, "Praying Medic", "praying-medic", True)
	loadCategory(output, "Quite Frankly", "quite-framkly", True)
	loadCategory(output, "Really Graceful", "really-graceful", True)
	loadCategory(output, "Redpill78", "redpill78", True)
	loadCategory(output, "Robert Sepehr", "robert-sepehr", True)
	loadCategory(output, "Sarah Westall", "sarah-westall", True)
	loadCategory(output, "SGT Report", "sgt-report", True)
	loadCategory(output, "Tore Says", "tore-says", True)
	loadProgramId(output, "Severe Anon", 103090, False)
	loadCategory(output, "TRUreporting", "trureporting", True)

	#fillTopChronological(output, 100)	# up to 100 videos max

	writeOutput(output, "/var/www/html/AVideo/rokuv2/devcolony.json")

# Do it. Build the channel.
buildColonyDev()
