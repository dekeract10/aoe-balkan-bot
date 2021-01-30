#!/bin/env python3
import requests

def get_player():
    connection = http.client.HTTPSConnection('www.aoe2.net')
    odgovor = connection.request('GET', "/api/player/ratinghistory?game=aoe2de&steam_id=76561199003184910&count=5")


if __name__ == "__main__":
    pass
