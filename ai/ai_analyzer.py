from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Read deployment logs
with open("deployment_logs.txt", "r") as f:
    logs = f.read()

# Create the prompt
prompt = f"""
You are a Senior DevOps Engineer.

Analyze the following deployment logs.

Return:

1. Deployment Status
2. Root Cause
3. Evidence
4. Suggested Fix
5. Best Practices
6. Severity
7. Confidence

Deployment Logs:

{logs}
"""

try:
    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    report = response.output_text

    print("\n========== AI DEPLOYMENT REPORT ==========\n")
    print(report)

    with open("ai_report.md", "w") as f:
        f.write(report)

except Exception as e:
    print(f"AI analysis failed: {e}")
