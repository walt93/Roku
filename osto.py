from RokuFunctions import *

def buildOSTO():
	output = createOutput("OSTO•Space", "truth.osto.space")
							
	loadCategory(output, "Featured", "osto-tv-content")

	#Alphabetical categories
	loadCategory(output, "OSTO TV CONTENT", "https://truth.osto.space/roku.json?catName=osto-tv-content")
	loadCategory(output, "1/6/2021 PRISONERS", "https://truth.osto.space/roku.json?catName=1-6-2021-prisoners")
	loadCategory(output, "ELECTILE DYSFUNCTION", "https://truth.osto.space/roku.json?catName=electile-dysfunction")
	loadCategory(output, "THE JABS", "https://truth.osto.space/roku.json?catName=the-jabs")
	loadCategory(output, "HUMAN TRAFFICKING", "https://truth.osto.space/roku.json?catName=human-trafficking")
	loadCategory(output, "THE SATANICS", "https://truth.osto.space/roku.json?catName=the-satanics")
	loadCategory(output, "DEEP STATE MEANS OBAMAGATE", "https://truth.osto.space/roku.json?catName=deep-state-means-obamagate")
	loadCategory(output, "CRYPTO-CURRENCY & (QFS)", "https://truth.osto.space/roku.json?catName=crypto-currency-qfs")
	loadCategory(output, "CPS-ADOPTION-FOSTER SYSTEM", "https://truth.osto.space/roku.json?catName=cps-adoption-foster-system")
	loadCategory(output, "ADRENOCHROME IS PEOPLE", "https://truth.osto.space/roku.json?catName=adrenochrome-is-people")
	loadCategory(output, "Bohemian Grove Rhapsody", "https://truth.osto.space/roku.json?catName=bohemian-grove-rhapsody")
	loadCategory(output, "Q", "https://truth.osto.space/roku.json?catName=q")
	loadCategory(output, "LINDA \"snarky\" PARIS", "https://truth.osto.space/roku.json?catName=linda-snarky-paris")
	loadCategory(output, "X22 REPORT", "https://truth.osto.space/roku.json?catName=x22-report")
	loadCategory(output, "WE THE PEOPLE (the situation)", "https://truth.osto.space/roku.json?catName=we-the-people-the-situtation-")
	loadCategory(output, "SANTA SURFING", "https://truth.osto.space/roku.json?catName=santa-surfing")
	loadCategory(output, "MITCHELL NICHOLAS GERBER", "https://truth.osto.space/roku.json?catName=mitchell-nicholas-gerber")
	loadCategory(output, "MELK", "https://truth.osto.space/roku.json?catName=melk")
	loadCategory(output, "MARTIN GEDDES", "https://truth.osto.space/roku.json?catName=martin-geddes")
	loadCategory(output, "THE FULFORD REPORT", "https://truth.osto.space/roku.json?catName=the-fulford-report")
	loadCategory(output, "STEW PETERS", "https://truth.osto.space/roku.json?catName=stew-peters")
	loadCategory(output, "SIMON PARKES", "https://truth.osto.space/roku.json?catName=simon-parkes")
	loadCategory(output, "RYUSHIN MALONE", "https://truth.osto.space/roku.json?catName=ryushin-malone")
	loadCategory(output, "KERRY CASSIDY", "https://truth.osto.space/roku.json?catName=kerry-cassidy")
	loadCategory(output, "JEAN WARDS MARS ANOMALY", "https://truth.osto.space/roku.json?catName=jean-wards-mars-anomaly")
	loadCategory(output, "COREYS DIGS", "https://truth.osto.space/roku.json?catName=coreys-digs")
	loadCategory(output, "COREY GOODE", "https://truth.osto.space/roku.json?catName=corey-goode")
	loadCategory(output, "\"THE SALLA\"", "https://truth.osto.space/roku.json?catName=-the-salla-")
	loadCategory(output, "CONSPIRACY FACT", "https://truth.osto.space/roku.json?catName=conspiracy-fact")
	loadCategory(output, "INTERNATIONAL TRUTH HEROES", "https://truth.osto.space/roku.json?catName=international-truth-hero-s")
	loadCategory(output, "NEW DIGITAL SOLDIERS", "https://truth.osto.space/roku.json?catName=new-digital-soldiers")
	loadCategory(output, "Lynn Miller -Intuitive Empath", "https://truth.osto.space/roku.json?catName=lynn-miller-intuitive-empath")
	loadCategory(output, "KNOWLEDGE OF THE FOREVER TIME", "https://truth.osto.space/roku.json?catName=knowledge-of-the-forever-time")
	loadCategory(output, "OSTO PAGES", "https://truth.osto.space/roku.json?catName=osto-pages")
	loadCategory(output, "STRANGERS IN YOUR OWN LAND", "https://truth.osto.space/roku.json?catName=-strangers-in-your-own-land")
	loadCategory(output, "DISCLOSURE SONGS", "https://truth.osto.space/roku.json?catName=disclosure-songs")
	loadCategory(output, "THE SCREAMING MEMER", "https://truth.osto.space/roku.json?catName=the-screaming-memer")

	writeOutput(output, "osto.json")

# Do it. Build the channel.
buildOSTO()