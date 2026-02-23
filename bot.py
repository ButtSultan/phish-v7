import requests
import time

# --- PASTE NEW URL HERE ---
URL = "https://script.google.com/macros/s/AKfycbykb7gQF51Mlg1YZgQcSxlpQIHAkcKhF-nJ_-jyaR0ur-YY1KsLaoZltPF1IbnJNs0HXw/exec"
ADMIN = "6671784926"

def start_bot():
    print("🚀 Connecting via Omni-Bridge v22.0...")
    session = requests.Session()
    # Google uses redirects, so we must follow them
    session.max_redirects = 10 
    
    try:
        # Step 1: Check Connection
        r = session.get(URL, allow_redirects=True, timeout=20)
        
        # Check if the response is actually JSON
        if r.headers.get('content-type', '').startswith('application/json'):
            data = r.json()
            if data.get("ok"):
                bot_user = data['result']['username']
                print(f"✅ Gold Connection: @{bot_user} is ONLINE")
                
                # Step 2: Send Admin Alert
                payload = {"chat_id": ADMIN, "text": "<b>🔥 v22.0 OMNI-BRIDGE ONLINE</b>\n🛡️ Status: <i>Bridged via Google</i>", "parse_mode": "HTML"}
                session.post(URL, json=payload, allow_redirects=True)
                return True
        else:
            print("❌ Bridge Error: Google returned HTML. Check deployment settings!")
            
    except Exception as e:
        print(f"❌ Connection Error: {e}")
    return False

if __name__ == "__main__":
    if start_bot():
        print("Monitoring... (Ctrl+C to exit)")
        while True: time.sleep(60)

