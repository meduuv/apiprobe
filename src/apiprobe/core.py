from urllib.parse import urlparse


def endpoint_info(url: str) -> dict:
    parsed = urlparse(url)
    return {
        "scheme": parsed.scheme,
        "host": parsed.hostname,
        "port": parsed.port,
        "path": parsed.path or "/",
        "valid": parsed.scheme in {"http", "https"} and bool(parsed.hostname),
    }


def classify_status(status: int) -> str:
    if not 100 <= status <= 599:
        raise ValueError("status must be between 100 and 599")
    if status < 200:
        return "informational"
    if status < 300:
        return "success"
    if status < 400:
        return "redirection"
    if status < 500:
        return "client_error"
    return "server_error"


def summarize_response(status: int, headers: dict | None = None) -> dict:
    headers = headers or {}
    normalized = {str(k).lower(): str(v) for k, v in headers.items()}
    return {
        "status": status,
        "category": classify_status(status),
        "content_type": normalized.get("content-type"),
        "content_length": normalized.get("content-length"),
        "server": normalized.get("server"),
    }
