import unittest
from src.scraper import scrape_news

class TestScraper(unittest.TestCase):
    def test_scrape_bbc(self):
        """Test scraping BBC News."""
        url = "https://www.bbc.com/news"
        articles = scrape_news(url)
        self.assertGreater(len(articles), 0, "No articles scraped from BBC")

    def test_invalid_url(self):
        """Test scraper with an invalid URL."""
        url = "https://invalid-url.com"
        articles = scrape_news(url)
        self.assertEqual(len(articles), 0, "Scraper should return empty list for invalid URL")

if __name__ == "__main__":
    unittest.main()
