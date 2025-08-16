import os

def get_env_list(name: str):
    val = os.getenv(name, "").strip()
    return [x.strip() for x in val.split(",") if x.strip()]

ROLE_KEYWORDS = [x.lower() for x in get_env_list("ROLE_KEYWORDS")] or [
    "data engineer", "pyspark", "iics", "etl"
]
LOCATIONS = get_env_list("LOCATIONS")  # optional

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN", "")
WHATSAPP_PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "")
WHATSAPP_TO = os.getenv("WHATSAPP_TO", "")

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)
REQUEST_TIMEOUT = 20
MAX_PER_SOURCE = 30
