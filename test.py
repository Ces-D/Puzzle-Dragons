import re
from bs4 import BeautifulSoup
import requests

PAD_URL = "http://www.puzzledragonx.com/en/monster.asp?n=6479"

page = requests.get(PAD_URL)
soup = BeautifulSoup(page.text, "html.parser")

title = soup.title.text

print(title)