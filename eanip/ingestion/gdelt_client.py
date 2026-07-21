"""
HTTP client for downloading datasets from GDELT.

This module communicates with GDELT and returns HTTP responses.
It does not perform storage or metadata generation.
"""

import logging

import requests
from requests import Response
from requests.exceptions import RequestException

from eanip.config import USER_AGENT

logger = logging.getLogger(__name__)


def download_stream(url: str) -> Response:
    """
    Download a dataset from GDELT as a streaming HTTP response.

    Args:
        url:
            Dataset URL.

    Returns:
        HTTP response object.

    Raises:
        RequestException:
            If the download fails.
    """

    logger.info("Downloading dataset from %s", url)

    try:

        from eanip.config import (REQUEST_TIMEOUT, USER_AGENT,)

        response = requests.get(
            url=url,
            stream=True,
            timeout=REQUEST_TIMEOUT,
            headers={
                "User-Agent": USER_AGENT,
            },
        )

        response.raise_for_status()

        logger.info(
            "Dataset downloaded successfully. Status Code: %s",
            response.status_code,
        )

        return response

    except RequestException:

        logger.exception(
            "Failed to download dataset."
        )

        raise


from eanip.ingestion.gdelt_urls import get_last_update_url


def get_latest_dataset_url() -> str:
    """
    Resolve the latest available GDELT export dataset URL.

    Downloads the GDELT lastupdate.txt file, extracts the latest
    export dataset URL, and returns it.

    Returns
    -------
    str
        URL of the latest GDELT export.CSV.zip dataset.

    Raises
    ------
    RequestException
        If the lastupdate.txt file cannot be downloaded.
    ValueError
        If the file format is invalid.
    """

    logger.info("Resolving latest GDELT dataset URL.")

    last_update_url = get_last_update_url()

    try:

        # Download lastupdate.txt
        response = download_stream(last_update_url)

        # Example first line:
        # 340219 https://data.gdeltproject.org/gdeltv2/20260720103000.export.CSV.zip
        first_line = response.text.strip().splitlines()[0]

        # Extract the export dataset URL
        latest_dataset_url = first_line.split()[-1]

        logger.info(
            "Latest dataset URL resolved successfully: %s",
            latest_dataset_url,
        )

        return latest_dataset_url

    except RequestException:

        logger.exception(
            "Failed to resolve latest dataset URL."
        )

        raise

    except (IndexError, ValueError):

        logger.exception(
            "Invalid format received from lastupdate.txt."
        )

        raise ValueError(
            "Unable to parse GDELT lastupdate.txt."
        )