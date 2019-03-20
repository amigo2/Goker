from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup




#my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20cards'
#ideal_url = 'https://www.idealista.com/venta-viviendas/sevilla/macarena/parlamento-torneo/'
foto_url = 'https://www.fotocasa.es/es/comprar/viviendas/sevilla-provincia/sevilla-capital-y-entorno/l?latitude=37.3928&longitude=-5.9858&combinedLocationIds=724,1,41,328,0,0,0,0,0'
uClient = uReq(foto_url)
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, "html.parser")

containers = page_soup.find_all("div", {"class":"item-container"})

#page_soup.findAll("div",{"class":"re-Searchresult-itemRow"})

for container in containers:

            title                 = container.div.div.h3["title"]
            title_property        = title.text

            price_container       = container.findAll("span",{"class":"re-Card-price"})
            price_property        = price_container[0].text

            feature_container     = container.findAll("span",{"class":"re-Card-feature"})
            rooms_feature         = feature_container[0].text
            size_feature          = feature_container[1].text

            description_container = container.find("span",{"class":"re-Card-description"})
            description_property  = description_container.text

            contact_container     = container.findAll("span",{"class":"sui-AtomButton-text"})
            contact_property      = contact_container[0].text


            print("title_property: "       + title_property)
            print("price_property: "       + price_property)
            print("rooms_feature: "        + rooms_feature)
            print("size_feature: "         + size_feature)
            print("description_property: " + description_property)
            print("contact_property: "     + contact_property)



