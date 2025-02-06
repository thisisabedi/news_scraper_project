import logging
from src.scraper import scrape_news
from src.process import save_to_csv
from src.utils import setup_logging

OUTPUT_FILE = "./output/news_data.csv"

def main():
    """Run the news scraping project."""
    setup_logging()
    logging.info("Starting news scraping project")

    news_sources = [
        "https://cnn.com/"
    ]

    all_articles = []
    for source in news_sources:
        try:
            articles = scrape_news(source)
            all_articles.extend(articles)
        except Exception as e:
            logging.error(f"Error scraping {source}: {e}")

    logging.info(f"Total articles scraped: {len(all_articles)}")
    save_to_csv(all_articles, OUTPUT_FILE)

if __name__ == "__main__":
    main()
