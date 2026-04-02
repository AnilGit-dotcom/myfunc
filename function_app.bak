import logging
import azure.functions as func
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os
import json

SERVICE_BUS_CONNECTION_STR = os.environ["SERVICE_BUS_CONNECTION_STR"]
QUEUE_NAME = os.environ.get("QUEUE_NAME", "policy-events")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing policy event...')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON body", status_code=400)

    policy_id = req_body.get("policyId")
    policy_type = req_body.get("policyType")

    if not policy_id or not policy_type:
        return func.HttpResponse("Missing policyId or policyType", status_code=400)

    # Send to Service Bus
    try:
        with ServiceBusClient.from_connection_string(SERVICE_BUS_CONNECTION_STR) as client:
            sender = client.get_queue_sender(queue_name=QUEUE_NAME)
            with sender:
                message = ServiceBusMessage(json.dumps(req_body))
                sender.send_messages(message)
                logging.info(f"Sent policyId {policy_id} to Service Bus queue {QUEUE_NAME}")
    except Exception as e:
        logging.error(f"Error sending to Service Bus: {e}")
        return func.HttpResponse(f"Failed to send message: {e}", status_code=500)

    return func.HttpResponse(
        f"Policy {policy_id} sent to Service Bus successfully",
        status_code=200
    )