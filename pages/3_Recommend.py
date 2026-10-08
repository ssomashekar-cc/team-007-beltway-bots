"""Recommend page.

Helps decision makers determine possible policy changes by comparing a
selected municipality's laws against Melbourne Beach, FL, surfacing
AI-generated recommendations, and offering a mock policy simulator.

See PROJECT_HANDOFF.md for full context.
"""

import streamlit as st

st.title("Recommend")

# TODO: guard clause - require a municipality to be selected (via session_state,
# set on the home page). Redirect/prompt the user if none is selected.

# --- Legal Comparison ---------------------------------------------------------
# compare target municipality laws vs. Melbourne Beach laws:
# matches, differences, missing protections, additional restrictions
st.header("Legal Comparison: Target Municipality vs. Melbourne Beach")

# --- AI Recommendations --------------------------------------------------------
# calls ai_service to generate policy recommendations explaining potential
# conservation benefits, possible tourism impacts, and alignment with
# best practices
st.header("AI Recommendations")

# --- Scenario / Policy Simulator ------------------------------------------------
# mock policy simulation (MVP scope)
st.header("Scenario Simulator")
