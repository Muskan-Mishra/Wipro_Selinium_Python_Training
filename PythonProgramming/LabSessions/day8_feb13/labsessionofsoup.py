#Scrape Product Details
import requests
from bs4 import BeautifulSoup

url = "https://scrapeme.live/shop/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    raise Exception("Failed to fetch page")

soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("li", class_="product")

for product in products:
    name = product.find("h2", class_="woocommerce-loop-product__title").text

    price = product.find("span", class_="woocommerce-Price-amount")
    price = price.text if price else "Not Available"

    rating = product.find("div", class_="star-rating")
    rating = rating.text.strip() if rating else "No Rating"

    availability = "In Stock"  # Most products show in stock by default

    print("Name:", name)
    print("Price:", price)
    print("Rating:", rating)
    print("Availability:", availability)
    print("-" * 40)
#Extract All Image URLs
images = soup.find_all("img")

for img in images:
    img_url = img.get("src")
    if img_url:
        print(img_url)
