import itertools
import threading
import time
import sys
#from tkinter import *
from plyer import notification
import requests
#getting the ip using requests module
try:
    while True:
        response = requests.get("https://ipapi.co/json/")
        khach = response.json()
        #getting the lines out of response.text
        ip = khach['ip']
        version = khach['version']
        region = khach['region']
        country = khach['country_name']
        ISP = khach['org']
        if __name__=="__main__":
        
                notification.notify(
                    title = "IP INFO",
                    message="IP - "+ip+"\nVersion - "+version+"\nRegion - "+region+"\nCountry - "+country+"\nISP - "+ISP,
                    app_name = "IP Checker",
                    app_icon = "",
                    # displaying time
                    timeout=4
            )
        time.sleep(300)
except:
    if __name__=="__main__":
        
                notification.notify(
                    title = "IP INFO",
                    message="No internet connection",
                    app_name = "IP Checker",
                    app_icon = "",#if you want to set an icon type the image path here
                    # displaying time
                    timeout=4
            )


# {'ip': '106.204.198.125', 'version': 'IPv4', 'city': 'Chandigarh', 'region': 'Chandigarh', 'region_code': 'CH', 'country': 'IN', 'country_name': 'India', 'country_code': 'IN', 'country_code_iso3': 'IND', 'country_capital': 'New Delhi', 'country_tld': '.in', 'continent_code': 'AS', 'in_eu': False, 'postal': '160023', 'latitude': 30.7339, 'longitude': 76.7889, 'timezone': 'Asia/Kolkata', 'utc_offset': '+0530', 'country_calling_code': '+91', 'currency': 'INR', 'currency_name': 'Rupee', 'languages': 'en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc', 'country_area': 3287590.0, 'country_population': 1352617328, 'asn': 'AS45609', 'org': 'Bharti Airtel Ltd. AS for GPRS Service'}
