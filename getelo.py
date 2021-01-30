#!/bin/env python3

import requests
import steam.steamid
import re
import dataio as io

def get_elo(player_id, steam_id, leaderboard_id = 3):
    url = "https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=" + str(leaderboard_id) + "&count=1"

    if steam_id:
        url += "&steam_id=" + str(player_id)
    else:
        url += "&profile_id=" + str(player_id)

    req = requests.get(url)

    parsed_json = req.json()
    return parsed_json[0]["rating"]

def get_id(url):
    # Check if our url is a correct 
    ID = steam.steamid.from_url(url, http_timeout=30)
    if(ID):
        return ID
    else:
        ID = url.split('-')
        return(int(ID[1]))

def validate_id(id_string):
    #
    steam_pattern = re.compile("https?://steamcommunity.com/(id|profile)/([^/]*)/?")
    aoe2net_pattern = re.compile("https?://aoe2.net/#profile-(\d+)/?")
    string_pattern = re.compile("[\w\d_-]{1,32}")
    ID = None
    id_type = None

    # Parse steam id
    if steam_pattern.match(id_string):
        steam_profile = steam.steamid.from_url(id_string, http_timeout=30)
        if steam_profile:
            ID = steam_profile.id
            id_type = io.UserType.STEAM
    # Parse aoe2.net id
    elif aoe2net_pattern.match(id_string):
        aux = aoe2net_pattern.match(id_string)

        ID = aux.groups()[0]
        url = "https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&start=1&count=1&profile_id=" + ID
        try:
            # ID can exceed largest int
            req = requests.get(url)
            user_aux = req.json()
            id_type = io.UserType.AOE2NET
        except:
            ID = None

        # if user_aux["count"] == 0:
            # ID = None
        # else:
    # If user just passed a string with his username
    elif string_pattern.match(id_string):
        url = "https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&start=1&count=5&search=" + id_string

        req = requests.get(url)
        user_aux = req.json()

        if user_aux["count"] == 1:
            ID = user_aux["leaderboard"][0]["profile_id"]
            id_type = io.UserType.AOE2NET


    return ID, id_type

if __name__ == "__main__":
    # validate_id("https://steamcommunity.com/id/dekeract/")
    # print(validate_id("https://steamcommunity.com/id/dekeract/"))
    print(validate_id("https://aoe2.net/#profile-50689812098371298379128371092837091237018937/"))
    # print(validate_id("dekeract"))


