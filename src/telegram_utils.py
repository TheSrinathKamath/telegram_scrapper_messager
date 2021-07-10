from asyncio.windows_events import NULL
import json
from logger import log_error
from datetime import datetime

from utils import colored


def display_apis(api_list):
    print(colored(3, 252, 7, '\n--------------\nAvailable APIs\n--------------'))

    for index in range(len(api_list)):
        print(colored(235, 52, 214,
                      f'[ {index + 1} ] {api_list[index].get("api_id")}'))


def retrieve_api(list_index):
    try:
        with open("../apis/api.json", 'r') as api_file:
            auth_data = json.loads(api_file)
        api_file.close()
        return auth_data[list_index]
    except Exception as err:
        log_error(err, 'retrieve_api')


def add_api_json():
    try:
        api_dict = {}
        temp = []

        while(True):
            api_dict['api_id'] = input("Enter the API key : ")
            api_dict['api_hash'] = input("Enter the API Hash : ")
            api_dict['phone'] = input("Enter the Phone No. : ")
            api_dict['created_on'] = datetime.today().strftime("%Y-%m-%d")

            temp.append(api_dict)
            api_dict = {}
            choice = input('Enter more? (y/n)')

            if((choice != 'y')):
                with open('../apis/api.json', 'r+') as api_file:
                    auth_data = json.load(api_file)
                    auth_data = auth_data + temp
                    api_file.seek(0)
                    json.dump(auth_data, api_file, indent=4)
                api_file.close()
                break

    except Exception as err:
        log_error(err, 'add_api_json')


def read_api_json(auth_file_name):
    try:
        with open(auth_file_name, 'r') as api_file:
            apis = json.load(api_file)
        api_file.close()
        return apis
    except Exception as err:
        log_error(err, 'read_api_json')


def select_api(apis):
    print(colored(3, 252, 7, '\n--------------\nAvailable APIs\n--------------\n'))

    for index in range(len(apis)):
        print(
            colored(235, 52, 214,
                    f'[ {index + 1} ] {apis[index].get("api_id")}'))
    print('\n')
    choice = int(input('Enter choice: '))

    if(choice == 0):
        return {"status": False, "api": NULL}
    elif(choice < 0 or choice > len(apis)):
        print(colored(245, 56, 56, '\nPlease select a valid option!\n'))
        select_api(apis)
    else:
        return {"status": True, "api": apis[choice-1]}
