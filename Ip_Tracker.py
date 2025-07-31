#!/usr/bin/env python3
# হাই কাকু কোড কি চুরি করতে আইছো 
#ওকে চুরি করো কিন্তু ধরা পরলে কিন্তু
#টুনটুনি কেটে দিবো ওক

import requests
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("\033[1;95m" + "=" * 44)
    print("🔍 IP Tracker Tool")
    print("👤 Founder: Mr Shakil Jack")
    print("📚 Educational Purpose Only")
    print("⚠️  Illegal Use is Prohibited")
    print("=" * 44 + "\033[0m")

def get_info(ip=""):
    try:
        url = f"http://ip-api.com/json/{ip}?fields=66846719"
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'success':
            title = "📌 Your IP Info:" if ip == "" else f"📌 Info for {ip}:"
            print(f"\n\033[1;94m{title}\033[0m\n")

            fields = [
                ('IP Address', 'query'),
                ('Country', 'country'),
                ('Region', 'regionName'),
                ('City', 'city'),
                ('ZIP', 'zip'),
                ('Timezone', 'timezone'),
                ('ISP', 'isp'),
                ('Organization', 'org'),
                ('AS', 'as'),
                ('Latitude', 'lat'),
                ('Longitude', 'lon')
            ]

            for label, key in fields:
                value = data.get(key, 'N/A')
                print(f"\033[1;92m{label:<12}:\033[0m {value}")
                time.sleep(0.05)

            lat = data.get("lat")
            lon = data.get("lon")
            if lat and lon:
                maps_link = f"https://www.google.com/maps?q={lat},{lon}"
                print(f"\n\033[1;93m🌍 Google Maps:\033[0m {maps_link}")
        else:
            print("\033[1;91m[✘] Invalid IP Address or Not Found!\033[0m")
    except Exception as e:
        print(f"\033[1;91m[✘] Error: {e}\033[0m")

if __name__ == "__main__":
    clear_screen()
    banner()
    ip = input("\n\033[1;96m[?] Enter IP (Leave blank for your IP): \033[0m").strip()
    print("\n\033[1;93m[⏳] Fetching Info...\033[0m\n")
    time.sleep(1)
    get_info(ip)
