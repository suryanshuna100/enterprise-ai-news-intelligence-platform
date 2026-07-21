"""
Main orchestration script for the Enterprise AI News Intelligence Platform.

This script performs the complete ingestion workflow:
1. Build the latest GDELT download URL.
2. Download the dataset as an HTTP stream.
3. Generate ingestion metadata.
4. Upload the dataset to the Bronze layer.
5. Upload metadata.json.
"""
from datetime import datetime, UTC
from zoneinfo import ZoneInfo
from urllib.parse import urlparse
from pathlib import PurePosixPath

import logging
import time

from eanip.ingestion.gdelt_client import (
    download_stream,
    get_latest_dataset_url,
)
#from eanip.ingestion.gdelt_urls import get_last_update_url --> not using anymore, as the get_latest_dataset_url() is now in gdelt_client.py
from eanip.ingestion.metadata import build_metadata
from eanip.storage.s3_storage import (
    upload_metadata,
    upload_stream,
)



from botocore.exceptions import BotoCoreError, ClientError
from requests.exceptions import (
    ConnectionError,
    HTTPError,
    RequestException,
    Timeout,
)

from eanip.config import (
    S3_BUCKET_NAME,
    BRONZE_PREFIX,
    GDELT_PREFIX,
)

logging.Formatter.converter = time.gmtime
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def main() -> None:
    """
    Execute the end-to-end ingestion workflow.

    Raises
    ------
    Exception
        Propagates any unexpected exception after logging.
    """

    logger.info("Starting GDELT ingestion workflow.")

    try:

        # -----------------------------------------------------
        # Step 1
        # Build the latest GDELT download URL.
        # -----------------------------------------------------

        logger.info("Building latest GDELT dataset URL.")

        url = get_latest_dataset_url()

        logger.info("Dataset URL: %s", url)

        # -----------------------------------------------------
        # Step 2
        # Download dataset as an HTTP stream.
        # -----------------------------------------------------

        logger.info("Downloading dataset.")

        dataset_response = download_stream(url)

        logger.info("Dataset downloaded successfully.")

        # -----------------------------------------------------
        # Step 3
        # Create metadata dictionary.
        # -----------------------------------------------------
        ''' it is better to generate metadata after the upload is successful, so that the status can be SUCCESS instead of PENDING.
        logger.info("Generating ingestion metadata.")

        metadata = build_metadata(
            response=dataset_response,
            source_url=url,
            upload_status="PENDING",
        )
       
        logger.info("Metadata generated successfully.")
        '''
        # -----------------------------------------------------
        # Step 4
        # Upload ZIP dataset to Amazon S3 Bronze layer.
        # -----------------------------------------------------

        logger.info("Uploading dataset to Amazon S3.")
        
        ingestion_time = datetime.now(UTC)

        ingestion_date = ingestion_time.strftime("%Y-%m-%d")

        ingestion_clock = ingestion_time.strftime("%H%M%S")

        s3_prefix = (
        f"{BRONZE_PREFIX}/"
        f"{GDELT_PREFIX}/"
        f"ingestion_date={ingestion_date}/"
        f"ingestion_time={ingestion_clock}/"
        )

        filename = PurePosixPath(
            urlparse(url).path
        ).name
        zip_object_key = f"{s3_prefix}{filename}"

        metadata_object_key = f"{s3_prefix}metadata.json"

        upload_stream(
            stream=dataset_response.raw,
            bucket_name=S3_BUCKET_NAME,
            object_key=zip_object_key,
        )

        logger.info("Dataset uploaded successfully.")

        # -----------------------------------------------------
        # Step 5
        # Build metadata after successful upload.
        # -----------------------------------------------------

        logger.info("Generating ingestion metadata.")

        metadata = build_metadata(
            response=dataset_response,
            source_url=url,
            upload_status="SUCCESS",
        )

        logger.info("Metadata generated successfully.")
        # -----------------------------------------------------
        # Step 6
        # Upload metadata.json beside the dataset.
        # -----------------------------------------------------

        logger.info("Uploading metadata.")

        upload_metadata(
            metadata=metadata,
            bucket_name=S3_BUCKET_NAME,
            object_key=metadata_object_key,
        )

        

        logger.info("GDELT ingestion workflow completed successfully.")

    
    except Timeout as error:

        logger.error("Request timed out: %s", error)

        raise

    except ConnectionError as error:

        logger.error("Connection failed: %s", error)

        raise

    except HTTPError as error:

        logger.error("HTTP request failed: %s", error)

        raise

    except (ClientError, BotoCoreError) as error:

        logger.error("Amazon S3 upload failed: %s", error)

        raise

    except ValueError as error:

        logger.error("Metadata validation failed: %s", error)

        raise

    except RequestException as error:

        logger.error("Unexpected request error: %s", error)

        raise

    except Exception as error:

        logger.exception("Unexpected error during ingestion: %s", error)

        raise


if __name__ == "__main__":
    main()

