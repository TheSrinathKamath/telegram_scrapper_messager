from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError

from broadcast_utils import get_message_list, get_scrapped_files
from scrapper_utils import read_scrapper_results
from utils import colored
import time

def send_message(client):
    users = []

    SLEEP_TIME_2 = 100
    SLEEP_TIME_1 = 40
    SLEEP_TIME = 4

    scrapped_file = get_scrapped_files('../results')
    users = read_scrapper_results(scrapped_file)

    # Enter you message here!
    message_file = get_message_list('../messages')
    
    with open(message_file, 'r') as mf:
        mf_data = mf.readlines()

    message = " ".join(mf_data)

    for user in users:
        receiver = InputPeerUser(user['id'], user['access_hash'])
        try:
            print(colored(253, 255, 201,
                                "\nSending Message to:"), user['name'])
            client.send_message(receiver, str(message))
            print(colored(232, 232, 232,
                                "Waiting {} seconds".format(SLEEP_TIME)))
            time.sleep(SLEEP_TIME)
            print(colored(3, 252, 7, "Done. Message sent to all users."))
        except PeerFloodError:
            print(
                "Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
            print("Waiting {} seconds".format(SLEEP_TIME_2))
            time.sleep(SLEEP_TIME_2)
        except Exception as e:
            print("Error:", e)
            print("Trying to continue...")
            print("Waiting {} seconds".format(SLEEP_TIME_1))
            time.sleep(SLEEP_TIME_1)
        finally:
            return True
