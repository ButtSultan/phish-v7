import requests
import time
import sys

# --- CONFIG ---
BRIDGE_URL = "https://script.google.com/macros/s/AKfycbzL_njCl5CDQidqHMb2LFt0AVqN6bz0ZOBZ5iMCq3WKofvvV0EunyGh0C1G18yAujH3mw/exec"
ADMIN_ID = "6671784926"

def check_connection():
    print("🚀 Bypassing ISP... Routing via Google...")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    try:
        # Use allow_redirects=True to handle Google's internal jumps
        response = requests.get(BRIDGE_URL, headers=headers, allow_redirects=True, timeout=20)
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("ok"):
                    bot_user = data['result']['username']
                    print(f"✅ Gold Connection: @{bot_user} is ONLINE")
                    return True
            except:
                print("❌ Bridge Error: Google returned HTML instead of JSON.")
                print("Tip: Go to Google Script -> Deploy -> New Deployment -> Access: ANYONE")
        else:
            print(f"❌ HTTP Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")
    return False

if __name__ == "__main__":
    if check_connection():
        print("Monitoring hits... (Press Ctrl+C to stop)")
        while True:
            try:
                time.sleep(60)
            except KeyboardInterrupt:
                sys.exit()
