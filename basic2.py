import requests from bs4 
import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:
    title = book.h3.a.get("title")
    price = book.find("p", class_="price_color").get_text()
    rating = book.find("p", class_="star-rating")["class"][1]
    img = book.find("img")
    img_url = "http://books.toscrape.com/" + img["src"].replace("../", "")

    data.append([title, price, rating, img_url])

df = pd.DataFrame(data, columns=["Title", "Price", "Rating", "Image_URL"])
df.to_csv("books.csv", index=False)

print("Scraping Completed ✅")



