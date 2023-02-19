from bs4 import BeautifulSoup
import requests

for sayfa in range(1,11): #vatanbilgisayarda 10 sayfa telefon modeli oldugu ıcın hepsini görmek adına:
    link="https://www.vatanbilgisayar.com/cep-telefonu-modelleri/?page={}".format(sayfa)

    parser=BeautifulSoup(requests.get(link).content,"html.parser")

    veri=parser.find("div",{"class":"wrapper-product wrapper-product--list-page clearfix"})\
    .find_all("div",{"class":"product-list product-list--list-page"})

    for i in veri:
        name=i.find("div",{"class":"product-list__content"}).find("a",{"class":"product-list__link"})\
        .find("div",{"class":"product-list__product-name"}).find("h3").string 

        #fiyatlarıda cekıyoruz
        fiyat=i.find("div",{"class":"product-list__content"}).find("div",{"class":"product-list__cost"})\
        .find("span",{"class":"product-list__price"}).string
        print("Model: {}\nFiyatı:{}.90 TL\n\n".format(name,fiyat))
