#!/usr/bin/env python3
# হাই কাকু কোড কি চুরি করতে আইছো 
#ওকে চুরি করো কিন্তু ধরা পরলে কিন্তু
#টুনটুনি কেটে দিবো ওক
import os
import time
import requests
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print("\033[1;91m███╗░░░███╗██████╗░")
    print("████╗░████║██╔══██╗")
    print("██╔████╔██║██████╔╝")
    print("██║╚██╔╝██║██╔══██╗")
    print("██║░╚═╝░██║██║░░██║")
    print("╚═╝░░░░░╚═╝╚═╝░░╚═╝\n")
    print("\033[1;92................𝑺𝒉𝒂𝒌𝒊𝒍 𝑱𝒂𝒄𝒌")
    print("\033[1;95m██╗██████╗░")
    print("██║██╔══██╗")
    print("██║██████╔╝")
    print("██║██╔═══╝░")
    print("██║██║░░░░░")
    print("╚═╝╚═╝░░░░░\033[0m")

def get_info(ip=""):
    try:
        url = f"http://ip-api.com/json/{ip}?fields=66846719"
        res = requests.get(url)
        data = res.json()
        if data['status'] == 'success':
            print("\n\033[1;96m📌 IP Address Information:\033[0m\n")
            count = 1
            for key, value in data.items():
                print(f"\033[1;92m{count:02d}. {key:<18}:\033[0m {value}")
                count += 1
            
            lat = data.get("lat")
            lon = data.get("lon")
            if lat and lon:
                maps_link = f"https://www.google.com/maps?q={lat},{lon}"
                print(f"\n\033[1;93m🌍 Google Map Location:\033[0m {maps_link}")
        else:
            print("\033[1;91m[✘] Invalid IP Address or Not Found!")
    except Exception as e:
        print(f"\033[1;91m[✘] Error: {e}")

if __name__ == "__main__":
    clear_screen()
    banner()
    
    # Stylized input box
    print("\033[1;94m┌" + "─" * 36 + "┐")
    print("│  🔍 target your IP address:             │")
    print("└" + "─" * 36 + "┘")
    ip = input("\033[1;96m➤ Enter IP Here: \033[0m")

    print("\n\033[1;93m[!] Fetching Info...\033[0m\n")
    time.sleep(1)
    get_info(ip.strip())
