  #"Kinopoisk Movie Ratings Web Scraper"

#This Python script is designed to retrieve the movie rating information from the Kinopoisk website (a popular Russian movie database) based on user input.

#The key features of this project include:

#1. User Input: The script prompts the user to enter a search term, which is then used to construct the URL for the Kinopoisk search results page.

#2. Web Scraping: The script uses the requests library to fetch the HTML content of the search results page and the BeautifulSoup library to parse the HTML and locate the specific elements containing the movie rating information.

#3. Rating Extraction: The script searches for all div elements with the class "rating" on the search results page, and extracts the text content of the first matching element, which is assumed to be the movie rating.

#4. Rating Display: The extracted movie rating is then printed to the console.

import requests
from bs4 import BeautifulSoup

url_base = 'https://www.kinopoisk.ru/index.php?kp_query='
search_term = input("Enter a search term for Kinopoisk: ")
url = url_base + search_term

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find div elements with class "rating"
rating_divs = soup.find_all('div', {'class': 'rating'})

for i in rating_divs:
    movie_rating = i.get_text()
    print(f"Movie rating: ", movie_rating)
    break
