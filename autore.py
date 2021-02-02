from telethon import TelegramClient
import asyncio
import time
from telethon import events

api_id = '2905565'
api_hash = '10e132995f08087650dccbf2614df267'

client = TelegramClient('lashdaysg', 2905565, 10e132995f08087650dccbf2614df267)

message = '💐Hi there! Thank you for your message.
❤️If you'd like to book an appointment, please go to https://lashdaysg.setmore.com for instant confirmation. (Price list is in there too)
👩‍🦱For enquiries/appointments, we will respond as soon as possible. Thank you!'

def main():

    client.start()

    @client.on(events.NewMessage(incoming=True))
    async def _(event):
        if event.is_private:
            time.sleep(1)  # pause for 1 second to rate-limit automatic replies
            await client.send_message(event.message.from_id, message)
    client.run_until_disconnected()


if __name__ == '__main__':
    main()
