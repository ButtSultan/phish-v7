import requests, time

# PASTE THE NEW URL FROM STEP 4 HERE
URL = "https://script.google.com/macros/s/AKfycbykb7gQF51Mlg1YZgQcSxlpQIHAkcKhF-nJ_-jyaR0ur-YY1KsLaoZltPF1IbnJNs0HXw/exec"
ADMIN = "6671784926"

def check_bridge():
    print("🚀 Testing Omni-Bridge Connection...")
    try:
        # We use a GET request to test the 'doGet' function
        r = requests.get(URL, allow_redirects=True, timeout=20)
        
        if "<!DOCTYPE html>" in r.text or "login.google.com" in r.url:
            print("❌ ERROR: Google is still asking for LOGIN.")
            print("FIX: In Deployment, set 'Who has access' to 'ANYONE'.")
            return False
            
        print("✅ SUCCESS: Bridge is open to the public!")
        # Send a test message
        requests.post(URL, json={"chat_id": ADMIN, "text": "<b>🔥 OMNI-V25 LIVE</b>", "parse_mode": "HTML"})
        return True
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return False

if __name__ == "__main__":
    if check_bridge():
        print("Monitoring hits...")
        while True: time.sleep(60)

