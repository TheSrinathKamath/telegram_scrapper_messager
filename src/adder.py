from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserNotMutualContactError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest

import time
import random
import traceback

from adder_utils import filter_scrapped_results, get_scrapped_files, set_delay
from logger import log_error
from scrapper_utils import read_scrapper_results
from utils import colored


def add_users_to_group(client):
    SLEEP_TIME_1 = 100
    SLEEP_TIME_2 = 100
    try:
        json_file_name = get_scrapped_files('../results')
    except Exception as e:
        print(e)
    # print(json_file_name)
    users = read_scrapper_results(json_file_name)
    users = filter_scrapped_results(users)
    # waiting_period = set_delay()
    PAUSE_TIME = int(input(
        'Add a pause time between 10 records to prevent ban (>=120s recommended): '))
    SELECTOR_MODE = int(
        input('Select Users by\n[1] ID\n[2] Username\n\nEnter choice: ')) - 1
    SELECTOR_CHOICES = ["id", "name"]
    SELECTOR = SELECTOR_CHOICES[SELECTOR_MODE]
    
    chats = []
    last_date = None
    chunk_size = 200
    groups = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.megagroup == True:
                groups.append(chat)
        except:
            continue

    print(colored(239, 245, 66,
                  '\n-----------------------------\nSelect a group to add members\n-----------------------------\n'))

    i = 0
    for group in groups:
        print(f'[{str(i)}] {group.title}')
        i += 1

    g_index = input("Enter your choice : ")
    target_group = groups[int(g_index)]

    target_group_entity = InputPeerChannel(
        target_group.id, target_group.access_hash)

    count = 0

    for user in users:
        count += 1
        if count % 80 == 0:
            print(f'Pausing the adder for {PAUSE_TIME} seconds')
            time.sleep(PAUSE_TIME)
        try:
            print(colored(
                245, 235, 56, "[+] Adding {}".format(user['name'])))
            # user_to_add = InputPeerUser(user['id'], user['access_hash'])
            if user['username'] == "":
                continue
            else:
                user_to_add = client.get_input_entity(user[SELECTOR])
                client(InviteToChannelRequest(
                    target_group_entity, [user_to_add]))
                print(f'Waiting for 60 - 90 Seconds...')
                time.sleep(random.randrange(60, 90))
        except PeerFloodError:
            print(colored(245, 56, 56,
                          "Getting Flood Error from telegram. Script is stopping now. Please try again after some time."))
            print("Waiting {} seconds".format(SLEEP_TIME_2))
            print(colored(245, 56, 56, 'Logout and signin again to resolve error.'))
            time.sleep(SLEEP_TIME_2)
        except UserPrivacyRestrictedError:
            print(colored(
                245, 56, 56, "\n\nThe user's privacy settings do not allow you to do this. Skipping."))
            print(colored(235, 52, 235, "\nWaiting for 5 Seconds..."))
            time.sleep(5)
        except UserNotMutualContactError as u_err:
            log_error(u_err, 'adder')
            print(colored(245, 56, 56, f'\n{u_err}\Skipping user. . .'))
        except Exception as err:
            log_error(err, 'adder')
            # traceback.print_exc()
            print(f'Error occured. Error : {err}')
            continue
