from telethon.sync import TelegramClient
from datetime import datetime
from logger import log_error
from telegram_utils import display_apis
from utils import colored


async def main(client, api_id, phone):
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', f'OSM Scrapper\n----------\nAPI: {api_id}\nPhone: {phone}\nDate : {datetime.today().strftime("%Y-%m-%d")}')


def init_telegram_client(phone, api_id, api_hash):
    client = TelegramClient(phone, api_id, api_hash)
    try:
        with client:
            client.loop.run_until_complete(main(client, api_id, phone))
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            client.sign_in(phone, input('Enter verification code: '))
        return client
    except Exception as err:
        print(colored(245, 56, 56, 'Oops, error accessing with selected API. Try again!'))
        log_error(err, 'init_telegram_client')


def end_active_telegram_client(client):
    try:
        client.disconnect()
        client.log_out()
    except Exception as err:
        log_error(err, 'end_active_telegram_client')
