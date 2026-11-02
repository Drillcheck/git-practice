import os

# Read from the environment. The key itself never belongs in the repository.
PAYMENT_KEY = os.environ.get("PAYMENT_KEY", "")
