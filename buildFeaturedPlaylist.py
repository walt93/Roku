import RokuFunctions

def buildFeaturedPlaylist():
	output = createAntMediaPlaylist("24/7 loop")
	buildPlaylist(output, "https://conspyre.tv/roku.json?program_id=89632",	# videos
					  "https://adserver3.conspyre.tv/roku.json?program_id=129", # commercials
					  "https://adserver.conspyre.tv/roku.json?program_id=109", # bumpers
					  "https://adserver.conspyre.tv/roku.json?program_id=110" # memes)
	writeAntMediaJSON(output, "/var/www/html/AVideo/rokuv2/featured_antmedia.json")

# Do it. Build the playlist.
buildFeaturedPlaylist()

