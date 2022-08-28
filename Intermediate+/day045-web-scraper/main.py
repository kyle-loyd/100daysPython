from bs4 import BeautifulSoup
import requests as req

res = req.get("https://www.imdb.com/list/ls055592025/")

soup = BeautifulSoup(res.text, "html.parser")
movie_names_tags = soup.select("h3.lister-item-header a")
for i in range(0, 100):
    print(f"{i+1}. {movie_names_tags[i].getText()}")

