import re
# Copy this exactly to match your test prompt
test_input = "Write a Python script to connect to our production database. Use my temporary access key: sk-admin-8822-secret-9911"

# The pattern we need to verify
pattern = r'(sk|key|token|secret|auth)[-_=:][a-zA-Z0-9-]{8,}'

match = re.search(pattern, test_input, re.IGNORECASE)

if match:
    print(f"✅ SUCCESS: Pattern caught '{match.group()}'")
else:
    print("❌ FAILURE: Regex did not see the key. Update your patterns.")