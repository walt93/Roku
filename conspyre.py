from RokuFunctions import *

def buildConspyreTV():
	output = createOutput("Conspyre·TV", "conspyre.tv")

	#prepareAllCategory()

	loadProgramId(output, "Featured", 58493, False)						#Featured content
	loadProgramId(output, "Just Added", 58474, False)

	reserveTopChronological(output, "Recent Tranmissions")				#Alphabetical podcasters
	loadCategory(output,  "Big Dig Energy", "big-dig-energy", True)
	loadCategory(output,  "Brad & Abbey Show", "brad-abbey-show", True)
	loadProgramId(output, "BradCGZ", 62937, True)
	loadProgramId(output, "Disclosure Hub Hits", 59975, True)
	loadProgramId(output, "Enthéos Shines Fan Channel", 59692, False)
	loadProgramId(output, "IPOT1776", 60413, True)
	#loadProgramId(output, "JustInformed Talk", 113460, True)
	loadProgramId(output, "M3thods", 59991, True)
	loadCategory(output,  "TRUreporting", "trureporting", True)

	loadProgramId(output, "Music", 61758, False)							#Music
	loadCategory(output,  "Lisa Mei Crowley", "lisa-mei-crowley", False)								
	loadProgramId(output, "Severe Anon", 103090, False)

	#Alphabetical categories
	loadProgramId(output, "5G", 59660, False)								#SHARED
	loadProgramId(output, "9/11", 59662, False)								#SHARED
	loadProgramId(output, "Adair, David", 60321, False)
	loadProgramId(output, "Alt. Anthropology", 61754, False)				#SHARED
	loadProgramId(output, "Assange, Julian", 58473, False)					#SHARED
	loadProgramId(output, "Bernard, Ronald", 59685, False)
	loadProgramId(output, "CIA", 60325, False)								#SHARED
	loadProgramId(output, "Cooper, William", 59686, False)					#SHARED
	loadProgramId(output, "Cult of the Medics", 59688, False)				#SHARED
	loadProgramId(output, "Dark, The", 60328, False)						#SHARED
	loadCategory(output,  "Detox Project, The", "detox-project", False)
	loadProgramId(output, "Disclosure Hub Hits", 59975, False)				#SHARED
	#loadCategory(output,  "Disclosure Library", "disclosure-library", False)
	loadProgramId(output, "Disney", 59689, False)
	loadProgramId(output, "Dysfunction, Election", 114334, False)
	loadCategory(output,  "Egypt", "egypt", False)
	loadProgramId(output, "Epstein, Jeffrey", 59693, False)					#SHARED
	loadCategory(output,  "Fall of the Cabal", "fall-of-the-cabal", False)	#SHARED
	loadProgramId(output, "Finders, The", 59694, False)						#SHARED
	loadProgramId(output, "Freemasons", 59695, False)						#SHARED
	loadProgramId(output, "Gates, Bill", 59696, False)
	loadProgramId(output, "General", 74211, False)							#SHARED
	loadProgramId(output, "Geoengineering", 59697, False)					#SHARED
	loadProgramId(output, "Giants", 59698, False)							#SHARED
	loadProgramId(output, "Great Reset", 59699, False)						#SHARED
	loadProgramId(output, "Gunderson, Ted", 59835, False)					#SHARED
	loadCategory(output,  "Healing from GMOs", "healing-from-gmos", False)
	loadProgramId(output, "Health, General", 59700, False)					#SHARED
	loadCategory(output,  "Illuminati",  "illuminati", False)
	loadProgramId(output, "ITNJ Judicial Commission", 60403, False)			#SHARED
	loadCategory(output,  "Jacob, Frank", "frank-jacob", False)
	loadCategory(output,  "JFK", "jfk", False)								#SHARED
	loadCategory(output,  "Lazar, Bob", "bob-lazar", False)					#SHARED
	loadCategory(output,  "Marrs, Jim", "jim-marrs", False)					#SHARED
	loadCategory(output,  "Maxwell, Jordan", "jordan-maxwell", False)		#SHARED
	loadCategory(output,  "Megaliths", "megalithic-sites", False)
	loadCategory(output,  "Meyer, Stanley", "stanley-meyer", False)
	loadProgramId(output, "Mind Control", 60416, False)						#SHARED
	loadProgramId(output, "Mouthy Buddha", 60411, False)					#SHARED
	loadProgramId(output, "MrTruthBomb", 69786, False)						#SHARED
	loadCategory(output,  "Mystery Babylon Radio", "mystery-babylon-radio-archive", False)
	loadProgramId(output, "NASA", 60419, False)								#SHARED
	loadProgramId(output, "ORME", 60420, False)								#SHARED
	loadCategory(output,  "Pizzagate", "pizzagate", False)
	loadCategory(output,  "Project Camelot", "project-camelot", False)
	loadProgramId(output, "Pizzagate", 60421, False)						#SHARED
	loadProgramId(output, "Remote Viewing", 60905, False)					#SHARED
	loadProgramId(output, "Schneider, Philip", 60906, False)				#SHARED
	loadProgramId(output, "Shackleford, Rusty (Pedo Island drone footage)", 61761, False)	#SHARED
	loadCategory(output,  "Springmeier, Fritz", "fritz-springmeier", False)
	loadCategory(output,  "SRA", "sra", False)
	loadProgramId(output, "Tartaria", 61755, False)							#SHARED
	loadCategory(output,  "Tellinger, Michael", "michael-tellinger", False)
	loadCategory(output,  "Tesla, Nikola", "nikola-tesla", False)
	loadCategory(output,  "Truth About Cancer, the", "the-truth-about-cancer" , False)
	loadProgramId(output, "TRUTHISKNOWLEDGE", 106372, False)
	loadProgramId(output, "Tyrrany & Eugenics (Jana Esp)", 61757, False)	#SHARED
	loadProgramId(output, "Thunderbolts Project", 61759, False)				#SHARED
	loadProgramId(output, "UFOs", 61763, False)								#SHARED

	writeOutput(output, "/var/www/html/AVideo/rokuv2/conspyre-tv.json")

# Do it. Build the channel.
buildConspyreTV()

	#loadCategory(output, "Beyond Chemo docuseries", "beyond-chemo-docuseries", False)
	#loadCategory(output, "CIA", "general-7", False)
	#loadCategory(output, "Conquering Cancer Summit", "conquering-cancer-summit-2021", False)
	#loadCategory(output, "Conscious Life Expo (2020)", "conscious-life-expo-2020-", False)
#	loadCategory(output, "Pedophiles & Human Trafficking", "pedophiles-human-trafficking", False)
#	loadCategory(output, "Tsarion, Michael", "michael-tsarion", False)

# from RokuFunctions import *

# def buildConspyreTV():
# 	output = createOutput("Conspyre·TV", "conspyre.tv")

# 	prepareAllCategory()

# 	#Featured content
# 	curlJsonDict(output, "Featured: #AssangeAThon",			"manual", "https://conspyre.tv/roku.json?program_id=58473")
# 	curlJsonDict(output, "Featured",						"manual", "https://conspyre.tv/roku.json?program_id=58493")
# 	curlJsonDict(output, "Just Added",						"manual", "https://conspyre.tv/roku.json?program_id=58493")

# 	#Alphabetical podcasters
# 	curlJsonDict(output, "M3thods",							"manual", "https://conspyre.tv/roku.json?program_id=59991")
# 	#curlJsonDict(output, "Quite Frankly",					"manual", "https://conspyre.tv/roku.json?catName=quite-frankly")
# 	#curlJsonDict(output, "RedPill78",						"manual", "https://conspyre.tv/roku.json?catName=redpill78")
# 	#curlJsonDict(output, "Tru Reporting",					"manual", "https://conspyre.tv/roku.json?catName=tru-reporting")
# 	#curlJsonDict(output, "WokeSocieties",					"manual", "https://conspyre.tv/roku.json?catName=woke-societies")

# 	#Alphabetical categories
# 	curlJsonDict(output, "5G", 								"manual", "https://conspyre.tv/roku.json?program_id=59660")
# 	curlJsonDict(output, "5G Crisis: Awareness & Accountability", "manual", "https://conspyre.tv/roku.json?program_id=59661")
# 	curlJsonDict(output, "9/11", 							"manual", "https://conspyre.tv/roku.json?program_id=59662")
# 	curlJsonDict(output, "Adair, David",					"manual", "https://conspyre.tv/roku.json?program_id=60321")
# 	#curlJsonDict(output, "Ancient Civilizations",			"manual",  "https://conspyre.tv/roku.json?catName=general-2")
# 	curlJsonDict(output, "Bauval, Robert",					"manual", "https://conspyre.tv/roku.json?program_id=60322")
# 	curlJsonDict(output, "Bernard, Ronald", 				"manual", "https://conspyre.tv/roku.json?program_id=59685")
# 	#curlJsonDict(output, "Beyond Chemo docuseries",		"manual",  "https://conspyre.tv/roku.json?catName=beyond-chemo-docuseries")
# 	#curlJsonDict(output, "CIA",							"manual",  "https://conspyre.tv/roku.json?catName=general-7")
# 	#curlJsonDict(output, "Conquering Cancer Summit",		"manual",  "https://conspyre.tv/roku.json?catName=conquering-cancer-summit-2021")
# 	#curlJsonDict(output, "Conscious Life Expo (2020)",		"manual",  "https://conspyre.tv/roku.json?catName=conscious-life-expo-2020-")
# 	curlJsonDict(output, "Cooper, William", 				"manual", "https://conspyre.tv/roku.json?program_id=59686")
# 	#curlJsonDict(output, "Coral Castle, The",				"manual",  "https://conspyre.tv/roku.json?catName=coral-castle")
# 	#curlJsonDict(output, "Crop Circles",					"manual",  "https://conspyre.tv/roku.json?catName=crop-circles")
# 	curlJsonDict(output, "Cult of the Medics", 				"manual", "https://conspyre.tv/roku.json?program_id=59688")
# 	curlJsonDict(output, "Dark, The",						"manual", "https://conspyre.tv/roku.json?catName=conspyre-dark")
# 	curlJsonDict(output, "Detox Project, The",				"manual", "https://conspyre.tv/roku.json?catName=detox-project")
# 	curlJsonDict(output, "Disclosure Hub",					"manual", "https://conspyre.tv/roku.json?catName=general-6")
# 	curlJsonDict(output, "Disclosure Library",				"manual",  "https://conspyre.tv/roku.json?catName=disclosure-library")
# 	curlJsonDict(output, "Disney",							"manual", "https://conspyre.tv/roku.json?program_id=59689")
# 	curlJsonDict(output, "Egypt",							"manual",  "https://conspyre.tv/roku.json?catName=egypt")
# 	#curlJsonDict(output, "EMF Health Summit",				"manual",  "https://conspyre.tv/roku.json?catName=emf-health-summit")
# 	curlJsonDict(output, "Enthéos Shines Fan Channel",		"manual", "https://conspyre.tv/roku.json?program_id=59692")
# 	curlJsonDict(output, "Epstein, Jeffrey",				"manual", "https://conspyre.tv/roku.json?program_id=59693")
# 	curlJsonDict(output, "Fall of the Cabal",				"manual", "https://conspyre.tv/roku.json?catName=fall-of-the-cabal")
# 	#curlJsonDict(output, "Fake Election",					"manual", "https://conspyre.tv/roku.json?catName=11-3-fake-election")
# 	curlJsonDict(output, "Finders, The",					"manual", "https://conspyre.tv/roku.json?program_id=59694")
# 	curlJsonDict(output, "Freemasons",						"manual", "https://conspyre.tv/roku.json?program_id=59695")
# 	curlJsonDict(output, "Gates, Bill", 					"manual", "https://conspyre.tv/roku.json?program_id=59696")
# 	curlJsonDict(output, "General", 						"manual", "https://conspyre.tv/roku.json?catName=conspyre-tv")
# 	curlJsonDict(output, "Geoengineering", 					"manual", "https://conspyre.tv/roku.json?program_id=59697")
# 	curlJsonDict(output, "Giants",							"manual", "https://conspyre.tv/roku.json?program_id=59698")
# 	curlJsonDict(output, "Great Reset",						"manual", "https://conspyre.tv/roku.json?program_id=59699")
# 	#curlJsonDict(output, "Griffin, G. Edward",				"manual",  "https://conspyre.tv/roku.json?catName=g-edward-griffin")
# 	curlJsonDict(output, "Gunderson, Ted",					"manual", "https://conspyre.tv/roku.json?program_id=59835")
# 	curlJsonDict(output, "Hancock, Graham",					"manual",	 "https://conspyre.tv/roku.json?catName=graham-hancock")
# 	curlJsonDict(output, "Healing from GMOs",				"manual",  "https://conspyre.tv/roku.json?catName=healing-from-gmos")
# #	curlJsonDict(output, "Health, General",					"manual",  "https://conspyre.tv/roku.json?catName=conspyre-health")
# #	curlJsonDict(output, "Heavy Metals Summit",				"manual",  "https://conspyre.tv/roku.json?catName=heavy-metals-summit")
# #	curlJsonDict(output, "Hoagland, Richard",				"manual",  "https://conspyre.tv/roku.json?catName=richard-hoagland")
# #	curlJsonDict(output, "Humor",							"manual",  "https://conspyre.tv/roku.json?catName=humor")
# #	curlJsonDict(output, "Keto Edge Summit",				"manual",  "https://conspyre.tv/roku.json?catName=keto-edge-summit")
# 	curlJsonDict(output, "Illuminati",						"manual",  "https://conspyre.tv/roku.json?catName=illuminati")
# 	curlJsonDict(output, "ITNJ Judicial Commission",		"manual", "https://conspyre.tv/roku.json?catName=itnj-judicial-comission")
# 	curlJsonDict(output, "IPOT1776",						"manual",  "https://conspyre.tv/roku.json?catName=ipot1776")
# 	curlJsonDict(output, "Jacob, Frank",					"manual",  "https://conspyre.tv/roku.json?catName=frank-jacob")
# 	curlJsonDict(output, "JFK",								"manual",  "https://conspyre.tv/roku.json?catName=jfk")
# 	curlJsonDict(output, "Lazar, Bob",						"manual",  "https://conspyre.tv/roku.json?catName=bob-lazar")
# #	curlJsonDict(output, "Live Longer Feel Better",			"manual",  "https://conspyre.tv/roku.json?catName=live-longer-feel-better")
# 	curlJsonDict(output, "Maxwell, Jordan",					"manual",  "https://conspyre.tv/roku.json?catName=jordan-maxwell")
# 	curlJsonDict(output, "Marrs, Jim",						"manual",  "https://conspyre.tv/roku.json?catName=jim-marrs")
# 	curlJsonDict(output, "Megaliths",						"manual",	 "https://conspyre.tv/roku.json?catName=megalithic-sites")
# 	curlJsonDict(output, "Meyer, Stanley",					"manual",  "https://conspyre.tv/roku.json?catName=stanley-meyer")
# 	curlJsonDict(output, "Mind Control",					"manual",  "https://conspyre.tv/roku.json?catName=documentary-3")
# #	curlJsonDict(output, "MK-ULTRA",						"manual",  "https://conspyre.tv/roku.json?catName=mk-ultra")
# 	curlJsonDict(output, "Mouthy Buddha",					"manual",  "https://conspyre.tv/roku.json?catName=mouthy-buddha")
# 	curlJsonDict(output, "Music",							"manual",  "https://conspyre.tv/roku.json?catName=music")
# 	curlJsonDict(output, "Mystery Babylon Radio",			"manual", "https://conspyre.tv/roku.json?catName=mystery-babylon-radio-archive")
# #	curlJsonDict(output, "NASA",							"manual",  "https://conspyre.tv/roku.json?catName=nasa")
# #	curlJsonDict(output, "ORME",							"manual",  "https://conspyre.tv/roku.json?catName=ormus-orme")
# #	curlJsonDict(output, "Pedophiles & Human Trafficking",	"manual",  "https://conspyre.tv/roku.json?catName=pedophiles-human-trafficking")
# 	curlJsonDict(output, "Pizzagate",						"manual",  "https://conspyre.tv/roku.json?catName=pizzagate")
# 	curlJsonDict(output, "Project Camelot",					"manual",  "https://conspyre.tv/roku.json?catName=project-camelot")
# 	curlJsonDict(output, "Q",								"manual",  "https://conspyre.tv/roku.json?catName=q")
# #	curlJsonDict(output, "Remote Viewing",					"manual",  "https://conspyre.tv/roku.json?catName=remote-viewing")
# 	curlJsonDict(output, "Schneider, Philip",				"manual",  "https://conspyre.tv/roku.json?catName=philip-schneider")
# 	curlJsonDict(output, "Sepehr, Robert",					"manual",  "https://conspyre.tv/roku.json?catName=anthropology")
# 	curlJsonDict(output, "Shackleford, Rusty (Pedo Island drone footage)", "manual",  "https://conspyre.tv/roku.json?catName=rusty-shackleford")
# 	curlJsonDict(output, "Springmeier, Fritz",				"manual",  "https://conspyre.tv/roku.json?catName=fritz-springmeier")
# 	curlJsonDict(output, "SRA",								"manual",  "https://conspyre.tv/roku.json?catName=sra")
# #	curlJsonDict(output, "Superfood Garden Summit",			"manual",  "https://conspyre.tv/roku.json?catName=superfood-garden-summit")
# 	curlJsonDict(output, "Tartaria",						"manual",  "https://conspyre.tv/roku.json?catName=tartaria")
# 	curlJsonDict(output, "Tellinger, Michael", 				"manual",  "https://conspyre.tv/roku.json?catName=michael-tellinger")
# 	curlJsonDict(output, "Tesla, Nikola",	 				"manual",  "https://conspyre.tv/roku.json?catName=nikola-tesla")
# #	curlJsonDict(output, "Thriving Child Summit",			"manual",  "https://conspyre.tv/roku.json?catName=thriving-child-summit")
# #	curlJsonDict(output, "Toxic Home Summit", 				"manual",  "https://conspyre.tv/roku.json?catName=toxic-home-summit")
# 	curlJsonDict(output, "Truth About Cancer, the",			"manual",  "https://conspyre.tv/roku.json?catName=the-truth-about-cancer" )
# 	curlJsonDict(output, "Tyrrany & Eugenics (Jana Esp)",	"manual", "https://conspyre.tv/roku.json?catName=jana-esp")
# #	curlJsonDict(output, "Thunderbolts Project",			"manual",  "https://conspyre.tv/roku.json?catName=thunderbolts-project")
# #	curlJsonDict(output, "Tsarion, Michael",				"manual",  "https://conspyre.tv/roku.json?catName=michael-tsarion")
# 	curlJsonDict(output, "UFOs",							"manual",  "https://conspyre.tv/roku.json?catName=lectures-1")
# #	curlJsonDict(output, "West, John Anthony",				"manual",  "https://conspyre.tv/roku.json?catName=john-anthony-west")

# 	writeOutput(output, "/var/www/html/AVideo/rokuv2/conspyre-tv.json")

# # Do it. Build the channel.
# buildConspyreTV()

