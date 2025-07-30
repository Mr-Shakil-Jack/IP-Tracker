#!/usr/bin/env python3
# হাই কাকু কোড কি চুরি করতে আইছো ওকে চুরি করো কিন্তু ধরা পরলে কিন্তু টুনটুনি কেটে দিবো ওকে 
import requests
import os
import time 

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print("\033[1;95m" + "═" * 60)
    print("║{:^58}║".format("Founder: Mr Shakil Jack"))
    print("║{:^58}║".format("This is an IP Tracker Tool"))
    print("║{:^58}║".format("Only for Educational Purpose"))
    print("║{:^58}║".format("Do not use it for any illegal activity"))
    print("═" * 60 + "\033[0m\n")
def get_info(ip=""):
    try:
        url = f"http://ip-api.com/json/{ip}?fields=66846719"
        res = requests.get(url)
        data = res.json()
        if data['status'] == 'success':
            print("\n\033[1;96m📌 IP Address Information:\033[0m\n")
            for key, value in data.items():
                print(f"\033[1;92m{key:<18}:\033[0m {value}")
            
            # Google Maps Link Box
            lat = data.get("lat")
            lon = data.get("lon")
            if lat and lon:
                maps_link = f"https://www.google.com/maps?q={lat},{lon}"
                print("\n\033[1;94m" + "═" * 60)
                print("║{:^58}║".format("🌍 Google Map Location"))
                print("╠" + "═" * 58 + "╣")
                print("║ {:<56} ║".format(maps_link))
                print("═" * 60 + "\033[0m")
        else:
            print("\033[1;91m[✘] Invalid IP Address or Not Found!")
    except Exception as e:
        print(f"\033[1;91m[✘] Error: {e}")

if __name__ == "__main__":
    clear_screen()
    banner()
    ip = input("\033[1;96m[?] Enter target IP address  ➤ \033[0m")
    print("\n\033[1;93m[!] Fetching Info...\033[0m\n")
    time.sleep(1)
    get_info(ip.strip())
