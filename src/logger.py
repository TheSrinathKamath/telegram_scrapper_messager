import time
from csv import DictWriter


def log_error(err, fn):
    error = {'Error': err, 'ErrFn': fn, 'Time': time.strftime(
        "%a, %d %b %Y %H:%M:%S")}
    field_names = ['Error', 'ErrFn', 'Time']
    try:
        with open("../logs/errors.csv", "a") as log_file:
            error_data = DictWriter(log_file, fieldnames=field_names)
            error_data.writerow(error)
        log_file.close()
    except:
        print('Oops, an error occured.')
