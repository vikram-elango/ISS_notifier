import requests
from datetime import *
import time
from smtplib import *
MY_LAT=120.433606
MY_LONG=11.872624
response=requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data=response.json()
# print(data)
# longitude=data["iss_position"]["longitude"]
# latitude=data["iss_position"]["latitude"]
# print(longitude,latitude)

my_email="abc@gmail.com"
my_password="xyz"



parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}

response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise=float(data["results"]["sunrise"].split('T')[1].split(':')[0])
sunset=float(data["results"]["sunset"].split('T')[1].split(':')[0])
print(sunrise,sunset)

today=datetime.now()
hour=float(today.hour)






iss_response=requests.get("http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
data_iss=iss_response.json()
iss_latitude=float(data_iss["iss_position"]["latitude"])
iss_longitude=float(data_iss["iss_position"]["longitude"])

print(MY_LONG-5,MY_LONG+5)
print(MY_LAT-5,MY_LAT+5)
while True:
    time.sleep(60)
    if MY_LONG-5 <= iss_longitude <= MY_LONG+5 and MY_LAT-5 <= iss_latitude <= MY_LAT+5 and sunset <= hour <= sunrise:
        with SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,to_addrs="xyz@yahoo.com",msg="Subject: INTERNATIONAL SPACE STATION \n\n"
                                                                                         "Hey Vikram, "
                                                                                         "The International Space Station is hovering above you!!!")




