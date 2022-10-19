from RokuFunctions import *

def buildBurrow():
	output = createOutput("Burrow•DEV", "conspyre.tv")

	#prepareAllCategory()

	#Featured content
	loadProgramId(output, "Featured", 58493)
	loadProgramId(output, "Just Added", 58474)
	reserveTopChronological(output, "Just Added")

	#Alphabetical podcasters
	loadCategory(output, "Amazing Polly", "amazing-polly")		# √
	loadProgramId(output, "BradCGZ", 62937)						# √
	loadCategory(output, "Corbett Report", "corbett-report")	# √
	loadCategory(output, "Dark Journalist", "dark-journalist")
	loadCategory(output, "Destroying the Illusion", "destroying-the-illusion")
	loadCategory(output, "Dustin Nemos", "dustin-nemos")
	loadCategory(output, "IPOT1776", "ipot1776")				# √
	loadCategory(output, "L", "l")	
	loadProgramId(output, "M3thods", 59991)						# √
	loadProgramId(output, "Mouthy Buddha", 60411)				# √
	loadCategory(output, "Patel Patriot", "patel-patriot")		# √
	loadCategory(output, "Praying Medic", "praying-medic")
	loadCategory(output, "Quite Frankly", "quite-frankly")		# √
	loadCategory(output, "RedPill78", "redpill78")				# √
	loadCategory(output, "Really Graceful", "really-graceful")	# √
	loadCategory(output, "Sarah Westall", "sarah-westall")
	loadCategory(output, "SGT Report", "sgt-report")
	loadCategory(output, "TRUreporting", "trureporting")
	loadCategory(output, "Woke Societies", "woke-societies")

	fillTopChronological(output, 100)	# up to 100 videos max

	writeOutput(output, "/var/www/html/AVideo/rokuv2/devcolony.json")

# Do it. Build the channel.
buildBurrow()

