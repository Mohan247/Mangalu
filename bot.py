from pyrogram import Client, filters

# Apni values yahan dal do
api_id = 23699522        # apna api_id
api_hash = "399ecb6b9f12118466dba00efd6e5fac"
bot_token = "8720044154:AAHFvpAjPFNPE23DlEHm2Xci8n9vfQf_OQ0"

# Bot create
app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Simple message handler (sync)
@app.on_message(filters.text)
def reply(client, message):
    message.reply("Bot chal raha hai 🚀")

# Run bot (sync)
app.run()
