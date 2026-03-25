from pyrogram import Client, filters
import asyncio

api_id = 23699522
api_hash = "399ecb6b9f12118466dba00efd6e5fac"
bot_token = "8720044154:AAHFvpAjPFNPE23DlEHm2Xci8n9vfQf_OQ0"

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.text)
async def reply(client, message):
    await message.reply("Bot chal raha hai 🚀")

async def main():
    await app.start()
    print("Bot Started 🔥")
    await asyncio.Event().wait()

asyncio.run(main())
