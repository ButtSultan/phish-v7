import telebot

# --- CONFIG ---
TOKEN = '8085353942:AAH-r1yJqPGNvPruBICBW4aFAh2IPJjy_Qw'
ADMIN_ID = '6671784926'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_cmd(message):
    if str(message.chat.id) == ADMIN_ID:
        bot.send_message(message.chat.id, "<b>🔥 v17.0 GLOBAL-OVERLORD ACTIVE</b>\n\n🛡️ Status: <b>Bridged via Google</b>", parse_mode='HTML')

if __name__ == "__main__":
    # IMPORTANT: Use a VPN on your phone for this part!
    print("Connecting to Telegram...")
    bot.polling(none_stop=True)

