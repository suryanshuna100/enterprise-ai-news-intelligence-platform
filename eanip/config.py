
from pathlib import Path

# ==========================================================
# Project Configuration
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ==========================================================
# GDELT Configuration
# ==========================================================

GDELT_BASE_URL = "http://data.gdeltproject.org/gdeltv2"

LAST_UPDATE_FILE = "lastupdate.txt"

MASTER_FILE_LIST = "masterfilelist.txt"

# ==========================================================
# Local Storage
# ==========================================================

RAW_DATA_DIRECTORY = PROJECT_ROOT / "data" / "raw" / "gdelt"

# ==========================================================
# HTTP Configuration
# ==========================================================

REQUEST_TIMEOUT = 30

USER_AGENT = "EnterpriseAINewsIntelligencePlatform/0.3.0"

# ==========================================================
# Logging
# ==========================================================

LOG_LEVEL = "INFO"

LOG_DIRECTORY = PROJECT_ROOT / "logs"


'''Things that belong in config.py:

✅ Base URLs
✅ Timeouts
✅ Retry counts
✅ AWS bucket names
✅ Region
✅ User agent
✅ API endpoints
'''
AWS_REGION = "ap-south-1"

S3_BUCKET_NAME = "eanip-bronze-2026-ss"

BRONZE_PREFIX = "bronze"

GDELT_PREFIX = "gdelt"

MAX_RETRIES = 3

RETRY_BACKOFF = 2

METADATA_FILENAME = "metadata.json"

LOG_FORMAT = (
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# ==========================================================
# Bronze Layer
# ==========================================================

BRONZE_PATH = (
    f"s3a://{S3_BUCKET_NAME}/{BRONZE_PREFIX}/{GDELT_PREFIX}/"
)
# ==========================================================
# Silver Layer
# ==========================================================

SILVER_PREFIX = "silver"

SILVER_PATH = (
    f"s3a://{S3_BUCKET_NAME}/{SILVER_PREFIX}/{GDELT_PREFIX}/events/"
)

# Supported:
# parquet
# delta

SILVER_FILE_FORMAT = "parquet"

# Supported:
# overwrite
# append
# error
# ignore

SILVER_WRITE_MODE = "overwrite"