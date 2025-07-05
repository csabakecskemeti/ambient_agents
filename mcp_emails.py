import time
import random
from fastmcp import FastMCP

mcp = FastMCP("Emails")

@mcp.tool()
def new_email() -> dict:
    """Return a new email (either normal or spam) as a JSON blob after a random delay"""

    # Simulate delay
    delay = random.randint(10, 60)
    time.sleep(delay)

    # Define both possible emails
    legitimate_email = {
        "from": "alice@example.com",
        "to": "bob@example.com",
        "subject": "Meeting Reminder",
        "body": "Hi Bob,\n\nJust a reminder that we have a meeting scheduled for tomorrow at 10 AM.\n\nBest,\nAlice"
    }

    spam_email = {
        "from": "prince@nigeria.gov",
        "to": "bob@example.com",
        "subject": "Urgent: Claim your inheritance",
        "body": "Congratulations! You've been selected to receive $10 million. Please send your bank details immediately to claim your prize."
    }

    # 50% chance to return spam
    return random.choice([legitimate_email, spam_email])


@mcp.tool()
def delete_email(email: dict) -> str:
    """Delete email if spam"""
    email_id = 1
    return f"email: {email_id} has been deleted"

if __name__ == "__main__":
    mcp.run(transport="stdio")