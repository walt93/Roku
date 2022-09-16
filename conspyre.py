from RokuFunctions import *

def buildConspyreTV():
	output = createOutput("Conspyre·TV")

	#prepareAllCategory()

	#Featured content
	curlJsonDict(output, "Featured: #AssangeAThon",			"most_popular",  "https://conspyre.tv/roku.json?catName=julian-assange")
	curlJsonDict(output, "Featured",						"most_popular",  "https://conspyre.tv/roku.json?catName=featured")
#	curlJsonDict(output, "Featured",						"manual", "https://conspyre.tv/roku.json?program_id=58493")

	#Alphabetical podcasters
	curlJsonDict(output, "M3thods",							"most_popular",  "https://conspyre.tv/roku.json?catName=m3thods")
	#curlJsonDict(output, "Quite Frankly",					"most_popular", "https://conspyre.tv/roku.json?catName=quite-frankly")
	#curlJsonDict(output, "RedPill78",						"most_popular", "https://conspyre.tv/roku.json?catName=redpill78")
	#curlJsonDict(output, "Tru Reporting",					"most_popular", "https://conspyre.tv/roku.json?catName=tru-reporting")
	#curlJsonDict(output, "WokeSocieties",					"most_popular", "https://conspyre.tv/roku.json?catName=woke-societies")

	#Alphabetical categories
	curlJsonDict(output, "5G",								"most_popular", "https://conspyre.tv/roku.json?catName=5g")
	curlJsonDict(output, "5G Crisis: Awareness & Accountability",	"most_popular", "https://conspyre.tv/roku.json?catName=5g-crisis-awareness-accountability")
	curlJsonDict(output, "9/11",							"most_popular", "https://conspyre.tv/roku.json?catName=9-11")
#	curlJsonDict(output, "Adair, David",					"most_popular",  "https://conspyre.tv/roku.json?catName=david-adair")
#	curlJsonDict(output, "Ancient Civilizations",			"most_popular",  "https://conspyre.tv/roku.json?catName=general-2")
#	curlJsonDict(output, "Bauval, Robert",					"most_popular",  "https://conspyre.tv/roku.json?catName=robert-bauval")
	curlJsonDict(output, "Bernard, Ronald",					"most_popular",  "https://conspyre.tv/roku.json?catName=ronald-bernard")
#	curlJsonDict(output, "Beyond Chemo docuseries",			"most_popular",  "https://conspyre.tv/roku.json?catName=beyond-chemo-docuseries")
#	curlJsonDict(output, "CIA",								"most_popular",  "https://conspyre.tv/roku.json?catName=general-7")
#	curlJsonDict(output, "Conquering Cancer Summit",		"most_popular",  "https://conspyre.tv/roku.json?catName=conquering-cancer-summit-2021")
#	curlJsonDict(output, "Conscious Life Expo (2020)",		"most_popular",  "https://conspyre.tv/roku.json?catName=conscious-life-expo-2020-")
	curlJsonDict(output, "Cooper, William",					"most_popular",  "https://conspyre.tv/roku.json?catName=videos")
#	curlJsonDict(output, "Coral Castle, The",				"most_popular",  "https://conspyre.tv/roku.json?catName=coral-castle")
#	curlJsonDict(output, "Crop Circles",					"most_popular",  "https://conspyre.tv/roku.json?catName=crop-circles")
	curlJsonDict(output, "Cult of the Medics",				"chronological", "https://conspyre.tv/roku.json?catName=cult-of-the-medics")
	curlJsonDict(output, "Dark, The",						"most_popular",  "https://conspyre.tv/roku.json?catName=conspyre-dark")
	curlJsonDict(output, "Detox Project, The",				"most_popular",  "https://conspyre.tv/roku.json?catName=detox-project")
	curlJsonDict(output, "Disclosure Hub",					"most_popular",  "https://conspyre.tv/roku.json?catName=general-6")
#	curlJsonDict(output, "Disclosure Library",				"most_popular",  "https://conspyre.tv/roku.json?catName=disclosure-library")
	curlJsonDict(output, "Disney",							"most_popular",  "https://conspyre.tv/roku.json?catName=disney")
	curlJsonDict(output, "Egypt",							"most_popular",  "https://conspyre.tv/roku.json?catName=egypt")
#	curlJsonDict(output, "EMF Health Summit",				"most_popular",  "https://conspyre.tv/roku.json?catName=emf-health-summit")
	curlJsonDict(output, "Enthéos Shines Fan Channel",		"most_popular",  "https://conspyre.tv/roku.json?catName=entheos-shines-fan-channel")
	curlJsonDict(output, "Epstein, Jeffrey",				"most_popular",  "https://conspyre.tv/roku.json?catName=general-8")
	curlJsonDict(output, "Fall of the Cabal",				"most_recent",   "https://conspyre.tv/roku.json?catName=fall-of-the-cabal")
	curlJsonDict(output, "Fake Election",					"most_recent",   "https://conspyre.tv/roku.json?catName=11-3-fake-election")
	curlJsonDict(output, "Finders, The",					"most_popular",  "https://conspyre.tv/roku.json?catName=the-finders")
	curlJsonDict(output, "Freemasons",						"most_popular",  "https://conspyre.tv/roku.json?catName=freemasons")
	curlJsonDict(output, "Gates, Bill",						"most_popular",  "https://conspyre.tv/roku.json?catName=bill-gates")
	curlJsonDict(output, "General",							"most_popular",  "https://conspyre.tv/roku.json?catName=conspyre-tv")
	curlJsonDict(output, "Geoengineering",					"most_popular",  "https://conspyre.tv/roku.json?catName=geoengineering")
	curlJsonDict(output, "Giants",							"most_popular",  "https://conspyre.tv/roku.json?catName=giants")
	curlJsonDict(output, "Great Reset",						"most_popular",  "https://conspyre.tv/roku.json?catName=great-reset")
#	curlJsonDict(output, "Griffin, G. Edward",				"most_popular",  "https://conspyre.tv/roku.json?catName=g-edward-griffin")
	curlJsonDict(output, "Gunderson, Ted",					"most_popular",  "https://conspyre.tv/roku.json?catName=ted-gunderson")
	curlJsonDict(output, "Hancock, Graham",					"most_popular",	 "https://conspyre.tv/roku.json?catName=graham-hancock")
	curlJsonDict(output, "Healing from GMOs",				"most_popular",  "https://conspyre.tv/roku.json?catName=healing-from-gmos")
#	curlJsonDict(output, "Health, General",					"most_popular",  "https://conspyre.tv/roku.json?catName=conspyre-health")
#	curlJsonDict(output, "Heavy Metals Summit",				"most_popular",  "https://conspyre.tv/roku.json?catName=heavy-metals-summit")
#	curlJsonDict(output, "Hoagland, Richard",				"most_popular",  "https://conspyre.tv/roku.json?catName=richard-hoagland")
#	curlJsonDict(output, "Humor",							"most_popular",  "https://conspyre.tv/roku.json?catName=humor")
#	curlJsonDict(output, "Keto Edge Summit",				"most_popular",  "https://conspyre.tv/roku.json?catName=keto-edge-summit")
	curlJsonDict(output, "Illuminati",						"most_popular",  "https://conspyre.tv/roku.json?catName=illuminati")
	curlJsonDict(output, "ITNJ Judicial Commission",		"chronological", "https://conspyre.tv/roku.json?catName=itnj-judicial-comission")
	curlJsonDict(output, "IPOT1776",						"most_popular",  "https://conspyre.tv/roku.json?catName=ipot1776")
	curlJsonDict(output, "Jacob, Frank",					"most_popular",  "https://conspyre.tv/roku.json?catName=frank-jacob")
	curlJsonDict(output, "JFK",								"most_popular",  "https://conspyre.tv/roku.json?catName=jfk")
#	curlJsonDict(output, "Live Longer Feel Better",			"most_popular",  "https://conspyre.tv/roku.json?catName=live-longer-feel-better")
	curlJsonDict(output, "Maxwell, Jordan",					"most_popular",  "https://conspyre.tv/roku.json?catName=jordan-maxwell")
	curlJsonDict(output, "Marrs, Jim",						"most_popular",  "https://conspyre.tv/roku.json?catName=jim-marrs")
	curlJsonDict(output, "Megaliths",						"most_popular",	 "https://conspyre.tv/roku.json?catName=megalithic-sites")
	curlJsonDict(output, "Meyer, Stanley",					"most_popular",  "https://conspyre.tv/roku.json?catName=stanley-meyer")
	curlJsonDict(output, "Mind Control",					"most_popular",  "https://conspyre.tv/roku.json?catName=documentary-3")
#	curlJsonDict(output, "MK-ULTRA",						"most_popular",  "https://conspyre.tv/roku.json?catName=mk-ultra")
	curlJsonDict(output, "Mouthy Buddha",					"most_popular",  "https://conspyre.tv/roku.json?catName=mouthy-buddha")
	curlJsonDict(output, "Music",							"most_popular",  "https://conspyre.tv/roku.json?catName=music")
	curlJsonDict(output, "Mystery Babylon Radio",			"chronological", "https://conspyre.tv/roku.json?catName=mystery-babylon-radio-archive")
#	curlJsonDict(output, "NASA",							"most_popular",  "https://conspyre.tv/roku.json?catName=nasa")
#	curlJsonDict(output, "ORME",							"most_popular",  "https://conspyre.tv/roku.json?catName=ormus-orme")
#	curlJsonDict(output, "Pedophiles & Human Trafficking",	"most_popular",  "https://conspyre.tv/roku.json?catName=pedophiles-human-trafficking")
	curlJsonDict(output, "Pizzagate",						"most_popular",  "https://conspyre.tv/roku.json?catName=pizzagate")
	curlJsonDict(output, "Project Camelot",					"most_popular",  "https://conspyre.tv/roku.json?catName=project-camelot")
	curlJsonDict(output, "Q",								"most_popular",  "https://conspyre.tv/roku.json?catName=q")
#	curlJsonDict(output, "Remote Viewing",					"most_popular",  "https://conspyre.tv/roku.json?catName=remote-viewing")
	curlJsonDict(output, "Schneider, Philip",				"most_popular",  "https://conspyre.tv/roku.json?catName=philip-schneider")
	curlJsonDict(output, "Sepehr, Robert",					"most_popular",  "https://conspyre.tv/roku.json?catName=anthropology")
	curlJsonDict(output, "Shackleford, Rusty (Pedo Island drone footage)", "most_popular",  "https://conspyre.tv/roku.json?catName=rusty-shackleford")
	curlJsonDict(output, "Springmeier, Fritz",				"most_popular",  "https://conspyre.tv/roku.json?catName=fritz-springmeier")
	curlJsonDict(output, "SRA",								"most_popular",  "https://conspyre.tv/roku.json?catName=sra")
#	curlJsonDict(output, "Superfood Garden Summit",			"most_popular",  "https://conspyre.tv/roku.json?catName=superfood-garden-summit")
	curlJsonDict(output, "Tartaria",						"most_popular",  "https://conspyre.tv/roku.json?catName=tartaria")
	curlJsonDict(output, "Tellinger, Michael", 				"most_popular",  "https://conspyre.tv/roku.json?catName=michael-tellinger")
	curlJsonDict(output, "Tesla, Nikola",	 				"most_popular",  "https://conspyre.tv/roku.json?catName=nikola-tesla")
#	curlJsonDict(output, "Thriving Child Summit",			"most_popular",  "https://conspyre.tv/roku.json?catName=thriving-child-summit")
#	curlJsonDict(output, "Toxic Home Summit", 				"most_popular",  "https://conspyre.tv/roku.json?catName=toxic-home-summit")
	curlJsonDict(output, "Truth About Cancer, the",			"most_popular",  "https://conspyre.tv/roku.json?catName=the-truth-about-cancer" )
	curlJsonDict(output, "Tyrrany & Eugenics (Jana Esp)",	"most_recent", "https://conspyre.tv/roku.json?catName=jana-esp")
#	curlJsonDict(output, "Thunderbolts Project",			"most_popular",  "https://conspyre.tv/roku.json?catName=thunderbolts-project")
#	curlJsonDict(output, "Tsarion, Michael",				"most_popular",  "https://conspyre.tv/roku.json?catName=michael-tsarion")
	curlJsonDict(output, "UFOs",							"most_popular",  "https://conspyre.tv/roku.json?catName=lectures-1")
#	curlJsonDict(output, "West, John Anthony",				"most_popular",  "https://conspyre.tv/roku.json?catName=john-anthony-west")

	writeOutput(output, "/var/www/html/AVideo/rokuv2/conspyre-tv.json")