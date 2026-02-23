import requests
import time

# --- CONFIG ---
URL = "https://script.google.com/macros/s/AKfycbxwolMlVYg8m1y8YXWeAZfoEVi00KBTTNljOZBiXd0pmsPoXis9-3psCoWbUgRlNPerdA/exec"
ADMIN = "6671784926"

def check():
    print("🚀 Connecting via Omni-Bridge...")
    s = requests.Session()
    try:
        # allow_redirects handles Google's macro jump
        r = s.get(URL, allow_redirects=True, timeout=20)
        if r.status_code == 200:
            data = r.json()
            if data.get("ok"):
                print(f"✅ Gold Connection: @{data['result']['username']} is ONLINE")
                s.post(URL, json={"chat_id":ADMIN, "text":"<b>🔥 v21.0 OMNI-BRIDGE ONLINE</b>", "parse_mode":"HTML"})
                return True
        print(f"❌ Error: {r.status_code}")
    except Exception as e:
        print(f"❌ Bridge Error: {e}")
    return False

if __name__ == "__main__":
    if check():
        print("Monitoring... (Ctrl+C to stop)")
        while True: time.sleep(60)
