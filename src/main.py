
from telegram import end_active_telegram_client, init_telegram_client
from sys import exit
from logger import log_error
from telegram_functions import telegram_functions
from telegram_utils import add_api_json, display_apis, read_api_json, retrieve_api, select_api
from utils import clear, colored, get_menu_choice

main_menu = [
    "View APIs",
    "Add APIs",
    "Login"
]

clear()
print(colored(66, 215, 245, '\n\x1B[3mThe Awesome Telegram Scrapper\x1B[0m\n'))
print(colored(245, 56, 56, 'Status : Not logged in'))

while (True):
    main_choice = get_menu_choice(main_menu, 'Main menu')

    if(main_choice == 0):
        exit()
    elif(main_choice == 1):
        apis = read_api_json('../apis/api.json')
        display_apis(apis)
    elif(main_choice == 2):
        add_api_json()
    elif(main_choice == 3):
        apis = read_api_json('../apis/api.json')
        api_dict = select_api(apis)

        if(api_dict.get('status')):
            api = api_dict.get('api')
            client = init_telegram_client(
                api.get('phone'), api.get('api_id'), api.get('api_hash'))
            telegram_functions(client)
        else:
            print(colored(245, 56, 56, 'No APIs added!'))
