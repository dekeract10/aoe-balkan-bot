import requests
import json

req = requests.get("https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=3&steam_id=76561199003184910&count=1")

parsed_json = req.json()

print(parsed_json[0]['rating'])
