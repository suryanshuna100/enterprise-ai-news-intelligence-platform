"""
Silver layer type mapping.

This module defines the target Spark SQL data type for each GDELT
column that requires conversion from the Bronze schema.

The Bronze layer stores every column as StringType to preserve the
raw source data exactly as received.

The Silver layer uses this mapping to cast columns to their
appropriate data types.
"""

from __future__ import annotations

# Mapping:
# Key   -> Bronze column name
# Value -> Target Spark SQL type

GDELT_SILVER_TYPE_MAPPING = {

    # ------------------------------------------------------------------
    # Event identifiers
    # ------------------------------------------------------------------

    "GlobalEventID": "long",

    # ------------------------------------------------------------------
    # Date components
    # ------------------------------------------------------------------

    "MonthYear": "integer",
    "Year": "integer",
    "FractionDate": "double",

    # ------------------------------------------------------------------
    # Event information
    # ------------------------------------------------------------------

    "IsRootEvent": "integer",
    "QuadClass": "integer",

    "GoldsteinScale": "double",

    "NumMentions": "integer",
    "NumSources": "integer",
    "NumArticles": "integer",

    "AvgTone": "double",

    # ------------------------------------------------------------------
    # Actor 1 Geography
    # ------------------------------------------------------------------

    "Actor1Geo_Type": "integer",
    "Actor1Geo_Lat": "double",
    "Actor1Geo_Long": "double",

    # ------------------------------------------------------------------
    # Actor 2 Geography
    # ------------------------------------------------------------------

    "Actor2Geo_Type": "integer",
    "Actor2Geo_Lat": "double",
    "Actor2Geo_Long": "double",

    # ------------------------------------------------------------------
    # Action Geography
    # ------------------------------------------------------------------

    "ActionGeo_Type": "integer",
    "ActionGeo_Lat": "double",
    "ActionGeo_Long": "double",

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------

    "DATEADDED": "long",
}