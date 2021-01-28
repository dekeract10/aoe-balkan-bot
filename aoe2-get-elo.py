#!/bin/env python3
import requests
import steam.steamid

def get_elo(player_id, steam_id = True, leaderboard_id = 3):
    url = "https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=" + str(leaderboard_id) + "&count=1"

    if steam_id:
        url += "&steam_id=" + str(player_id)
    else:
        url += "&profile_id=" + str(player_id)

    req = requests.get(url)
    
    parsed_json = req.json()

    return parsed_json[0]['rating']

def assoc(url):
        ID = steam.steamid.from_url(url, http_timeout=30)
        if(ID):
            return ID
        else:
            ID = url.split('-')
            return(int(ID[1]))

if __name__ == "__main__":
    ID = assoc("https://aoe2.net/#profile-1509347")
    print(get_elo(ID, steam_id = False)) 

