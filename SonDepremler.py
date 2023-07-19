import requests
from bs4 import BeautifulSoup

url = "https://hasanadiguzel.com.tr/api/sondepremler"

response = requests.get(url)
içerik = response.content

soup =  BeautifulSoup(içerik,"html.parser")

json = response.json()

print("{:<12} {:<14} {:<38} {:<12} {:<12}".format("Tarih", "Saat", "Bölge", "Büyüklük", "Derinlik"))


for i in json["data"]:
    if i["ml"]>3:
        print("{:<12} {:<14} {:<38} {:<12} {:<12}".format(i["tarih"],i["saat"],i["yer"],i["ml"],i["derinlik_km"]))


