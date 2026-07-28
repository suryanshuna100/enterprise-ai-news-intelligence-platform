"""
Silver layer writer.

This module is responsible for persisting the Silver DataFrame.

Responsibilities
----------------
- Persist the Silver DataFrame.
- Configure write mode.
- Configure storage format.

This module performs NO transformations.
"""

from __future__ import annotations

from pyspark.sql import DataFrame


def write_silver_dataframe(
    dataframe: DataFrame,
    output_path: str,
    storage_format: str,
    write_mode: str,
) -> None:
    """
    Persist the Silver DataFrame.

    Parameters
    ----------
    dataframe : DataFrame
        Silver DataFrame.

    output_path : str
        Destination path.

    storage_format : str
        Storage format.

        Examples
        --------
        parquet
        delta

    write_mode : str
        Spark write mode.

        Examples
        --------
        overwrite
        append
        ignore
        error
    """

    (
        dataframe.write
        .format(storage_format)
        .mode(write_mode)
        .save(output_path)
    )