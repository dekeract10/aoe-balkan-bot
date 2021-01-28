#!/bin/env python3
import requests

def get_elo(player_id, steam_id = True, leaderboard_id = 3):
    url = "https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=" + str(leaderboard_id) + "&count=1"

    if steam_id:
        url += "&steam_id=" + str(player_id)
    else:
        url += "&player_id=" + str(player_id)

    req = requests.get(url)
    parsed_json = req.json()

    print(parsed_json[0]['rating'])

if __name__ == "__main__":
    get_elo("76561199003184910") 
