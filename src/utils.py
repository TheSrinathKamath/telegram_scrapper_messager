from os import system, name, makedirs, chdir, listdir
from logger import log_error


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def get_menu_choice(menu, menu_name, is_logged_in=False):
    print(colored(66, 215, 245, f'\n---------\n{menu_name}\n---------\n'))
    for item in range(len(menu)):
        print(f'[{item + 1}] {menu[item]}')

    if(is_logged_in):
        print(f'[0] Log out')
    else:
        print(f'[0] Exit')
    return int(input('Enter choice: '))


def files_in_folder(file_path):
    try:
        arr = listdir(file_path)
    except Exception as err:
        print(err)
        log_error(err)
        arr = []
    return arr
