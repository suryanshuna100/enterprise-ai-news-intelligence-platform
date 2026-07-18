"""
Enterprise AI News Intelligence Platform

Module:
    GDELT Data Extraction

Purpose:
    Download raw GDELT datasets and prepare them for ingestion into the Bronze layer.

Status:
    Day 3 - GDELT Dataset Extraction
"""

import logging
from pathlib import Path

import requests

from eanip.ingestion.config import (
    LAST_UPDATE_URL,
    REQUEST_TIMEOUT,
    USER_AGENT,
)

logger = logging.getLogger(__name__)



def get_latest_dataset_url() -> str:
    """
    Retrieves the latest available GDELT dataset URL.

    Returns
    -------
    str
        Direct download URL of the latest GDELT dataset.

    Raises
    ------
    requests.HTTPError
        If the HTTP request fails.

    ValueError
        If the response format is invalid.
    """

    logger.info("Requesting latest GDELT update information...")

    headers = {
        "User-Agent": USER_AGENT
    }

    response = requests.get(
        LAST_UPDATE_URL,
        headers=headers,
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()

    latest_record = response.text.splitlines()[0]

    latest_dataset_url = latest_record.split()[-1]

    logger.info(f"Latest dataset identified: {latest_dataset_url}")

    return latest_dataset_url


def download_dataset(url: str) -> bytes:
    """
    Downloads a GDELT dataset.

    Parameters
    ----------
    url : str
        Direct URL of the dataset.

    Returns
    -------
    bytes
        Binary contents of the downloaded ZIP file.
    """

    logger.info("Downloading GDELT dataset...")

    headers = {
        "User-Agent": USER_AGENT
    }
    
    response = requests.get(
        url,
        headers=headers,
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()

    logger.info("Dataset downloaded successfully.")

    return response.content


def validate_download(content: bytes) -> None:
    """
    Validates the downloaded dataset.

    Parameters
    ----------
    content : bytes
        Binary content of the downloaded dataset.

    Raises
    ------
    ValueError
        If the downloaded content is empty.
    """
    logger.info("Validating downloaded dataset...")

    if len(content) == 0:
        raise ValueError("Downloaded dataset is empty.")

    logger.info("Download validation successful.")


def save_file(content: bytes, file_path: Path) -> None:
    """
    Saves the downloaded dataset to disk.

    Parameters
    ----------
    content : bytes
        Binary content of the downloaded dataset.

    file_path : Path
        Destination path where the dataset will be saved.
    """

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(file_path, "wb") as file:
        file.write(content)

    logger.info(f"Dataset saved to: {file_path}")


def main() -> None:
    """
    Entry point for the GDELT extraction process.
    """
    logger.info("Starting GDELT extraction...")

    try:

        url = get_latest_dataset_url()

        content = download_dataset(url)

        validate_download(content)

        file_path = Path(
            "data/raw/latest/gdelt_export.zip"
        )

        logger.info(f"Saving dataset to {file_path}")

        save_file(content, file_path)

    except requests.Timeout as error:
        logger.error(f"Request timed out: {error}")
        raise

    except requests.ConnectionError as error:
        logger.error(f"Connection failed: {error}")
        raise

    except requests.HTTPError as error:
        logger.error(f"HTTP request failed: {error}")
        raise

    except ValueError as error:
        logger.error(f"Validation failed: {error}")
        raise

    except Exception as error:
        logger.error(f"Unexpected error: {error}")
        raise

    logger.info("GDELT extraction completed successfully.")  ## much better-->  logger.exception("GDELT extraction failed.")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    main()