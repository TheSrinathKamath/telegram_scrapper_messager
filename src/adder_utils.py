
from utils import clear, colored, files_in_folder


def filter_scrapped_results(users):
    print(colored(235, 52, 235, f'\nThere are {len(users)} results!\n'))
    start = int(input('Enter start index : '))
    offset = int(input('No. of records to read at a time : '))

    if(start+offset > len(users)):
        print(colored(245, 56, 56,
                      'Offset exceeds the number of records. Re-enter offset:'))
        filter_scrapped_results(users)
    filtered_users = users[start:(start+offset)]

    return filtered_users


def set_delay():
    time_delay = int(input('Enter time delay (in seconds) : '))

    if(time_delay <= 0):
        print(colored(245, 56, 56, 'Delay must be greater than 0 seconds!'))
        set_delay()

    return time_delay


def get_scrapped_files(results_path):
    print(colored(239, 245, 66,
                  '\n-------------------------\nSelect from scrapped list\n-------------------------\n'))
    files = files_in_folder(results_path)
    print(files)
    for x in range(len(files)):
        print(f'[{x + 1}] {files[x]}')

    file_index = int(input('\nPlease select a list to be proceed : ')) - 1

    if(file_index >= 0 or file_index < len(files)):
        return results_path + '/' + files[file_index]
    else:
        clear()
        get_scrapped_files()
