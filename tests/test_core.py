from apiprobe import classify_status, endpoint_info, summarize_response


def test_classify_status():
    assert classify_status(200) == "success"
    assert classify_status(404) == "client_error"
    assert classify_status(503) == "server_error"


def test_endpoint_info():
    info = endpoint_info("https://example.com/api")
    assert info["valid"] is True
    assert info["host"] == "example.com"
    assert info["path"] == "/api"


def test_summary_normalizes_headers():
    result = summarize_response(204, {"Content-Type": "application/json"})
    assert result["category"] == "success"
    assert result["content_type"] == "application/json"
