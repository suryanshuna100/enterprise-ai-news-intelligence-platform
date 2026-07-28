"""
Bronze layer locator.

This module is responsible for locating the latest Bronze
dataset stored in Amazon S3.

Responsibilities
----------------
- List Bronze objects.
- Ignore metadata files.
- Find the latest Bronze ZIP.
- Return an S3A URI for Spark.

This module performs NO Spark operations.
"""

from __future__ import annotations

import logging

import boto3

from botocore.exceptions import ClientError

from eanip.config import (
    AWS_REGION,
    S3_BUCKET_NAME,
    BRONZE_PREFIX,
    GDELT_PREFIX,
)

logger = logging.getLogger(__name__)


def get_latest_bronze_zip_path() -> str:
    """
    Return the latest Bronze ZIP file.

    Returns
    -------
    str
        S3A URI of the latest Bronze ZIP.

    Raises
    ------
    FileNotFoundError
        If no Bronze ZIP exists.

    ClientError
        If S3 request fails.
    """

    prefix = f"{BRONZE_PREFIX}/{GDELT_PREFIX}/"

    s3 = boto3.client(
        "s3",
        region_name=AWS_REGION,
    )

    paginator = s3.get_paginator(
        "list_objects_v2"
    )

    latest_object = None

    try:

        for page in paginator.paginate(
            Bucket=S3_BUCKET_NAME,
            Prefix=prefix,
        ):

            if "Contents" not in page:
                continue

            for obj in page["Contents"]:

                key = obj["Key"]

                if not key.endswith(".zip"):
                    continue

                if (
                    latest_object is None
                    or obj["LastModified"]
                    > latest_object["LastModified"]
                ):
                    latest_object = obj

        if latest_object is None:

            raise FileNotFoundError(
                "No Bronze ZIP files found."
            )

        latest_path = (
            f"s3a://{S3_BUCKET_NAME}/"
            f"{latest_object['Key']}"
        )

        logger.info(
            "Latest Bronze ZIP located: %s",
            latest_path,
        )

        return latest_path

    except ClientError:

        logger.exception(
            "Failed to locate Bronze dataset."
        )

        raise
    