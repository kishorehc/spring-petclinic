
# import os
# from openai import OpenAI

# # Read API key from environment variable
# client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# # Read deployment logs
# with open("deployment_logs.txt", "r") as f:
#     logs = f.read()

# prompt = f"""
# You are a Senior DevOps Engineer.

# Analyze the following deployment logs.

# Return your answer using exactly these sections:

# Deployment Status:
# Root Cause:
# Evidence:
# Suggested Fix:
# Best Practices:
# Severity:
# Confidence:

# Logs:
# {logs}
# """

# response = client.responses.create(
#     model="gpt-5",
#     input=prompt
# )

# print("\n========== AI DEPLOYMENT REPORT ==========\n")
# print(response.output_text)


from openai import OpenAI
from openai import RateLimitError
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

try:
    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    report = response.output_text

    print(report)

    with open("ai_report.md", "w") as f:
        f.write(report)

except RateLimitError:
    print("OpenAI quota exceeded. Please check billing or API credits.")

except Exception as e:
    print(f"AI analysis failed: {e}")
