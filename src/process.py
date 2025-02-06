import pandas as pd
import logging

logger = logging.getLogger(__name__)

def save_to_csv(data, output_path):
    """
    Save the scraped news data to a CSV file.

    Args:
        data (list[dict]): List of extracted news articles.
        output_path (str): Path to save the CSV file.
    """
    if not data:
        logger.warning("No data to save. CSV will be empty.")
        return

    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    logger.info(f"Saved {len(df)} articles to {output_path}")
