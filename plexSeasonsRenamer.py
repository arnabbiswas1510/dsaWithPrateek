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
# Precondition: You will need to cd to the season folder and run the following command:
# rename 's/^/S_-_/' *
# Replace TARGET_SERIES (line 24) with the exact name of series (TV Show) from Plex Client
# Updated to also add episode titles. For this to work ensure all episodes start with S1E1- format.
# The - is critical after the episode number
#####################################################################
 
import re
import sys
 
TARGET_SERIES = "NeetCode Advanced Algorithms"
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
    # if episode.seasonNumber in seasons_processed:
    #     continue
    filepath = episode.media[0].parts[0].file
    matchstr = "^S_-_"
    matchstr2 = r"S\d+E\d+\s*-\s*"
    season_title = None
    episode_title = None

    # Search filepath for season directory
    for node in filepath.split("/"):
        result = re.findall(matchstr, node) 
        result2 = re.findall(matchstr2, node)
        # Parse out title
        if len(result)> 0:
            try:
                season_title = node.split("_-_")[1].strip() #Use a fancy separator here!!!
            except IndexError:
                pass
        if len(result2)> 0:
            try:
                episode_title = re.split(matchstr2, node)[1].strip()
            except IndexError:
                pass
    # if season_title is None and episode_title is None:
    #     continue
 
    # Update plex
    
    # Updates title to "Season # - My New Season Name"
    # new_title = "Season %d - %s" % (episode.seasonNumber, season_title)
 
    # Updates title to "My New Season Name"
        if season_title is not None:
            dict_param = {"title.value": season_title}
            episode.season().edit(**dict_param)
            print("Season %d title updated to: %s" % (episode.seasonNumber, season_title))

        if episode_title is not None:
            dict_param = {"title.value": episode_title}
            episode.edit(**dict_param)
            print("Episode title updated to: %s" % (episode_title))

    # seasons_processed.append(episode.seasonNumber)
