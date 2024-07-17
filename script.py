import requests
from bs4 import BeautifulSoup
import pandas as pd


def fetch_page_content(url):
    """Fetches and returns the HTML content of the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_page_content(content):
    """Parses the HTML content of a page using BeautifulSoup."""
    soup = BeautifulSoup(content, "html.parser")
    title = soup.title.string if soup.title else "No Title"
    body_content = " ".join(p.get_text() for p in soup.find_all("p"))
    return title, body_content


def extract_links(soup):
    """Extracts the links from a BeautifulSoup object."""
    links = [a["href"] for a in soup.find_all("a", href=True)]
    return links


def crawl_website(url):
    """Crawls a website from a given URL and collects data."""
    visited = set()
    data = []
    counter = 0

    # Fetch content from the main page
    content = fetch_page_content(url)
    # If the content is None (Forbidden error like ksp.co.il), return the empty data -> empty excel file
    if content is None:
        return data

    # Parse the main page
    soup = BeautifulSoup(content, "html.parser")
    title, body_content = parse_page_content(content)
    data.append({"Page Title": title, "Page Url": url, "Page Content": body_content})

    # Extract links from the main page
    links = extract_links(soup)

    # Fetch content from the extracted links
    for link in links:
        full_link = requests.compat.urljoin(url, link)
        if full_link not in visited and counter < 10 and full_link != url:
            content = fetch_page_content(full_link)
            if content is None:
                continue
            title, body_content = parse_page_content(content)
            data.append(
                {
                    "Page Title": title,
                    "Page Url": full_link,
                    "Page Content": body_content,
                }
            )
            counter += 1
            visited.add(full_link)

    return data


def save_data_to_excel(data, filename="web_crawl_data.xlsx"):
    """Saves the collected data to an Excel file."""
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Data has been saved to {filename}")


def main():
    """The main entry point of the script."""
    print('Starting web crawling...')
    base_url = "https://www.yahoo.com/"  # הכנס כאן את הכתובת הרצויה
    # base_url = "https://www.ksp.co.il/"  # הכנס כאן את הכתובת הרצויה
    extracted_data = crawl_website(base_url)
    save_data_to_excel(extracted_data)


if __name__ == "__main__":
    main()
