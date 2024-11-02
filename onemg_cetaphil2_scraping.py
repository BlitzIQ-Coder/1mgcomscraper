from bs4 import BeautifulSoup
import requests
import json

def cetaphil2():
    target_url = "https://www.1mg.com/categories/skin-care/cetaphil-524?filter=true&page=2"

    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "text",
        "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,en-IN;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }

    response = requests.get(target_url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    products = soup.find_all("div", class_="style__product-box___liepi")

    # List to hold all product details
    product_list = []

    for product in products:
        # Extracting product details
        try:
            name = product.find("div", {"class": "style__pro-title___2QwJy"}).text.strip()
            measurement = product.find("div", {"class": "style__pack-size___2JQG7"}).text.strip()
            rating = product.find("span", {"class": "CardRatingDetail__weight-700___27w9q"}).text.strip()
            views = product.find("span", {"class": "CardRatingDetail__ratings-header___2yyQW"}).text.replace("ratings", "").strip()
            price = product.find("div", {"class": "style__price-tag___cOxYc"}).text.strip()
            actual_price=price.replace("\u20b9","Rs.")
            link_suffix = product.a['href'].strip()
            link = f"https://www.1mg.com{link_suffix}"

            # Append to the list as a dictionary
            product_list.append({
                "name": name,
                "measurement": measurement,
                "rating": rating,
                "views": views,
                "price": actual_price,
                "link": link
            })
        except AttributeError:
            # Handle cases where some elements might not be found
            continue

    # Convert to JSON for better readability (optional)
    #print(json.dumps(product_list, indent=4))
    #print(f"Raw price: {price}")
    with open(r'ScrapedData\Cetaphilpage2_1mg.txt','w',encoding='utf-8') as sourcecode:
        sourcecode.write(json.dumps(product_list, indent=4))
    print("𝑭𝒊𝒍𝒆 𝑪𝒆𝒕𝒂𝒑𝒉𝒊𝒍𝒑𝒂𝒈𝒆2_1𝒎𝒈.𝒕𝒙𝒕 𝒄𝒓𝒆𝒂𝒕𝒆𝒅 𝒊𝒏 1𝒎𝒈𝒔𝒄𝒓𝒂𝒑𝒆𝒓 𝒇𝒐𝒍𝒅𝒆𝒓, 𝒄𝒉𝒆𝒄𝒌 𝒕𝒉𝒆 𝑺𝒄𝒓𝒂𝒑𝒆𝒅𝑫𝒂𝒕𝒂 𝒇𝒐𝒍𝒅𝒆𝒓")