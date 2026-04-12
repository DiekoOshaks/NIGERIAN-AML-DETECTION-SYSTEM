import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

NUM_USERS = 50
NUM_TRANSACTIONS = 5000

users = [f"user_{i}" for i in range(NUM_USERS)]

data = []

for _ in range(NUM_TRANSACTIONS):
    user = random.choice(users)

    # Normal vs suspicious behavior
    if random.random() < 0.85:
        # Normal transaction
        amount = round(random.uniform(1000, 200000), 2)
    else:
        # Suspicious transaction
        amount = round(random.uniform(300000, 2000000), 2)

    timestamp = datetime.now() - timedelta(minutes=random.randint(0, 100000))

    recipient = f"user_{random.randint(0, NUM_USERS + 20)}"

    location = random.choice([
        "Lagos", "Abuja", "Port Harcourt", "Kano", "Ibadan"
    ])

    transaction_type = random.choice([
        "transfer", "withdrawal", "deposit"
    ])

    data.append([
        user, recipient, amount, timestamp, location, transaction_type
    ])

df = pd.DataFrame(data, columns=[
    "sender", "receiver", "amount", "timestamp", "location", "type"
])

df.to_csv("transactions.csv", index=False)

print("Dataset generated successfully!")