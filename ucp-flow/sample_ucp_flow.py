from __future__ import annotations

import json
from datetime import datetime, timezone


def build_flow():
    return [
        {"step": 1, "name": "intent_discovery", "payload": {"intent": "pasta_dinner_under_40"}},
        {"step": 2, "name": "merchant_capability_check", "payload": {"capabilities": ["product_discovery", "inventory_check", "cart_create", "checkout_session"]}},
        {"step": 3, "name": "product_discovery", "payload": {"skus": ["SKU-PASTA-001", "SKU-SAUCE-001", "SKU-SALAD-001"]}},
        {"step": 4, "name": "cart_creation", "payload": {"cart_id": "cart_ucp_demo"}},
        {"step": 5, "name": "cart_mandate_creation", "payload": {"cart_id": "cart_ucp_demo", "budget_limit": 40, "allowed_actions": ["add", "coupon_apply"]}},
        {"step": 6, "name": "coupon_discount_update", "payload": {"coupon_code": "SAVE10", "valid": True}},
        {"step": 7, "name": "checkout_hydration", "payload": {"total": 22.41, "currency": "USD"}},
        {"step": 8, "name": "pickup_delivery_selection", "payload": {"fulfillment_type": "pickup", "slot": "tomorrow_morning"}},
        {"step": 9, "name": "user_confirmation", "payload": {"required": True}},
        {"step": 10, "name": "mock_order_placement", "payload": {"order_id": "order_ucp_demo", "timestamp": datetime.now(timezone.utc).isoformat()}},
        {"step": 11, "name": "order_tracking", "payload": {"status": "placed"}},
    ]


if __name__ == "__main__":
    print(json.dumps(build_flow(), indent=2))
