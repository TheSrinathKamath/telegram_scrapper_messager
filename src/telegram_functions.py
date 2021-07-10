from adder import add_users_to_group
from broadcast import send_message
from scrapper import scrape
from telegram import end_active_telegram_client
from utils import clear, colored, get_menu_choice

second_menu = [
    "Scrape members from group",
    "Add members to group",
    "Broadcast messages"
]


def telegram_functions(client):

    clear()
    print(colored(66, 215, 245,
                  '\n\x1B[3mThe Awesome Telegram Scrapper\x1B[0m\n'))
    print(colored(3, 252, 7, 'Status : Logged in'))
    while(True):
        fn_choice = get_menu_choice(second_menu, 'Functions menu', True)

        if(fn_choice == 0):
            end_active_telegram_client(client)
            break
        elif(fn_choice == 1):
            scrape(client)
        elif(fn_choice == 2):
            add_users_to_group(client)
        elif(fn_choice == 3):
            send_message(client)
        elif(fn_choice < 0 or fn_choice > 3):
            print('\nPlease enter a valid choice or 0 to logout!')
