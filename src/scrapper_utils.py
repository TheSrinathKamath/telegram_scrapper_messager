import json
from datetime import datetime

from utils import colored


def write_scrapped_list_to_json(file_name, all_participants, target_group):
    members_list = {}
    list_all = []

    for user in all_participants:
        members_list['user_id'] = user.id

        if user.username:
            members_list['username'] = user.username
        else:
            members_list['username'] = ""
        if user.first_name:
            members_list['first_name'] = user.first_name
        else:
            members_list['first_name'] = ""
        if user.last_name:
            members_list['last_name'] = user.last_name
        else:
            members_list['last_name'] = ""

        members_list['access_hash'] = user.access_hash
        members_list['target_group_title'] = target_group.title
        members_list['target_group_id'] = target_group.id
        list_all.append(members_list)
        members_list = {}

    folder = '../results'
    file_name = file_name.replace(" ", "_")

    with open(f'{folder}/{file_name}_-_{datetime.today().strftime("%Y-%m-%d")}.json', "w") as outfile:
        json.dump(list_all, outfile)
    outfile.close()
    print(colored(3, 252, 7, f'Saved as {file_name}_-_{datetime.today().strftime("%Y-%m-%d")}.json\n\n'))


def read_scrapper_results(file_name):
    file_path = file_name
    users = []

    with open(file_path, 'r') as f:  # Enter your file name
        json_object = json.load(f)
        for row in json_object:
            user = {}
            user['username'] = row.get('username') or ""
            user['id'] = row.get('user_id') or ""
            user['access_hash'] = row.get('access_hash') or ""
            user['name'] = row.get("first_name") + " " + row.get("last_name")
            users.append(user)

    return users
