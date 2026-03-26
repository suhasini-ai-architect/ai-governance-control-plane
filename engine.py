from langgraph.graph import StateGraph, END
from utils.scrub import EnterpriseScrubber
import json

scrubber = EnterpriseScrubber()

class AgentState(dict):
    user_input: str
    status: str
    selected_model: str
    output: str
    risk_score: float
    estimated_cost: float

def pii_scrubber_node(state):
    text = state['user_input']
    risks = scrubber.scan(text)
    
    if risks:
        return {
            "status": "FLAGGED", 
            "user_input": scrubber.redact(text), 
            "output": f"Security Violation: {', '.join(risks)} detected.",
            "risk_score": 1.0
        }
    return {"status": "CLEAN", "risk_score": 0.0}

def finops_router_node(state):
    # If the status is NOT 'CLEAN', we STOP immediately
    if state.get('status', 'INIT') != "CLEAN":
        # Force these fields so the UI doesn't get 'None'
        return {"selected_model": "BLOCKED", "estimated_cost": 0.0}
    
    # Normal logic...
    return {"selected_model": "ollama/llama3.2", "estimated_cost": 0.0001}

def execution_node(state):
    # Double-check: Never execute if not clean
    if state.get('status') != "CLEAN":
        return {"output": "Blocked by Security Policy: PII Detected."}
    
    return {"output": f"Success: Processed via {state['selected_model']}"}
def hallucination_auditor_node(state):
    # Principal Feature: Post-generation compliance check
    output = state.get('output', "")
    if "internal_api" in output.lower():
        return {"status": "AUDIT_FAILED", "output": "Compliance Error: Internal Schema leaked."}
    return {"status": "AUDIT_PASSED"}

# Build the Graph
builder = StateGraph(AgentState)
builder.add_node("scrub", pii_scrubber_node)
builder.add_node("route", finops_router_node)
builder.add_node("execute", execution_node)
builder.add_node("audit", hallucination_auditor_node)

builder.set_entry_point("scrub")
builder.add_edge("scrub", "route")
builder.add_edge("route", "execute")
builder.add_edge("execute", "audit")
builder.add_edge("audit", END)

app_engine = builder.compile()