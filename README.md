
---

## Core Components

### Sentry Agent (Pre-Processor)

- Detects and masks sensitive data using regex and local inference
- Prevents exposure of emails, API keys, and sensitive identifiers
- Enforces zero-trust input validation

---

### Budgeter Agent (FinOps Engine)

- Applies token budget policies
- Dynamically selects optimal execution path
- Routes complex queries to cloud models
- Routes simple queries to local models
- Enables cost optimization

---

### Intelligent Router

- Routes requests through a unified abstraction layer
- Supports multiple LLM providers via LiteLLM
- Decouples application logic from model providers

---

### Auditor Agent (Post-Processor)

- Validates responses using rule-based and agent-driven checks
- Detects hallucinations, policy violations, and unsafe outputs
- Supports response blocking, rewriting, and escalation

---

### Observability and Governance Layer

- Provides real-time monitoring using Streamlit
- Tracks token usage, cost savings, risk scores, and audit logs

---

## Key Capabilities

### Data Protection

- Local PII masking before external calls
- Prevents sensitive data from leaving system boundaries

### Cost Optimization

- Budget-aware routing strategy
- Reduces dependency on expensive cloud models

### Output Reliability

- Detects hallucinations and unsafe responses
- Applies validation and correction mechanisms

### Observability

- Provides visibility into AI usage and behavior
- Enables governance and auditability

---

## Technology Stack

| Layer | Technology |
|------|------------|
| Orchestration | LangGraph |
| Gateway | LiteLLM, FastAPI |
| Local Models | Ollama |
| Governance | Regex, custom policies |
| Validation | Guardrails, custom logic |
| UI | Streamlit |

---

## Execution Flow

1. Input is intercepted and sanitized  
2. Budget and complexity are evaluated  
3. Request is routed to the optimal model  
4. Output is validated for safety and compliance  
5. Metrics are captured for governance and optimization  

---

## Example Use Case

**Input:**

Analyze customer data containing emails and identifiers

**System Behavior:**

- Sensitive data is masked locally
- Request is routed based on complexity
- Output is validated for compliance
- Risk score is generated

---

## Business Impact

- Reduces risk of data leakage
- Lowers AI operational cost
- Improves reliability of AI-generated outputs
- Enables scalable enterprise AI adoption

---

## Installation and Setup

```bash
git clone https://github.com/suhasini-ai-architect/ai-governance-control-plane.git
cd guardian-mesh

python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt

## Running the Application

streamlit run app.py

## Positioning Statement

This project demonstrates:

Enterprise AI governance architecture
Multi-agent orchestration design
Cost-aware LLM routing (AI FinOps)
Secure and scalable AI system design
Future Enhancements
Integration with enterprise SIEM tools
Policy-based governance and access control
Multi-model orchestration
Kubernetes deployment
Author

## Enterprise AI Architect
Multi-Agent Systems, AI Governance, Cloud Architecture

## Conclusion

Guardian-Mesh is a reference architecture for enterprise AI governance, enabling organizations to scale AI systems with control, transparency, and cost efficiency.
