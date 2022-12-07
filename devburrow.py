from RokuFunctions import *

def buildBurrow():
	output = createOutput("Burrow DEV", "conspyre.tv")

	#prepareAllCategory()

	#Featured content
	loadProgramId(output, "Featured", 60320, False)	#featured - head 60320
	appendProgramId(output, "Featured", 58493, False)
	appendProgramId(output, "Featured", 61726, False)	#featured - tail 61726
	
	#DisclosureHub curated rows
	loadProgramId(output, "Disclosure Hub Hits", 59975, False)
	loadProgramId(output, "Recommended For You", 59976, False)
	loadProgramId(output, "Banned Pandemic Doctors", 59978, False)
	loadProgramId(output, "Lost Covid Videos", 59979, False)
	loadProgramId(output, "Hidden Health Wealth", 59980, False)	
	loadProgramId(output, "Real Law Knowledge", 59982, False)
	loadProgramId(output, "Quantum Human Capabilities", 59983, False)
	loadProgramId(output, "Human Trafficking / Elite Pedophelia", 59984, False)
	loadProgramId(output, "Rituals and Satanic Cults", 59985, False)
	loadProgramId(output, "New World Order", 59986, False)
	loadProgramId(output, "Free Energy", 59987, False)
	appendProgramId(output, "Free Energy", 60415)	#Meyer, Stanley
	appendProgramId(output, "Free Energy", 74478)	#Energy from the Vacuum
	loadProgramId(output, "EMF/EMR/RF/5G Radiation", 59988, False)
	loadProgramId(output, "Extraterrestrial Videos", 59989, False)
	loadProgramId(output, "Vaccines Exposed", 61701, False)

	#Just added content
	#loadProgramId(output, "Just Added", 75167, False)	#just added - head
	loadProgramId(output, "Conspyre.tv just added", 58474, False)
	#appendProgramId(output, "Just Added", 75168, False)	#just added - tail

	loadProgramId(output, "TRUTHISKNOWLEDGE", 106372, False)
	loadProgramId(output, "THE EVIL WILL BE EXTINGUISHED COMPLETELY FOREVER", 52585, False)

	#Alphabetical categories, documentaries, people
	loadProgramId(output, "5G", 59660, False)
	loadProgramId(output, "9/11", 59662, False)
	loadProgramId(output, "Alt. Anthropology", 61754, False)
	loadProgramId(output, "Antarctica", 60399, False)
	loadProgramId(output, "Assange, Julian", 58473, False)
	loadProgramId(output, "BradCGZ", 62937, False)
	loadProgramId(output, "CIA", 60325, False)
	loadProgramId(output, "Cooper, William", 59686, False)
	loadProgramId(output, "Cult of the Medics", 59688, False)
	loadProgramId(output, "Dark, The", 60328, False)
	loadProgramId(output, "Disclosure Library", 61762, False)
	loadProgramId(output, "Enthéos Shines Fan Channel", 59692, False)
	loadProgramId(output, "Epstein, Jeffrey", 59693, False)
	loadProgramId(output, "Epstein Pedo Island drone footage", 61761, False)
	loadProgramId(output, "Fall of the Cabal", 61751, False)
	loadProgramId(output, "Finders, The", 59694, False)
	loadProgramId(output, "Freemasons", 59695, False)
	loadProgramId(output, "General", 74211, False)
	loadProgramId(output, "Geoengineering", 59697, False)
	loadProgramId(output, "Giants", 59698, False)
	loadProgramId(output, "Great Reset", 59699, False)
	loadProgramId(output, "Gunderson, Ted", 59835, False)
	loadProgramId(output, "Health, General", 59700, False)
	loadProgramId(output, "Illuminati", 60402, False)
	loadProgramId(output, "IPOT1776", 60413, False)
	loadProgramId(output, "ITNJ Judicial Commission", 60403, False)
	loadProgramId(output, "JFK", 60405, False)
	loadProgramId(output, "Lazar, Bob", 60406, False)
	loadProgramId(output, "Lectures, Conspiracy", 74210, False)
	loadProgramId(output, "M3thods", 59991, False)
	loadProgramId(output, "Marrs, Jim", 60414, False)
	loadProgramId(output, "Maxwell, Jordan", 60407, False)
	loadProgramId(output, "Mind Control", 60416, False)
	loadProgramId(output, "Mouthy Buddha", 60411, False)
	loadProgramId(output, "MrTruthBomb", 69786, False)
	loadProgramId(output, "Music", 61758, False)
	loadProgramId(output, "NASA", 60419, False)
	loadProgramId(output, "ORME", 60420, False)
	loadProgramId(output, "Pizzagate", 60421, False)
	loadProgramId(output, "Q", 61753, False)
	loadProgramId(output, "Remote Viewing", 60905, False)
	loadProgramId(output, "Schneider, Philip", 60906, False)
	loadProgramId(output, "Tartaria", 61755, False)
	loadProgramId(output, "Tyrrany & Eugenics (Jana Esp, False)", 61757, False)
	loadProgramId(output, "Thunderbolts Project", 61759, False)
	loadProgramId(output, "UFOs", 61763, False)

	writeOutput(output, "/var/www/html/AVideo/rokuv2/devburrow.json")

# Do it. Build the channel.
buildBurrow()

# select videos_id from playlists_has_videos where playlists_id in (60320,58493,61726,58474,59975,59976,59978,59979,59980,59982,59983,59984,59985,59986,59987,60415,74478,59988,59989,61701,59660,59662,61754,60399,62937,60325,59686,59688,60328,61762,59692,59693,61761,61751,59694,59695,74211,59697,59698,59699,59835,59700,60402,60413,60403,60405,60406,74210,59991,60414,60407,60416,60411,69786,61758,60418,60419,60420,60421,61753,60905,60906,61755,61757,61759,61763)
