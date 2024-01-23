print("""\033[31m

 ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░
  ░░   ░    ░    ░ ░  ░      ░         ░    ░   ▒   ░      ░   
   ░        ░  ░   ░                   ░  ░     ░  ░       ░   
                 ░                                             
      """)
import time
import os
time.sleep(2)
os.system("pip install requests")
os.system("pip install json")
os.system("pip install getmac")
import requests
import json
import getmac
os.system("clear")
print("""\033[31m
 ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░
  ░░   ░    ░    ░ ░  ░      ░         ░    ░   ▒   ░      ░   
   ░        ░  ░   ░                   ░  ░     ░  ░       ░   
                 ░                    
""")


class IPQuery:
    def __init__(self, ip):
        self.ip = ip
        self.ipapi_url = f"https://ipapi.co/{ip}/json/"
        self.ipinfo_url = f"https://ipinfo.io/{ip}/json"

    def make_request(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            return None
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            return None
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            return None
        except requests.exceptions.RequestException as err:
            print(f"Oops, Something went wrong... {err}")
            return None

    def get_ipapi_info(self):
        ipapi_data = self.make_request(self.ipapi_url)
        return ipapi_data

    def get_ipinfo_info(self):
        ipinfo_data = self.make_request(self.ipinfo_url)
        return ipinfo_data

    def get_mac_address(self):
        mac_address = getmac.get_mac_address(ip=self.ip)
        return mac_address

    def perform_query(self):
        ipapi_info = self.get_ipapi_info()
        ipinfo_info = self.get_ipinfo_info()
        mac_address = self.get_mac_address()

        return {
            "ipapi_info": ipapi_info,
            "ipinfo_info": ipinfo_info,
            "mac_address": mac_address
        }

if __name__ == "__main__":
    # Kullanıcıdan IP adresi girmesini iste
    ip = input("Lütfen bir IP adresi girin: ")

    # IP sorgusu yap
    ip_query = IPQuery(ip)
    query_result = ip_query.perform_query()

    # Sonuçları yazdır
    if query_result["ipapi_info"] and query_result["ipinfo_info"]:
        print("ipapi.co Bilgileri:")
        print(json.dumps(query_result["ipapi_info"], indent=2))

        print("\nipinfo.io Bilgileri:")
        print(json.dumps(query_result["ipinfo_info"], indent=2))

        print("\033[33m\nMAC Adresi:")
        print(query_result["mac_address"])
    else:
        print("IP sorgusu başarısız oldu. Lütfen geçerli bir IP adresi girin.")
