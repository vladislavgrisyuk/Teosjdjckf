from telethon import TelegramClient, events
import re

# Your Telegram API credentials
api_id = '20173382'
api_hash = '7b900f720d7b0afa46360b6be1c7f44f'
phone_number = '+380633783368'

dst_chat_id = 7506910400  # Destination chat where you want to paste the message
# group_to_parse = [-1002186494712]
group_to_parse = [-1002186494712, -1002246276077]

# Connect to Telegram
client = TelegramClient('durovsinshalavi', api_id, api_hash)
should_fetch = True


@client.on(events.NewMessage(chats=group_to_parse))  # , from_users=[380472185]
async def copy_message(event):
    try:
        global should_fetch
        if should_fetch:
            await client.get_dialogs()
            should_fetch = False

        entity = await client.get_input_entity(dst_chat_id)

        await client.send_message(entity, event.message)
    except ValueError:
        try:
            await client.get_dialogs()
            entity = await client.get_input_entity(dst_chat_id)

            await client.send_message(entity, event.message)
        except Exception as e:
            print(f"Inner. An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Start the client
client.start(phone_number)

# Run the client's event loop
client.run_until_disconnected()
