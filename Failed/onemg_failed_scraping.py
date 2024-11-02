# import requests
# from bs4 import BeautifulSoup as bs

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
# }

# params = {
#     'filter': 'true',
#     'page': '1',
# }
# url = 'https://www.1mg.com/categories/skin-care/cetaphil-524'
# response = requests.get(url, params=params, headers=headers)

# soup = bs(response.text,"html.parser")
# print(soup)

from bs4 import BeautifulSoup
import requests
import json

target_url="https://www.1mg.com/categories/skin-care/cetaphil-524?filter=true&page=1"


HEADERS={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding":"text", 
    "Accept-Language":"en-GB,en;q=0.9,en-US;q=0.8,en-IN;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}
response=requests.get(target_url,headers=HEADERS)
soup=BeautifulSoup(response.content,"html.parser")
main=soup.find_all("div",class_="style__product-box___liepi")

names = soup.find("div",{"class":"style__pro-title___2QwJy"}).text
measurement=soup.find("div",{"class":"style__pack-size___2JQG7"}).text
rating=soup.find("span",{"class":"CardRatingDetail__weight-700___27w9q"}).text
views=soup.find("span",{"class":"CardRatingDetail__ratings-header___2yyQW"}).text.replace("ratings","")
price=soup.find("div",{"class":"style__price-tag___cOxYc"}).text
link2=soup.find("div",{"class":"style__product-box___liepi"}).a['href']
link1="https://www.1mg.com"
totallink=link1+link2
print(price)

''' test 2
for index,meds in enumerate(main):
    print(f"meds {index+1}")
    result = {}
    result["product name"] = (
        meds.find("div", class_="style__pro-title___2QwJy")
        #.text.replace("(More medss)", "")
        .text.strip()
    )
    result["measurement"] = (
        meds.find("div", class_="style__pack-size___2JQG7")
        #.text.replace("(More medss)", "")
        .text.strip()
    )
    result["rating"] = (
        meds.find("span", class_="CardRatingDetail__weight-700___27w9q")
        #.text.replace("(More medss)", "")
        
    ) 
    result["views"] = (
        meds.find("span", class_="CardRatingDetail__ratings-header___2yyQW")
        .text.replace("ratings", "").strip()
    )
    result["price"] = (
        meds.find("div", class_="style__price-tag___cOxYc")
        .text.strip()
    )
    base_url="https://www.1mg.com"
    
    #result["link"] = (base_url+
    #    meds.find("div", class_="style__product-box___liepi")
    #    .a['href'].strip()
    #)
    
    #result["link"] = base_url+meds.find("div",class_="style__product-box___liepi").a['href']
    
    print(json.dumps(result, indent=2))
    print()
'''
