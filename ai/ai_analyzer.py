
import os
from openai import OpenAI

# Read API key from environment variable
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Read deployment logs
with open("deployment_logs.txt", "r") as f:
    logs = f.read()

prompt = f"""
You are a Senior DevOps Engineer.

Analyze the following deployment logs.

Return your answer using exactly these sections:

Deployment Status:
Root Cause:
Evidence:
Suggested Fix:
Best Practices:
Severity:
Confidence:

Logs:
{logs}
"""

response = client.responses.create(
    model="gpt-5",
    input=prompt
)

print("\n========== AI DEPLOYMENT REPORT ==========\n")
print(response.output_text)
