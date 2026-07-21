"""
Utilities for uploading datasets to Amazon S3.
"""
import logging

import boto3
from botocore.exceptions import BotoCoreError, ClientError

logger = logging.getLogger(__name__)


def create_s3_client():
    """
    Creates an S3 client using boto3.

    Returns
    -------
    boto3.client
        An S3 client instance.
    """
    return boto3.client('s3')


def upload_stream(
        stream, bucket_name: str, object_key: str) -> None:
    """
    Upload a file-like object (HTTP stream) directly to Amazon S3.

    Args:
        stream:
            File-like object (e.g. response.raw).

        bucket_name:
            Destination S3 bucket.

        object_key:
            Destination object key in S3.

    Raises:
        ClientError:
            If AWS rejects the upload.

        BotoCoreError:
            For boto3 internal errors.
    """
    s3_client = create_s3_client()
 
    logger.info(
        "Uploading stream to s3://%s/%s",
        bucket_name,
        object_key,
    )
    try:

        s3_client.upload_fileobj(
            Fileobj=stream,
            Bucket=bucket_name,
            Key=object_key,
        )

        logger.info("Upload completed successfully.")

    except (ClientError, BotoCoreError) as error:

        logger.exception("Failed to upload stream to Amazon S3.")

        raise   


    
import io
import json

def upload_metadata(
        metadata: dict,
        bucket_name: str,
        object_key: str,
    ) -> None:
        """
        Upload metadata.json to Amazon S3.
        """

        s3_client = create_s3_client()

        metadata_bytes = io.BytesIO(
            json.dumps(
                metadata,
                indent=4,
            ).encode("utf-8")
        )
        
        metadata_bytes.seek(0)

        logger.info(
            "Uploading metadata to s3://%s/%s",
            bucket_name,
            object_key,
        )

        try:

            s3_client.upload_fileobj(
                Fileobj=metadata_bytes,
                Bucket=bucket_name,
                Key=object_key,
            )

            logger.info(
                "Metadata uploaded successfully."
            )

        except (ClientError, BotoCoreError):

            logger.exception(
                "Failed to upload metadata."
            )

            raise