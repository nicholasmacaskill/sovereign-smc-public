import subprocess
import os

# Values sourced from your .env.local
secrets = {
    "GEMINI_API_KEY": "AIzaSyCG8MLSeiG-k6u48RW0gjCwPJRA59nld_Y",
    "TELEGRAM_BOT_TOKEN": "8408836802:AAFgtKeid0xPVcczjUa3PdjzxMKWo5EA-Fk",
    "TELEGRAM_CHAT_ID": "7934081383",
    "CRYPTOPANIC_API_KEY": "ffe28af03a6f44dd84ae8b3d72feb79362509658",
    "WHALE_ALERT_API_KEY": "SKIP",
    "SYNC_AUTH_KEY": "cxS_KlwEq5fPfiNggQfMQa6Smxt-2WA5DLiF3TMwbJk",
    # Account A
    "TRADELOCKER_EMAIL_A": "1h3w4hp7ld@upcomers.com",
    "TRADELOCKER_PASSWORD_A": "u2Nx<%pUL}79",
    "TRADELOCKER_SERVER_A": "UPCOMS",
    "TRADELOCKER_BASE_URL_A": "https://demo.tradelocker.com",
    # Account B
    "TRADELOCKER_EMAIL_B": "5pys8ajue0@upcomers.com",
    "TRADELOCKER_PASSWORD_B": "t1M2-@vOw]9B",
    "TRADELOCKER_SERVER_B": "UPCOMS",
    "TRADELOCKER_BASE_URL_B": "https://demo.tradelocker.com"
}

# Construct the command
cmd = ["./venv/bin/modal", "secret", "create", "smc-secrets", "--force"]
for k, v in secrets.items():
    cmd.append(f"{k}={v}")

print("🚀 Uploading secrets to Modal (smc-secrets)...")
try:
    subprocess.run(cmd, check=True)
    print("✅ Secrets configured successfully!")
except subprocess.CalledProcessError as e:
    print(f"❌ Error uploading secrets: {e}")
