pincodes = ['570022', '570021']
for_the_next_n_days = 100

from time import sleep
from datetime import datetime, timedelta, date
import os, requests
date_list = [date.today() + timedelta(days=x) for x in range(for_the_next_n_days)]
for i in pincodes:
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={i}&date="
    for j in range(for_the_next_n_days):
        print(requests.get(url + str(date_list[j].strftime("%d-%m-%Y"))).text)
        print(url + date_list[j].strftime("%d-%m-%Y"))
        sleep(0.5)

