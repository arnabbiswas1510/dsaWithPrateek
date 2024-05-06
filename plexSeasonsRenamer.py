#!/usr/bin/env python3
#####################################################################
# Plex custom season title script
# Updates season title from season directory name
#####################################################################
# Name your season directory normally but add a dash and put 
# the season title after it. Plex will still recognize the directory 
# as a season directory and import the files properly. This script will 
# read the title from the directory name and update the season title 
# in the UI
#
# Example:
#   Season directory named "season 1 - My New Season Name"
#   will set the season title in the UI to: "My New Season Name" 
#
#####################################################################
 
import re
import sys
import os
 
TARGET_SERIES = "Udacity Data Structures and Algorithms Nanodegree Nd256 V2 0 0"
TARGET_LIBRARY = "Tech Courses"
 
if len(sys.argv) > 1:
    TARGET_SERIES=sys.argv[1]
 
USERNAME="arnabbiswas@yahoo.com"
PASSWORD="Paromita2478!"
SERVERNAME="rpi"
 
from plexapi.myplex import MyPlexAccount
account = MyPlexAccount(USERNAME, PASSWORD)
# returns a PlexServer instance
plex = account.resource(SERVERNAME).connect()  
 
episodes = plex.library.section(TARGET_LIBRARY).get(TARGET_SERIES).episodes()
print("Found %d episodes for: %s" % (len(episodes), TARGET_SERIES))
 
seasons_processed = []
 
for episode in episodes:
    if episode.seasonNumber in seasons_processed:
        continue    
    filepath = episode.media[0].parts[0].file
    matchstr = "^[Ss]eason"
    season_title = None
 
    # Search filepath for season directory
    for node in filepath.split("/"):
        result = re.findall(matchstr, node) 
        # Parse out title
        if len(result) > 0:
            try:
                season_title = node.split("_-_")[1].strip() #Use a fancy separator here!!!
            except IndexError:
                pass
            break
    if season_title is None:
        continue
 
    # Update plex
    
    # Updates title to "Season # - My New Season Name"
    # new_title = "Season %d - %s" % (episode.seasonNumber, season_title)
 
    # Updates title to "My New Season Name"
    new_title = season_title
 
    dict_param = {"title.value": new_title}
    episode.season().edit(**dict_param)
    seasons_processed.append(episode.seasonNumber)
    print("Season %d title updated to: %s" % (episode.seasonNumber, new_title))
 
