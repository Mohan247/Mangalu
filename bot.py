import asyncio
import os
from pyrogram import Client, filters

# Env vars
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.text)
async def reply(client, message):  # async handler
    await message.reply("Bot chal raha hai 🚀 - Render pe live!")

async def main():
    await app.start()  # manual start
    print("Bot started! Press Ctrl+C to stop.")
    await asyncio.Event().wait()  # infinite run

if __name__ == "__main__":
    asyncio.run(main())
