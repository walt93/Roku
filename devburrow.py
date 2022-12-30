from RokuFunctions import *

def buildConspyreTV():
	output = createOutput("Conspyre·TV", "conspyre.tv")

	#Featured content
	loadProgramId(output, "Featured", 60320, False)	#featured - head 60320
	appendProgramId(output, "Featured", 58493)
	appendProgramId(output, "Featured", 61726)	#featured - tail 61726
	
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
	#appendProgramId(output, "Just Added", 75168)	#just added - tail

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
buildConspyreTV()

	#loadCategory(output, "Beyond Chemo docuseries", "beyond-chemo-docuseries", False)
	#loadCategory(output, "CIA", "general-7", False)
	#loadCategory(output, "Conquering Cancer Summit", "conquering-cancer-summit-2021", False)
	#loadCategory(output, "Conscious Life Expo (2020)", "conscious-life-expo-2020-", False)
#	loadCategory(output, "Pedophiles & Human Trafficking", "pedophiles-human-trafficking", False)
#	loadCategory(output, "Tsarion, Michael", "michael-tsarion", False)
