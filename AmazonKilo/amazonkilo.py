from bs4 import BeautifulSoup as BS4
import requests
from AmazonKilo.data import Category, Product
from AmazonKilo.exception import ConnectionException, CategoryNotFound, WrongProductException

class AmazonKilo:
    URL_API = "https://www.amazon.com/"
    URL_category = URL_API + "s/ref=nb_sb_noss?url={}&field-keywords="

    def __init__(self, user_agent):
        self.user_agent = user_agent
        if not self.get_respond(self.URL_API):
            raise ConnectionException()

    def get_respond(self, URL):
        headers = {
            'authority': 'www.amazon.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': self.user_agent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        r = requests.get(URL, headers=headers)

        return r

    def get_categories(self):
        r = self.get_respond(self.URL_API)
        if not r.ok:
            raise ConnectionException(r)
        soup = BS4(r.text, "lxml")
        soups = soup.find("select", id="searchDropdownBox").find_all("option")
        categories = [(Category(k, v.get("value"), v.text)) for k, v in enumerate(soups)]
        if len(categories) == 0:
            raise CategoryNotFound
        return categories

    def get_product_detail_by_url(self, URL):
        r = self.get_respond(URL)
        if not r.ok:
            raise WrongProductException
        soup = BS4(r.text, "lxml")
        price = float(soup.find("span", id="priceblock_ourprice").text.split()[0].replace("$", ""))
        title = soup.find("span", id="productTitle").text.strip()
        rating = soup.find("span", class_="a-icon-alt").text.split()[0]+"/5"
        return Product(title, price, rating)