from pyrogram import Client, filters
import os

api_id = int(os.getenv("23699522"))
api_hash = os.getenv("399ecb6b9f12118466dba00efd6e5fac")
bot_token = os.getenv("8720044154:AAHFvpAjPFNPE23DlEHm2Xci8n9vfQf_OQ0")

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.text & filters.private)
async def reply(client, message):
    await message.reply("Bot chal raha hai 🚀 - Udaipur se!")

print("Bot starting...")
app.run()
