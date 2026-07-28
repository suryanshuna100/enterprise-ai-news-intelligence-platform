from pyspark.sql.types import (
    StructField,   # Defines a single column in the DataFrame schema.
    StructType,    # Defines the complete DataFrame schema.
    StringType,    # Defines the data type of a column as String.
)

GDELT_SCHEMA = StructType([
# Creates the schema for the GDELT Events dataset.

    StructField("GlobalEventID", StringType(), True),
    # Unique identifier for each GDELT event.

    StructField("Day", StringType(), True),
    # Event date in YYYYMMDD format.

    StructField("MonthYear", StringType(), True),
    # Event month in YYYYMM format.

    StructField("Year", StringType(), True),
    # Year when the event occurred.

    StructField("FractionDate", StringType(), True),
    # Decimal representation of the date for time-series analysis.

    StructField("Actor1Code", StringType(), True),
    # Unique code identifying the first actor.

    StructField("Actor1Name", StringType(), True),
    # Name of the first actor.

    StructField("Actor1CountryCode", StringType(), True),
    # Country code of the first actor.

    StructField("Actor1KnownGroupCode", StringType(), True),
    # Organization or known group of the first actor.

    StructField("Actor1EthnicCode", StringType(), True),
    # Ethnicity code of the first actor.

    StructField("Actor1Religion1Code", StringType(), True),
    # Primary religion code of the first actor.

    StructField("Actor1Religion2Code", StringType(), True),
    # Secondary religion code of the first actor.

    StructField("Actor1Type1Code", StringType(), True),
    # Primary actor classification.

    StructField("Actor1Type2Code", StringType(), True),
    # Secondary actor classification.

    StructField("Actor1Type3Code", StringType(), True),
    # Tertiary actor classification.

    StructField("Actor2Code", StringType(), True),
    # Unique code identifying the second actor.

    StructField("Actor2Name", StringType(), True),
    # Name of the second actor.

    StructField("Actor2CountryCode", StringType(), True),
    # Country code of the second actor.

    StructField("Actor2KnownGroupCode", StringType(), True),
    # Organization or known group of the second actor.

    StructField("Actor2EthnicCode", StringType(), True),
    # Ethnicity code of the second actor.

    StructField("Actor2Religion1Code", StringType(), True),
    # Primary religion code of the second actor.

    StructField("Actor2Religion2Code", StringType(), True),
    # Secondary religion code of the second actor.

    StructField("Actor2Type1Code", StringType(), True),
    # Primary actor classification.

    StructField("Actor2Type2Code", StringType(), True),
    # Secondary actor classification.

    StructField("Actor2Type3Code", StringType(), True),
    # Tertiary actor classification.

    StructField("IsRootEvent", StringType(), True),
    # Indicates whether this is the primary (root) event.

    StructField("EventCode", StringType(), True),
    # Specific CAMEO event code.

    StructField("EventBaseCode", StringType(), True),
    # Generalized event category.

    StructField("EventRootCode", StringType(), True),
    # Top-level event category.

    StructField("QuadClass", StringType(), True),
    # Broad event class (Cooperation or Conflict).

    StructField("GoldsteinScale", StringType(), True),
    # Measures the impact of the event (-10 to +10).

    StructField("NumMentions", StringType(), True),
    # Number of mentions across all news reports.

    StructField("NumSources", StringType(), True),
    # Number of unique news sources reporting the event.

    StructField("NumArticles", StringType(), True),
    # Number of news articles covering the event.

    StructField("AvgTone", StringType(), True),
    # Average sentiment/tone of the news coverage.

    StructField("Actor1Geo_Type", StringType(), True),
    # Geographic location type of Actor 1.

    StructField("Actor1Geo_FullName", StringType(), True),
    # Full location name of Actor 1.

    StructField("Actor1Geo_CountryCode", StringType(), True),
    # Country code of Actor 1's location.

    StructField("Actor1Geo_ADM1Code", StringType(), True),
    # State or administrative region of Actor 1.

    StructField("Actor1Geo_Lat", StringType(), True),
    # Latitude of Actor 1's location.

    StructField("Actor1Geo_Long", StringType(), True),
    # Longitude of Actor 1's location.

    StructField("Actor1Geo_FeatureID", StringType(), True),
    # Geographic feature identifier.

    StructField("Actor2Geo_Type", StringType(), True),
    # Geographic location type of Actor 2.

    StructField("Actor2Geo_FullName", StringType(), True),
    # Full location name of Actor 2.

    StructField("Actor2Geo_CountryCode", StringType(), True),
    # Country code of Actor 2's location.

    StructField("Actor2Geo_ADM1Code", StringType(), True),
    # State or administrative region of Actor 2.

    StructField("Actor2Geo_Lat", StringType(), True),
    # Latitude of Actor 2's location.

    StructField("Actor2Geo_Long", StringType(), True),
    # Longitude of Actor 2's location.

    StructField("Actor2Geo_FeatureID", StringType(), True),
    # Geographic feature identifier.

    StructField("ActionGeo_Type", StringType(), True),
    # Type of location where the event occurred.

    StructField("ActionGeo_FullName", StringType(), True),
    # Full name of the event location.

    StructField("ActionGeo_CountryCode", StringType(), True),
    # Country code where the event occurred.

    StructField("ActionGeo_ADM1Code", StringType(), True),
    # State or administrative region of the event location.

    StructField("ActionGeo_Lat", StringType(), True),
    # Latitude of the event location.

    StructField("ActionGeo_Long", StringType(), True),
    # Longitude of the event location.

    StructField("ActionGeo_FeatureID", StringType(), True),
    # Geographic feature identifier of the event location.

    StructField("DATEADDED", StringType(), True),
    # Timestamp when GDELT added the event to its database.

    StructField("SOURCEURL", StringType(), True),
    # Original news article URL from which the event was extracted.

])
# Ends the schema definition.