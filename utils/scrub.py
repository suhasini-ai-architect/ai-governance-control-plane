import re

class EnterpriseScrubber:
    def __init__(self):
        # Extremely broad patterns to ensure NO leakage
        self.patterns = {
            "API_Key": r'(sk|key|token|secret|auth)[-_=:][a-zA-Z0-9]{8,}',
            "Generic_Secret": r'sk-[a-zA-Z0-9-]{15,}', # Specific for your test case
            "SSN": r'\b\d{3}-\d{2}-\d{4}\b',
            "Email": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        }

    def scan(self, text):
        found_risks = []
        for label, pattern in self.patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                found_risks.append(label)
        return found_risks

    def redact(self, text):
        for label, pattern in self.patterns.items():
            text = re.sub(pattern, f"[{label}_REDACTED]", text, flags=re.IGNORECASE)
        return text