import requests
from bs4 import BeautifulSoup


def fetch_palo_alto_advisories():
    url = 'https://securityadvisories.paloaltonetworks.com/'  # Example URL
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch advisories. Status code: {response.status_code}")
        return None


def parse_advisories(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Print the first 1000 characters to understand the structure
    print(soup.prettify())

    # Adjust selectors based on the actual page structure
    advisories = []
    for item in soup.select('.advisory-item'):  # Example selector
        title = item.select_one('.title').get_text(strip=True) if item.select_one('.title') else 'No title'
        date = item.select_one('.date').get_text(strip=True) if item.select_one('.date') else 'No date'
        link = item.select_one('a')['href'] if item.select_one('a') else 'No link'
        advisories.append({'title': title, 'date': date, 'link': link})

    return advisories


def main():
    html_content = fetch_palo_alto_advisories()

    if html_content:
        advisories = parse_advisories(html_content)
        if advisories:
            for advisory in advisories:
                print(f"Title: {advisory['title']}")
                print(f"Date: {advisory['date']}")
                print(f"Link: {advisory['link']}")
                print("")
        else:
            print("No advisories found.")
    else:
        print("Failed to retrieve content.")


if __name__ == '__main__':
    main()
