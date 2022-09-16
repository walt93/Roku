from RokuFunctions import *

def buildMrTruthBomb():
	output = createOutput("Conspyre·MrTruthBomb")

	#prepareAllCategory()

	curlJsonDict(output, "Death of the Deep State",			"chronological",	"https://conspyre.tv/roku.json?program_id=59654")
	curlJsonDict(output, "Death of the Deep State (segments)",	"most_popular",		"https://conspyre.tv/roku.json?program_id=59655")

	curlJsonDict(output, "Deep State War",				"chronological",	"https://conspyre.tv/roku.json?program_id=59645")
	curlJsonDict(output, "Deep State War (segments)",		"most_popular",		"https://conspyre.tv/roku.json?program_id=59653")

	curlJsonDict(output, "Devolution",				"chronological",	"https://conspyre.tv/roku.json?program_id=59647")

	curlJsonDict(output, "Durham",					"chronological",	"https://conspyre.tv/roku.json?program_id=59648")
	curlJsonDict(output, "Durham (segments)",			"most_popular",		"https://conspyre.tv/roku.json?program_id=59656")

	curlJsonDict(output, "Election Deception",			"chronological",	"https://conspyre.tv/roku.json?program_id=59649")
	curlJsonDict(output, "Election Deception (segments)",		"most_popular",		"https://conspyre.tv/roku.json?program_id=59657")

	curlJsonDict(output, "Plandemic Scamdemic",			"chronological",	"https://conspyre.tv/roku.json?program_id=59646")
	curlJsonDict(output, "Plandemic Scamdemic (segments)",		"most_popular",		"https://conspyre.tv/roku.json?program_id=59658")

	curlJsonDict(output, "Putin vs the Deep State",			"chronological",	"https://conspyre.tv/roku.json?program_id=59650")
	curlJsonDict(output, "Putin vs the Deep State (segments)",	"most_popular",		"https://conspyre.tv/roku.json?program_id=59659")

	curlJsonDict(output, "Other",					"most_popular",		"https://conspyre.tv/roku.json?program_id=59652")

	writeOutput(output, "/var/www/html/AVideo/rokuv2/mrtruthbomb.json")

# Do it. Build the channel.
buildMrTruthBomb()