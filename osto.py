from RokuFunctions import *

def buildOSTO():
	output = createOutput("OSTO•Space", "conspyre.tv")
							
	loadProgramId(output, "Featured", 92884)

	#Alphabetical categories
	loadProgramId(output, "1/6/2021 PRISONERS", 92861)
	loadProgramId(output, "ELECTILE DYSFUNCTION", 92871)
	loadProgramId(output, "THE JABS", 92891)
	loadProgramId(output, "HUMAN TRAFFICKING", 92872)
	loadProgramId(output, "THE SATANICS", 92892)
	loadProgramId(output, "DEEP STATE MEANS OBAMAGATE", 92869
	loadProgramId(output, "CRYPTO-CURRENCY & (QFS)", 92868)
	loadProgramId(output, "CPS-ADOPTION-FOSTER SYSTEM", 92867)
	loadProgramId(output, "ADRENOCHROME IS PEOPLE", 92862)
	loadProgramId(output, "Bohemian Grove Rhapsody", 92863)
	loadProgramId(output, "Q", 92885)
	loadProgramId(output, "LINDA \"snarky\" PARIS", 92877)
	loadProgramId(output, "X22 REPORT", 92895)
	loadProgramId(output, "WE THE PEOPLE (the situation)", 92894)
	loadProgramId(output, "SANTA SURFING", 92887)
	loadProgramId(output, "MITCHELL NICHOLAS GERBER", 92881)
	loadProgramId(output, "MELK", 92880)
	loadProgramId(output, "MARTIN GEDDES", 92879)
	loadProgramId(output, "THE FULFORD REPORT", 92890)
	loadProgramId(output, "STEW PETERS", 92889)
	loadProgramId(output, "SIMON PARKES", 92888)
	loadProgramId(output, "RYUSHIN MALONE", 92886)
	loadProgramId(output, "KERRY CASSIDY", 92875)
	loadProgramId(output, "JEAN WARDS MARS ANOMALY", 92874)
	loadProgramId(output, "COREYS DIGS", 92866)
	loadProgramId(output, "COREY GOODE", 92865)
	loadProgramId(output, "\"THE SALLA\"", 92860)
	loadProgramId(output, "CONSPIRACY FACT", 92864)
	loadProgramId(output, "INTERNATIONAL TRUTH HEROES", 92873)
	loadProgramId(output, "NEW DIGITAL SOLDIERS", 92882)
	loadProgramId(output, "Lynn Miller -Intuitive Empath", 92878)
	loadProgramId(output, "KNOWLEDGE OF THE FOREVER TIME", 92876)
	loadProgramId(output, "OSTO PAGES", 92883)
	loadProgramId(output, "STRANGERS IN YOUR OWN LAND", 92859)
	loadProgramId(output, "DISCLOSURE SONGS", 92870)
	loadProgramId(output, "THE SCREAMING MEMER", 92893)

	writeOutput(output, "/var/www/html/AVideo/osto.json")

# Do it. Build the channel.
buildOSTO()
