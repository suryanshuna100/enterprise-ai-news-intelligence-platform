from pathlib import Path

# ==========================================================
# Project Configuration
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ==========================================================
# GDELT Configuration
# ==========================================================

GDELT_BASE_URL = "http://data.gdeltproject.org/gdeltv2"

LAST_UPDATE_URL = f"{GDELT_BASE_URL}/lastupdate.txt"

MASTER_FILE_LIST_URL = f"{GDELT_BASE_URL}/masterfilelist.txt"

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