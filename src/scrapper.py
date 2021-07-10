from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from scrapper_utils import write_scrapped_list_to_json
from utils import clear, colored, get_menu_choice


def scrape(client):
    # Variable declarations
    chats = []
    last_date = None
    chunk_size = 200
    groups = []

    # Scrapped results
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
                  '\n-----------------------------\nSelect a group to be scrapped\n-----------------------------\n'))

    i = 0
    for g in groups:
        print(f'[{str(i)}] {g.title}')
        i += 1

    g_index = input("\nPlease enter your choice : ")
    target_group = groups[int(g_index)]
    print('Fetching Members. . .\n')
    all_participants = []
    all_participants = client.get_participants(target_group, aggressive=True)

    write_scrapped_list_to_json(
        target_group.title, all_participants, target_group)

    client.log_out()
    return [True, all_participants]
