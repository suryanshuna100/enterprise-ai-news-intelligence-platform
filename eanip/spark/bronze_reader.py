"""
Bronze layer reader.

This module reads raw GDELT ZIP files from the Bronze layer,
extracts the CSV file, and returns a Spark DataFrame.

Responsibilities
----------------
- Read ZIP archive from Bronze storage.
- Extract CSV bytes using zip_reader.
- Load CSV into a Spark DataFrame using the predefined schema.

This module is responsible only for converting raw Bronze ZIP files
into Spark DataFrames. Data cleansing, validation, and type conversion
are delegated to the Silver layer.
"""

from __future__ import annotations

import tempfile

from pyspark.sql import DataFrame, SparkSession

from eanip.spark.schemas import GDELT_SCHEMA
from eanip.spark.zip_reader import extract_csv_from_zip


def read_bronze_events(
    spark: SparkSession,
    bronze_zip_path: str,
) -> DataFrame:
    """
    Read a Bronze GDELT ZIP file into a Spark DataFrame.

    Parameters
    ----------
    spark : SparkSession
        Active Spark session.

    bronze_zip_path : str
        Path to the ZIP file in Bronze storage.

    Returns
    -------
    DataFrame
        Raw Bronze DataFrame.
    """

    # Read ZIP file as binary
    binary_df = (
        spark.read
        .format("binaryFile")
        .load(bronze_zip_path)
    )

    # Extract ZIP bytes
    row = binary_df.select("content").first()

    if row is None:
        raise FileNotFoundError(
        f"No Bronze file found at: {bronze_zip_path}"
    )

    zip_bytes = row["content"]

    # Extract CSV bytes from ZIP
    csv_bytes = extract_csv_from_zip(zip_bytes)

    # Create temporary CSV file
    with tempfile.NamedTemporaryFile(
        suffix=".csv",
        delete=False,
    ) as temp_csv:

        temp_csv.write(csv_bytes)
        temp_csv_path = temp_csv.name

    # Read CSV using Spark
    df = (
        spark.read
        .option("header", "false")
        .schema(GDELT_SCHEMA)
        .csv(temp_csv_path)
    )

    return df