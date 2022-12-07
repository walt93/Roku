from RokuFunctions import *

def buildColonyDev():
	output = createOutput("Burrow•Colony", "conspyre.tv")

	#prepareAllCategory()

	#Featured content
	loadProgramId(output, "Burrow: Featured", 58493)
	loadProgramId(output, "Burrow: Just Added", 58474)
	reserveTopChronological(output, "Latest Podcasts")

	#Alphabetical podcasters
#	loadCategory(output, "Amazing Polly", "amazing-polly", True)		# √ 32
	loadCategory(output, "Brad & Abbey Show", "brad-abbey-show", True)
	loadProgramId(output, "BradCGZ", 62937, True)
#	loadCategory(output, "Corbett Report", "corbett-report", True)	# √ 18
#	loadCategory(output, "Dark Journalist", "dark-journalist", True)	# √ 23
#	loadCategory(output, "Dustin Nemos", "dustin-nemos", True)		# √ 23
	loadProgramId(output, "IPOT1776", 60413, True)
#	loadCategory(output, "Jordan Sather", "jordan-sather", True)		# 18
#	loadCategory(output, "L", "l", True)								# 16
	loadCategory(output, "Lisa Mei Crowley", "lisa-mei-crowley", True)								
	loadProgramId(output, "M3thods", 59991, True)						# √
	loadProgramId(output, "Music", 61758, False)
#	loadProgramId(output, "Mouthy Buddha", 60411, True)				# √
#	loadCategory(output, "Patel Patriot", "patel-patriot", True)		# 16
#	loadCategory(output, "Praying Medic", "praying-medic", True)		#
#	loadCategory(output, "Quite Frankly", "quite-framkly", True)		# 17
#	loadCategory(output, "Really Graceful", "really-graceful", True)	# 26
#	loadCategory(output, "Redpill78", "redpill78", True)				# 17
#	loadCategory(output, "Robert Sepehr", "robert-sepehr", True)		# √
#	loadCategory(output, "Sarah Westall", "sarah-westall", True)		#
#	loadCategory(output, "SGT Report", "sgt-report", True)			# 20
#	loadCategory(output, "Tore Says", "tore-says", True)				# 

	loadProgramId(output, "Severe Anon", 103090, False)				# √
	loadCategory(output, "TRUreporting", "trureporting", True)		# √ 18

	#fillTopChronological(output, 100)	# up to 100 videos max

	writeOutput(output, "/var/www/html/AVideo/rokuv2/colony.json")

# Do it. Build the channel.
buildColonyDev()

