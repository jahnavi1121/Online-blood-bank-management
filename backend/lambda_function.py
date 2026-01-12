import json
from db import add_donor, get_donors

def lambda_handler(event, context):
    method = event.get("httpMethod")

    # POST → Add donor
    if method == "POST":
        body = json.loads(event["body"])

        response = add_donor(body)

        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }

    # GET → Fetch donors
    if method == "GET":
        donors = get_donors()

        return {
            "statusCode": 200,
            "body": json.dumps(donors)
        }

    return {
        "statusCode": 400,
        "body": json.dumps({"message": "Invalid request"})
    }