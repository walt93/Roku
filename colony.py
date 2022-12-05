from RokuFunctions import *

def buildColonyDev():
	output = createOutput("Burrow•Colony", "conspyre.tv")

	#prepareAllCategory()

	#Featured content
	loadProgramId(output, "Burrow: Featured", 58493)
	loadProgramId(output, "Burrow: Just Added", 58474)
	reserveTopChronological(output, "Latest Podcasts")

	#Alphabetical podcasters
#	loadCategory(output, "Amazing Polly", "amazing-polly")		# √ 32
	loadCategory(output, "Brad & Abbey Show", "brad-abbey-show")
	loadProgramId(output, "BradCGZ", 62937)
#	loadCategory(output, "Corbett Report", "corbett-report")	# √ 18
#	loadCategory(output, "Dark Journalist", "dark-journalist")	# √ 23
#	loadCategory(output, "Dustin Nemos", "dustin-nemos")		# √ 23
	loadProgramId(output, "IPOT1776", 60413)
#	loadCategory(output, "Jordan Sather", "jordan-sather")		# 18
#	loadCategory(output, "L", "l")								# 16
	loadCategory(output, "Lisa Mei Crowley", "lisa-mei-crowley")								
	loadProgramId(output, "M3thods", 59991)						# √
	loadProgramId(output, "Music", 61758)
#	loadProgramId(output, "Mouthy Buddha", 60411)				# √
#	loadCategory(output, "Patel Patriot", "patel-patriot")		# 16
#	loadCategory(output, "Praying Medic", "praying-medic")		#
#	loadCategory(output, "Quite Frankly", "quite-framkly")		# 17
#	loadCategory(output, "Really Graceful", "really-graceful")	# 26
#	loadCategory(output, "Redpill78", "redpill78")				# 17
#	loadCategory(output, "Robert Sepehr", "robert-sepehr")		# √
#	loadCategory(output, "Sarah Westall", "sarah-westall")		#
#	loadCategory(output, "SGT Report", "sgt-report")			# 20
#	loadCategory(output, "Tore Says", "tore-says")				# 

	loadProgramId(output, "Severe Anon", 103090)				# √
	loadCategory(output, "TRUreporting", "trureporting")		# √ 18

	#fillTopChronological(output, 100)	# up to 100 videos max

	writeOutput(output, "/var/www/html/AVideo/rokuv2/colony.json")

# Do it. Build the channel.
buildColonyDev()

