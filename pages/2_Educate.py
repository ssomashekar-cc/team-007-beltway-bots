"""Educate page.

Helps users visualize conservation and economic trends for a selected
municipality, including a side-by-side comparison against Melbourne Beach, FL.

See PROJECT_HANDOFF.md for full context.
"""

import streamlit as st

st.title("Educate")

# TODO: guard clause - require a municipality to be selected (via session_state,
# set on the home page). Redirect/prompt the user if none is selected.

# --- Turtle Metrics -----------------------------------------------------------
# nest count trends, population trends, historical activity
st.header("Turtle Metrics")

# --- Tourism Metrics -----------------------------------------------------------
# visitor counts, tourism revenue, seasonal trends
st.header("Tourism Metrics")

# --- Community Metrics ---------------------------------------------------------
# population growth, census trends
st.header("Community Metrics")

# --- Comparison View ------------------------------------------------------------
# side-by-side: target municipality vs. Melbourne Beach, FL
st.header("Comparison View: Target Municipality vs. Melbourne Beach")
