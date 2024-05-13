def lambda_handler(event, context):
    # TODO implement
    return {
        "statusCode": 200,
        "headers": {"content-type": "text/html"},
        "body": "<body><h1>Hello Serverless World</h1></body>"
    }