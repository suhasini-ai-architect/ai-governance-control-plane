import streamlit as st
from engine import app_engine

st.set_page_config(page_title="Guardian-Mesh AI Governance", layout="wide")

# Persistent State for ROI Tracking
if 'total_saved' not in st.session_state:
    st.session_state.total_saved = 2450.00
if 'queries_handled' not in st.session_state:
    st.session_state.queries_handled = 0

st.title("🛡️ Guardian-Mesh: Enterprise AI Control Plane")
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Control Plane Input")
    user_query = st.text_area("Analyze Prompt:", placeholder="Try a PII violation or a complex architecture question...")
    
    if st.button("Execute Secure Route"):
        st.session_state.queries_handled += 1
        
        # Run Graph
        result = app_engine.invoke({"user_input": user_query, "risk_score": 0.0})
        
        # Update ROI (Simulated)
        if result.get('selected_model') == "ollama/llama3.2":
            st.session_state.total_saved += 0.15 # Save 15 cents per local call
        
        with col2:
            st.subheader("Governance Audit Trail")
            
            # 1. Define the 'Red Flag' conditions
            is_blocked = result.get('status') == "FLAGGED" or result.get('risk_score', 0) > 0
            is_audit_fail = result.get('status') == "AUDIT_FAILED"
            
            # 2. UI Logic: Check for blocks FIRST
            if is_blocked:
                st.error("🛑 SECURITY VIOLATION: PII DETECTED")
                st.warning(result.get('output')) # This shows the "Blocked by Security Policy" message
                st.info(f"Safe Version: {result.get('user_input')}")
                
            elif is_audit_fail:
                st.error("⚠️ COMPLIANCE VIOLATION: AUDIT FAILED")
                st.info(result.get('output'))
                
            else:
                st.success("✅ APPROVED: ROUTING SECURE")
                st.info(result.get('output'))
            
            # 3. The Technical Trace
            with st.expander("Architectural Trace (JSON)"):
                st.json(result)
# Sidebar with Live ROI
st.sidebar.header("System Health")
st.sidebar.metric("Security Posture", "STRICT")
st.sidebar.metric("Cost Savings (MTD)", f"${st.session_state.total_saved:,.2f}", delta="+ $0.15")
st.sidebar.write(f"Total Queries Audited: {st.session_state.queries_handled}")