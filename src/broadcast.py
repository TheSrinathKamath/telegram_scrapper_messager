from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
from adder_utils import filter_scrapped_results

from broadcast_utils import get_message_list, get_scrapped_files
from logger import log_error
from scrapper_utils import read_scrapper_results
from utils import colored
import time


def send_message(client):
    users = []

    SLEEP_TIME_2 = 100
    SLEEP_TIME_1 = 40
    SLEEP_TIME = 4

    try:
        scrapped_file = get_scrapped_files('../results')
    except Exception as e:
        print(e)

    users = read_scrapper_results(scrapped_file)
    users = filter_scrapped_results(users)
    # Enter you message here!
    message_file = get_message_list('../messages')

    PAUSE_TIME = int(input(
        'Add a pause time between 10 records to prevent ban (>=120s recommended): '))
    SELECTOR_MODE = int(
        input('Select Users by\n[1] ID\n[2] Username\n\nEnter choice: ')) - 1
    SELECTOR_CHOICES = ["id", "username"]
    SELECTOR = SELECTOR_CHOICES[SELECTOR_MODE]
    
    with open(message_file, 'r', encoding='utf-8') as mf:
        mf_data = mf.readlines()

    message = " ".join(mf_data)

    count = 0

    for user in users:
        # print(user['id'], user['access_hash'])
        receiver = InputPeerUser(user[SELECTOR], user['access_hash'])
        try:
            print(colored(253, 255, 201,
                          "\nSending Message to:"), user['name'])
            client.send_message(receiver, str(message))
            print(colored(232, 232, 232,
                          "Waiting {} seconds".format(SLEEP_TIME)))
            time.sleep(SLEEP_TIME)
            print(colored(3, 252, 7, f"Done. Message sent to {user['name']}"))
            count += 1
        except PeerFloodError:
            print(colored(245, 56, 56,
                          "Getting Flood Error from telegram. Script is stopping now. Please try again after some time."))
            log_error('Peer flood error', 'broadcaster')
            print("Waiting {} seconds".format(SLEEP_TIME_2))
            time.sleep(SLEEP_TIME_2)
        except Exception as e:
            log_error(e, 'broadcaster')
            print("Error:", e)
            print("Trying to continue...")
            print("Waiting {} seconds".format(SLEEP_TIME_1))
            time.sleep(SLEEP_TIME_1)

        if(count % 80 == 0):
            print(f'Pausing the broadcaster for {PAUSE_TIME} seconds')
            time.sleep(PAUSE_TIME)
