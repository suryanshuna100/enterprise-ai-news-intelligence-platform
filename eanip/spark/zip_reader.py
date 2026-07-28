"""
Utility functions for working with ZIP archives.

This module is responsible only for extracting files from ZIP archives.
It has no knowledge of Spark, S3, or GDELT business logic.
"""

from __future__ import annotations

import io
import zipfile


def extract_csv_from_zip(zip_content: bytes) -> bytes:
    """
    Extract the first CSV file from a ZIP archive.

    Parameters
    ----------
    zip_content : bytes
        Raw bytes of a ZIP archive.

    Returns
    -------
    bytes
        Raw bytes of the extracted CSV file.

    Raises
    ------
    ValueError
        If no CSV file exists inside the archive.
    """

    with zipfile.ZipFile(io.BytesIO(zip_content)) as archive:

        csv_files = [
            file_name
            for file_name in archive.namelist()
            if file_name.lower().endswith(".csv")
        ]

        if not csv_files:
            raise ValueError("No CSV file found inside ZIP archive.")

        with archive.open(csv_files[0]) as csv_file:
            return csv_file.read()