#!/bin/env python3
from enum import Enum

class UserType(Enum):
    STEAM = 1
    AOE2NET = 2
    STRING = 3

import json

users_filename = "users.json"

def read_users():
    with open(users_filename, "r") as users_file:
        users = json.load(users_file)

    return users
    


def write_user(user_id, id_type, discord_id):
    """Pass user_id as int, id_type should be one of the UserType members, and discord_id. Writes users to users_filename as json"""
    # We will save users as list of dicts
    user_list = []

    existing_user = check_if_user_exists(user_id, user_list=user_list)

    if existing_user == None:
        user_dict = {}
        user_dict["id"] = user_id
        user_dict["id_type"] = id_type
        user_dict["discord_id"] = discord_id
        
        user_list.append(user_dict)

        with open(users_filename) as users_file:
            json.dump(user_list, users_file)

    else:
        existing_user["id"] = user_id
        existing_user["id_type"] = id_type
        existing_user["discord_id"] = discord_id

        with open(users_filename) as users_file:
            json.dump(user_list, users_file)




def check_if_user_exists(new_user, user_list = None):
    users = read_users()

    for user in users:
        if new_user["id"] == user["id"]:
            return user

    return None

if __name__ == "__main__":
    print(read_users())
