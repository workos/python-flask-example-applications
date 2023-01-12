from datetime import datetime

user_organization_set = {
    "action": "user.organization_set",
    "occurred_at": datetime.now().isoformat(),
    "actor": {
        "type": "user",
        "id": "user_01GBNJC3MX9ZZJW1FSTF4C5938",
    },
    "targets": [
        {
            "type": "team",
            "id": "team_01GBNJD4MKHVKJGEWK42JNMBGS",
        },
    ],
    "context": {
        "location": "123.123.123.123",
        "user_agent": "Chrome/104.0.0.0",
    },
}
