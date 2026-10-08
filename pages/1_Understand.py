"""Understand page.

Helps users understand the current state of a selected municipality:
community profile, legal environment, and environmental/beach characteristics,
plus an AI-generated summary.

See PROJECT_HANDOFF.md for full context.
"""

import streamlit as st

st.title("Understand")

# TODO: guard clause - require a municipality to be selected (via session_state,
# set on the home page). Redirect/prompt the user if none is selected.

# --- Community Profile -----------------------------------------------------
# population, population growth, demographics, tourism statistics,
# conservation spending
st.header("Community Profile")

# --- Legal Environment -------------------------------------------------------
# wildlife protection laws, turtle protection ordinances, dark sky ordinances,
# lighting restrictions, noise ordinances, beach access regulations
st.header("Legal Environment")

# --- Environmental / Beach Characteristics ----------------------------------
# turtle nesting counts, historical turtle populations, beach characteristics,
# vehicle/bicycle access policies, beach access hours
st.header("Environmental & Beach Characteristics")

# --- AI-Generated Summary ----------------------------------------------------
# calls ai_service to produce a plain-English summary of the municipality,
# its laws, tourism environment, and strengths/weaknesses
st.header("AI-Generated Summary")
