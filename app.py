import requests

html = requests.get(
    "https://petsyoga.com/pages/book-tickets"
)

print(html.text)
