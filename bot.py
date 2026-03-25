from pyrogram import Client, filters
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.text & filters.private)
async def reply(client, message):
    await message.reply("Bot chal raha hai 🚀 - Udaipur se!")

print("Bot starting...")
app.run()
