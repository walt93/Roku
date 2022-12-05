from RokuFunctions import *

def buildBurrow():
	output = createOutput("Burrow", "conspyre.tv")

	#prepareAllCategory()

	#Featured content
	loadProgramId(output, "Featured", 60320)	#featured - head 60320
	appendProgramId(output, "Featured", 58493)
	appendProgramId(output, "Featured", 61726)	#featured - tail 61726
	
	#DisclosureHub curated rows
	loadProgramId(output, "Disclosure Hub Hits", 59975)
	loadProgramId(output, "Recommended For You", 59976)
	loadProgramId(output, "Banned Pandemic Doctors", 59978)
	loadProgramId(output, "Lost Covid Videos", 59979)
	loadProgramId(output, "Hidden Health Wealth", 59980)	
	loadProgramId(output, "Real Law Knowledge", 59982)
	loadProgramId(output, "Quantum Human Capabilities", 59983)
	loadProgramId(output, "Human Trafficking / Elite Pedophelia", 59984)
	loadProgramId(output, "Rituals and Satanic Cults", 59985)
	loadProgramId(output, "New World Order", 59986)
	loadProgramId(output, "Free Energy", 59987)
	appendProgramId(output, "Free Energy", 60415)	#Meyer, Stanley
	appendProgramId(output, "Free Energy", 74478)	#Energy from the Vacuum
	loadProgramId(output, "EMF/EMR/RF/5G Radiation", 59988)
	loadProgramId(output, "Extraterrestrial Videos", 59989)
	loadProgramId(output, "Vaccines Exposed", 61701)

	#Just added content
	#loadProgramId(output, "Just Added", 75167)	#just added - head
	loadProgramId(output, "Conspyre.tv just added", 58474)
	#appendProgramId(output, "Just Added", 75168)	#just added - tail

	#Alphabetical categories, documentaries, people
	loadProgramId(output, "5G", 59660)
	loadProgramId(output, "9/11", 59662)
	loadProgramId(output, "Alt. Anthropology", 61754)
	loadProgramId(output, "Antarctica", 60399)
	loadProgramId(output, "BradCGZ", 62937)
	loadProgramId(output, "CIA", 60325)
	loadProgramId(output, "Cooper, William", 59686)
	loadProgramId(output, "Cult of the Medics", 59688)
	loadProgramId(output, "Dark, The", 60328)
	loadProgramId(output, "Disclosure Library", 61762)
	loadProgramId(output, "Enthéos Shines Fan Channel", 59692)
	loadProgramId(output, "Epstein, Jeffrey", 59693)
	loadProgramId(output, "Epstein Pedo Island drone footage", 61761)
	loadProgramId(output, "Fall of the Cabal", 61751)
	loadProgramId(output, "Finders, The", 59694)
	loadProgramId(output, "Freemasons", 59695)
	loadProgramId(output, "General", 74211)
	loadProgramId(output, "Geoengineering", 59697)
	loadProgramId(output, "Giants", 59698)
	loadProgramId(output, "Great Reset", 59699)
	loadProgramId(output, "Gunderson, Ted", 59835)
	loadProgramId(output, "Health, General", 59700)
	loadProgramId(output, "Illuminati", 60402)
	loadProgramId(output, "IPOT1776", 60413)
	loadProgramId(output, "ITNJ Judicial Commission", 60403)
	loadProgramId(output, "JFK", 60405)
	loadProgramId(output, "Lazar, Bob", 60406)
	loadProgramId(output, "Lectures, Conspiracy", 74210)
	loadProgramId(output, "M3thods", 59991)
	loadProgramId(output, "Marrs, Jim", 60414)
	loadProgramId(output, "Maxwell, Jordan", 60407)
	loadProgramId(output, "Mind Control", 60416)
	loadProgramId(output, "Mouthy Buddha", 60411)
	loadProgramId(output, "MrTruthBomb", 69786)
	loadProgramId(output, "Music", 61758)
	loadProgramId(output, "NASA", 60419)
	loadProgramId(output, "ORME", 60420)
	loadProgramId(output, "Pizzagate", 60421)
	loadProgramId(output, "Q", 61753)
	loadProgramId(output, "Remote Viewing", 60905)
	loadProgramId(output, "Schneider, Philip", 60906)
	loadProgramId(output, "Tartaria", 61755)
	loadProgramId(output, "Tyrrany & Eugenics (Jana Esp)", 61757)
	loadProgramId(output, "Thunderbolts Project", 61759)
	loadProgramId(output, "UFOs", 61763)

	writeOutput(output, "/var/www/html/AVideo/rokuv2/burrow.json")

# Do it. Build the channel.
buildBurrow()

# select videos_id from playlists_has_videos where playlists_id in (60320,58493,61726,58474,59975,59976,59978,59979,59980,59982,59983,59984,59985,59986,59987,60415,74478,59988,59989,61701,59660,59662,61754,60399,62937,60325,59686,59688,60328,61762,59692,59693,61761,61751,59694,59695,74211,59697,59698,59699,59835,59700,60402,60413,60403,60405,60406,74210,59991,60414,60407,60416,60411,69786,61758,60418,60419,60420,60421,61753,60905,60906,61755,61757,61759,61763)
