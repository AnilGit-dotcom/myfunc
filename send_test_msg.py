from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os
import json

conn_str = os.environ.get("SERVICE_BUS_CONNECTION_STR")
queue_name = os.environ.get("QUEUE_NAME")

servicebus_client = ServiceBusClient.from_connection_string(conn_str)
with servicebus_client:
    sender = servicebus_client.get_queue_sender(queue_name=queue_name)
    with sender:
        message_data = {"policyId": "12345", "policyType": "Health"}
        message = ServiceBusMessage(json.dumps(message_data))
        sender.send_messages(message)
        print("Test message sent!")