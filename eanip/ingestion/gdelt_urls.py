"""
Utilities for resolving GDELT dataset URLs.

This module determines which dataset should be downloaded.
It never performs HTTP requests or storage operations.
"""

from eanip.config import (
    GDELT_BASE_URL,
    LAST_UPDATE_FILE,
)


def get_last_update_url() -> str:
    """
    Return the GDELT endpoint that provides the latest dataset information.

    Returns:
        URL to the GDELT lastupdate.txt endpoint.
    """

    return f"{GDELT_BASE_URL}/{LAST_UPDATE_FILE}"


def build_export_url(timestamp: str) -> str:
    """
    Build the export dataset URL from a GDELT timestamp.

    Args:
        timestamp:
            GDELT dataset timestamp.

    Returns:
        Complete export dataset URL.
    """

    return f"{GDELT_BASE_URL}/{timestamp}.export.CSV.zip"