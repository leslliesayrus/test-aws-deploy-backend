import json


def lambda_handler(event, context):
    """
    Integração .
    """
    try:
        body_raw = event.get("body") or "{}"
        if event.get("isBase64Encoded"):
            import base64

            body_raw = base64.b64decode(body_raw).decode("utf-8")
        payload = json.loads(body_raw)
    except (json.JSONDecodeError, TypeError):
        payload = {}

    message = payload.get("message", "")

    response_body = {
        "ok": True,
        "echo": message,
        "hint": "Envie JSON com campo message no body.",
    } 

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(response_body, ensure_ascii=False),
    }
