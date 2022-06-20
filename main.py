from pyrogram import Client, emoji, filters ,enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os

TARGET = 777000

session_string = os.environ.get('STRING_SESSION')

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
i_ds = os.environ.get('IDS')


app = Client("my_account",session_string=session_string, api_id=api_id, api_hash=api_hash)
ids = i_ds.split(",")

@app.on_message(filters.chat(TARGET))
async def welcome(client, message):
    msg = message.text
    for id in ids:
        await app.send_chat_action(id, enums.ChatAction.TYPING)
        await message.forward(id)


if __name__ == "__main__":
    print("I'm Working...")
    app.run()
