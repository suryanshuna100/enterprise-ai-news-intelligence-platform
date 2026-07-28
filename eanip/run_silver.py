"""
Main orchestration script for the Bronze to Silver pipeline.

Workflow
--------
1. Create SparkSession.
2. Read Bronze dataset.
3. Transform Bronze -> Silver.
4. Persist Silver dataset.
"""

from __future__ import annotations

import logging
import time

from eanip import spark
from pyspark.sql import SparkSession

from eanip.config import (
    SILVER_PATH,
    SILVER_STORAGE_FORMAT,
    SILVER_WRITE_MODE,
)

from eanip.storage.bronze_locator import (
    get_latest_bronze_zip_path,
)
from eanip.spark.bronze_reader import read_bronze_events
from eanip.spark.silver_transform import transform_to_silver
from eanip.storage.silver_writer import write_silver_dataframe

logging.Formatter.converter = time.gmtime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def create_spark_session() -> SparkSession:
    """
    Create SparkSession.
    """

    return (
        SparkSession.builder
        .appName("EANIP Silver Pipeline")
        .config(
            "spark.sql.session.timeZone",
            "UTC",
        )
        .getOrCreate()
    )


def main() -> None:
    """
    Execute the Bronze to Silver pipeline.
    """

    logger.info("Starting Silver transformation workflow.")

    spark = create_spark_session()

    try:

        # --------------------------------------------------
        # Step 1
        # Read Bronze dataset
        # --------------------------------------------------

        logger.info("Reading Bronze dataset.")

        latest_bronze_zip = get_latest_bronze_zip_path()

        bronze_df = read_bronze_events(
            spark=spark,
            bronze_zip_path=latest_bronze_zip,
        )

        logger.info("Bronze dataset loaded successfully.")

        # --------------------------------------------------
        # Step 2
        # Transform Bronze -> Silver
        # --------------------------------------------------

        logger.info("Transforming Bronze dataset.")

        silver_df = transform_to_silver(
            bronze_df
        )

        logger.info("Transformation completed.")

        # --------------------------------------------------
        # Step 3
        # Persist Silver dataset
        # --------------------------------------------------

        logger.info("Writing Silver dataset.")

        write_silver_dataframe(
            dataframe=silver_df,
            output_path=SILVER_PATH,
            storage_format=SILVER_STORAGE_FORMAT,
            write_mode=SILVER_WRITE_MODE,
        )

        logger.info("Silver dataset written successfully.")

    except Exception:

        logger.exception(
            "Silver pipeline failed."
        )

        raise

    finally:

        spark.stop()

        logger.info(
            "Spark session stopped."
        )


if __name__ == "__main__":
    main()