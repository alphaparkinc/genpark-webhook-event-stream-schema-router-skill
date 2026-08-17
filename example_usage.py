from client import WebhookEventStreamSchemaRouterClient

def main():
    client = WebhookEventStreamSchemaRouterClient()
    raw = '{"event": "subscription.charge.success", "amount": 19900, "currency": "usd"}'
    res = client.route_webhook(raw)
    print(f"Event: {res['parsed_event_type']}")
    print(f"Route: {res['target_route']}")
    print(f"Latency: {res['processing_latency_micros']} microseconds")

if __name__ == "__main__":
    main()
