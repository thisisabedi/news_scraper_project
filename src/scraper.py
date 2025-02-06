import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

def scrape_news(url):
    """Scrape news articles from the given website URL."""
    articles = []
    logger.info(f"Scraping news from {url}")

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code != 200:
        logger.error(f"Failed to fetch {url}: Status {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "lxml")

    #   BBC  & CNN
    if "bbc.com" in url:
        news_links = soup.select("div.gs-c-promo-body a.gs-c-promo-heading")
    elif "cnn.com" in url:
        news_links = soup.select("h3 a, div.card a")
    else:
        logger.warning(f"Website structure unknown for {url}")
        return []

    for link in news_links:
        title = link.get_text(strip=True)
        article_url = link.get("href")
        if not article_url.startswith("http"):
            article_url = url + article_url  

        articles.append({"title": title, "url": article_url})

    logger.info(f"Extracted {len(articles)} articles from {url}")
    return articles
