import asyncio
import os
from pyrogram import Client, filters

print("🔥 Step 1: Starting...")

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

app = Client("mangalu_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.text)
async def reply(client, message):
    print(f"📱 Message from {message.from_user.first_name}")
    await message.reply("✅ Bot chal raha hai! Render live 🚀")

async def main():
    print("🔥 Step 2: Connecting...")
    await app.start()
    print("✅ Step 3: Bot LIVE!")
    
    # BETTER LOOP - No Event().wait()
    while True:
        await asyncio.sleep(30)  # 30 sec heartbeat
        print("❤️ Heartbeat OK")

if __name__ == "__main__":
    try:
        print("🚀 Final start...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("👋 Stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
