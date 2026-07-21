from datetime import datetime


def build_metadata(
    response,
    source_url: str,
    upload_status: str,
) -> dict:
    """
    Build metadata for an ingested dataset.

    Args:
        response:
            HTTP response returned by the download request.
        source_url:
            Original dataset URL.
        upload_status:
            Upload status (e.g. SUCCESS, FAILED).

    Returns:
        Metadata dictionary.
    """

    return {
        "dataset_url": source_url,
        "ingestion_timestamp": datetime.utcnow().isoformat(),
        "file_size": response.headers.get("Content-Length"),
        "content_type": response.headers.get("Content-Type"),
        "http_status": response.status_code,
        "status": upload_status,
        "checksum": None,
    }