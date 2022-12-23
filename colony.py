from RokuFunctions import *

def buildColonyDev():
	output = createOutput("Burrow•Colony", "conspyre.tv")

	#prepareAllCategory()

	#Featured content
	loadProgramId(output, "Colony has moved", 120859, False)
	#loadProgramId(output, "Burrow: Featured", 58493, False)
	#loadProgramId(output, "Burrow: Just Added", 58474, False)
	#reserveTopChronological(output, "Latest Podcasts")

	#Alphabetical podcasters
	#loadCategory(output,  "Brad & Abbey Show", "brad-abbey-show", True)
	#loadProgramId(output, "BradCGZ", 62937, True)
	#loadProgramId(output, "IPOT1776", 60413, True)
	#loadProgramId(output, "JustInformed Talk", 113460, True)
	#loadCategory(output,  "L", "l", True)
	#loadCategory(output,  "Lisa Mei Crowley", "lisa-mei-crowley", True)								
	#loadProgramId(output, "M3thods", 59991, True)
	#loadProgramId(output, "Music", 61758, False)
	#loadProgramId(output, "Severe Anon", 103090, False)
	#loadCategory(output,  "TRUreporting", "trureporting", True)

	writeOutput(output, "/var/www/html/AVideo/rokuv2/colony.json")

# Do it. Build the channel.
buildColonyDev()

