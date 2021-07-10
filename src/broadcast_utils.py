from utils import colored, clear, files_in_folder


def get_scrapped_files(results_path):
    print(colored(239, 245, 66,
                  '\n-------------------------\nSelect from scrapped list\n-------------------------\n'))
    files = files_in_folder(results_path)

    for x in range(len(files)):
        print(f'[{x + 1}] {files[x]}')

    file_index = int(input('\nPlease select a list to be proceed : ')) - 1

    if(file_index >= 0 or file_index < len(files)):
        return results_path + '/' + files[file_index]
    else:
        clear()
        get_scrapped_files()


def get_message_list(message_path):
    print(colored(239, 245, 66,
                  '\n-------------------------\nSelect a preset message\n-------------------------\n'))
    files = files_in_folder(message_path)

    for x in range(len(files)):
        print(f'[{x + 1}] {str(files[x])}')

    file_index = int(input('Please select a message to be sent : ')) - 1

    if(file_index >= 0 or file_index < len(files)):
        return message_path + '/' + files[file_index]
    else:
        clear()
        get_message_list()
