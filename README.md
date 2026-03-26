Guardian-Mesh: AI Governance Control Plane
Overview

Guardian-Mesh is an enterprise-grade AI governance layer designed to address the key challenges in large-scale AI adoption:

Data privacy risks (PII leakage)
Uncontrolled LLM costs (FinOps)
Hallucinations and unreliable outputs

It acts as a Zero-Trust AI control plane between users and LLMs, enforcing governance, optimizing cost, and validating outputs in real time.

Guardian-Mesh can be positioned as a unified layer combining a firewall, cost optimization engine, and output validation system for AI platforms.

One-Line Value Proposition

A Zero-Trust AI control plane that governs, optimizes, and validates every LLM interaction.

Why This Project Matters

As enterprises adopt Generative AI, they face systemic risks:

Unmonitored and uncontrolled AI usage
Exposure of sensitive enterprise data
Rapid increase in token consumption and cost
Lack of trust in model-generated outputs

Guardian-Mesh introduces a governed execution layer that brings control, visibility, and reliability to AI systems.

Architecture Diagram

Add your architecture image here.

![Guardian Mesh Architecture](./assets/guardian-mesh-architecture.png)
Architecture Overview
User / Application
        ↓
Guardian-Mesh Control Plane
        ↓
Input Guard Layer (PII Protection and Injection Defense)
        ↓
Sentry Agent (Pre-Processing)
        ↓
Budgeter Agent (Cost and Policy Decision)
        ↓
Intelligent Router (Execution Layer)
        ↓
Cloud LLM (Azure OpenAI) or Local LLM (Ollama)
        ↓
Auditor Agent (Validation and Risk Control)
        ↓
Observability Layer (Cost, Risk, Usage, Logs)
Core Components
Sentry Agent (Pre-Processor)
Detects and masks sensitive data using regex and local inference
Prevents exposure of emails, API keys, and sensitive identifiers
Enforces zero-trust input validation
Budgeter Agent (FinOps Engine)
Applies token budget policies
Dynamically selects optimal execution path
Routes complex queries to cloud models
Routes simple queries to local models
Enables cost optimization
Intelligent Router
Routes requests through a unified abstraction layer
Uses LiteLLM for multi-provider support
Decouples application logic from model providers
Auditor Agent (Post-Processor)
Validates responses using rule-based and agent-driven checks
Detects hallucinations, policy violations, and unsafe outputs
Supports response blocking, rewriting, and escalation
Observability and Governance Layer
Provides real-time monitoring using Streamlit
Tracks token usage, cost savings, risk scores, and audit logs
Key Capabilities
Data Protection
Local PII masking before external calls
Prevents sensitive data from leaving system boundaries
Cost Optimization
Budget-aware routing strategy
Reduces dependency on expensive cloud models
Enables efficient AI resource utilization
Output Reliability
Detects hallucinations and unsafe responses
Applies validation and correction mechanisms
Observability
Provides visibility into AI usage and behavior
Enables governance and auditability
Technology Stack
Layer	Technology
Orchestration	LangGraph
Gateway	LiteLLM, FastAPI
Local Models	Ollama
Governance	Regex and custom policies
Validation	Guardrails and custom logic
UI	Streamlit
Execution Flow
Input is intercepted and sanitized
Budget and complexity are evaluated
Request is routed to the optimal model
Output is validated for safety and compliance
Metrics are captured for governance and optimization
Example Use Case

Input:
Analyze customer data containing emails and identifiers

System behavior:

Sensitive data is masked locally
Request is routed based on complexity
Output is validated for compliance
Risk score is generated
Business Impact
Reduces risk of data leakage
Lowers AI operational cost
Improves reliability of AI-generated outputs
Enables scalable enterprise AI adoption
Installation and Setup
git clone https://github.com/suhasini-ai-architect/ai-governance-control-plane.git
cd guardian-mesh

python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt
Running the Application
streamlit run app.py
Positioning Statement

This project demonstrates:

Enterprise AI governance architecture
Multi-agent orchestration design
Cost-aware LLM routing (AI FinOps)
Secure and scalable AI system design
Future Enhancements
Integration with enterprise SIEM tools
Policy-based governance and access control
Multi-model orchestration
Kubernetes-based deployment
Author

Enterprise AI Architect
Multi-Agent Systems, AI Governance, Cloud Architecture

Conclusion

Guardian-Mesh represents a reference architecture for enterprise AI governance, enabling organizations to adopt and scale AI systems with control, transparency, and cost efficiency.
