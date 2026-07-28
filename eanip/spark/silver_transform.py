from pyspark.sql import DataFrame
from pyspark.sql.functions import col, to_date

from eanip.spark.silver_types import TYPE_MAPPING


def transform_to_silver(df: DataFrame) -> DataFrame:
    """
    Transform a Bronze DataFrame into a typed Silver DataFrame.
    """

    # Cast numeric columns
    for column_name, spark_type in TYPE_MAPPING.items():
        df = df.withColumn(
            column_name,
            col(column_name).cast(spark_type)
        )

    # Convert dates
    df = df.withColumn(
        "Day",
        to_date(col("Day"), "yyyyMMdd")
    )

    return df