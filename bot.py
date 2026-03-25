from pyrogram import Client, filters

app = Client(
    "bot",
    api_id=23699522,
    api_hash="399ecb6b9f12118466dba00efd6e5fac",
    bot_token="8720044154:AAHFvpAjPFNPE23DlEHm2Xci8n9vfQf_OQ0"
)

@app.on_message(filters.text)
def reply(client, message):
    message.reply("Bot chal raha hai 🚀")

app.run()
