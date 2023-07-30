import requests
from bs4 import BeautifulSoup


def find_hyperlinked_tags_with_class_in_parent(url, parent_tag, parent_attrs, class_name):
    try:
        # Fetch the HTML content of the web page
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request fails
        html_content = response.text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the parent tag
        parent_tag = soup.find(parent_tag, attrs=parent_attrs)
        if not parent_tag:
            print(f"Parent tag not found.")
            return []

        # Find all hyperlinked tags with the given class within the parent tag
        all_tags = parent_tag.find_all('div', class_=class_name)
        sold_out_tags = parent_tag.find_all('div', class_="grid-view-item--sold-out")
        available_tags = [x for x in all_tags if x not in set(sold_out_tags)]

        links = [x.find("a", class_="grid-view-item__link grid-view-item__image-container full-width-link")["href"] for
                 x in available_tags]

        return ["https://petsyoga.com" + link for link in links]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


if __name__ == '__main__':
    url = "https://petsyoga.com/pages/book-tickets"
    parent_tag = 'div'  # Replace this with the desired parent tag (e.g., 'div', 'section', etc.)
    parent_attrs = {'class': 'custom-content'}  # Replace this with the attributes of the parent tag
    class_name = 'grid-view-item'  # Replace this with the desired class name
    links = find_hyperlinked_tags_with_class_in_parent(url, parent_tag, parent_attrs, class_name)
    print(links)
