from RokuFunctions import *

def buildBurrow():
	output = createOutput("Burrow•DEV", "conspyre.tv")

	#prepareAllCategory()

	#Featured content
	loadProgramId(output, "Featured", 60320)	#featured - head 60320
	appendProgramId(output, "Featured", 58493)
	appendProgramId(output, "Featured", 61726)	#featured - tail 61726
	loadProgramId(output, "Just Added", 58474)

	#Alphabetical podcasters
	loadProgramId(output, "BradCGZ", 62937)
	loadProgramId(output, "IPOT1776", 60413)
	loadProgramId(output, "Lisa Mei Crowley", 70798)
	loadProgramId(output, "M3thods", 59991)
	loadProgramId(output, "Mouthy Buddha", 60411)
	loadProgramId(output, "Patel Patriot", 67973)
	loadProgramId(output, "Quite Frankly", 67997)
	loadProgramId(output, "RedPill78", 67996)
	loadProgramId(output, "Severe Anon", 70797)
	loadProgramId(output, "Tru Reporting", 67998)
	loadProgramId(output, "Woke Societies", 67999)

	writeOutput(output, "/var/www/html/AVideo/rokuv2/devcolony.json")

# Do it. Build the channel.
buildBurrow()

