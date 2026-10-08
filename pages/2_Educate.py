"""Educate page.

Visualizes sea turtle nesting activity and coastal data across Broward and
Brevard counties, complementing the policy/legal narrative on the Understand
page with charts and derived metrics instead of repeating it.

Sources: docs/broward_brevard_sea_turtle_statutory_comparison.md and
docs/broward-sea-turtle-policy-comparison 1.md.
"""

import pandas as pd
import plotly.express as px
import streamlit as st

from components.styles import page_styles

st.markdown(page_styles("educate-content"), unsafe_allow_html=True)

with st.container(key="educate-content"):
    st.title("Educate")
    st.markdown(
        '<p class="page-intro">Visualizing how nesting activity, coastline, and '
        "nighttime beach access compare across Broward and Brevard counties—"
        "charts and trends to complement the policy details on the Understand page.</p>",
        unsafe_allow_html=True,
    )

    # --- Turtle Metrics: nesting activity, shoreline, and density -----------
    st.subheader("Nesting Activity, By the Numbers")

    nesting_df = pd.DataFrame(
        [
            {"County": "Broward", "2025 Nests": 3300, "Shoreline (mi)": 24.0},
            {"County": "Brevard", "2025 Nests": 53000, "Shoreline (mi)": 71.6},
        ]
    )
    nesting_df["Nests per Mile"] = (
        nesting_df["2025 Nests"] / nesting_df["Shoreline (mi)"]
    ).round(0)

    nests_col, density_col = st.columns(2)
    with nests_col:
        fig_nests = px.bar(
            nesting_df,
            x="County",
            y="2025 Nests",
            color="County",
            color_discrete_map={"Broward": "#0c393b", "Brevard": "#6fa287"},
            title="2025 Nest Counts",
        )
        fig_nests.update_layout(showlegend=False, margin=dict(t=40, b=0))
        st.plotly_chart(fig_nests, use_container_width=True)
    with density_col:
        fig_density = px.bar(
            nesting_df,
            x="County",
            y="Nests per Mile",
            color="County",
            color_discrete_map={"Broward": "#0c393b", "Brevard": "#6fa287"},
            title="Nest Density (Nests per Shoreline Mile)",
        )
        fig_density.update_layout(showlegend=False, margin=dict(t=40, b=0))
        st.plotly_chart(fig_density, use_container_width=True)

    st.caption(
        "Brevard's coastline is roughly 3x longer than Broward's, but sees about "
        "5x the nest density per mile. Figures are from the supplied county "
        "comparison dataset summary and are not independently verified."
    )

    # --- Nighttime beach access ------------------------------------------------
    st.subheader("Nighttime Beach Access")
    broward_access, brevard_access = st.columns(2)
    with broward_access:
        st.markdown(
            """
            <div class="insight-card">
                <h3>Broward · limited night access</h3>
                <p>The supplied beach access hours comparison lists Broward parks
                with limited nighttime access.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with brevard_access:
        st.markdown(
            """
            <div class="insight-card">
                <h3>Brevard · no night access</h3>
                <p>The supplied beach access hours comparison lists Brevard parks
                with no nighttime access.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.caption(
        "This reflects general park access hours, not a turtle-specific law, "
        "but it affects how much nighttime beach disturbance is possible."
    )

    # --- Nesting season windows (visual timeline) -------------------------------
    st.subheader("Nesting Season Windows")
    season_df = pd.DataFrame(
        [
            {"Area": "Melbourne Beach (reference)", "Start": "2024-05-01", "Finish": "2024-10-31"},
            {"Area": "Broward cities (8 reviewed)", "Start": "2024-03-01", "Finish": "2024-10-31"},
            {"Area": "Brevard County ordinance", "Start": "2024-05-01", "Finish": "2024-10-31"},
        ]
    )
    fig_season = px.timeline(
        season_df,
        x_start="Start",
        x_end="Finish",
        y="Area",
        color="Area",
        color_discrete_map={
            "Melbourne Beach (reference)": "#d1e7bc",
            "Broward cities (8 reviewed)": "#0c393b",
            "Brevard County ordinance": "#6fa287",
        },
    )
    fig_season.update_yaxes(title=None)
    fig_season.update_layout(showlegend=False, margin=dict(t=10, b=0))
    st.plotly_chart(fig_season, use_container_width=True)
    st.caption(
        "Dates show the recurring annual nesting-season window (year shown is a "
        "placeholder for charting), not a single year's data."
    )

    # --- Tourism & Community Metrics (pending data integration) -----------------
    st.subheader("Tourism & Community Trends")
    st.info(
        "Visitor counts, tourism revenue, and census/population trend data "
        "haven't been integrated yet. Per PROJECT_HANDOFF.md, these will be "
        "sourced from tourism boards, state tourism organizations, economic "
        "development agencies, and the U.S. Census Bureau."
    )

    # --- Comparison View ---------------------------------------------------------
    st.subheader("Comparison View: Target Municipality vs. Melbourne Beach")
    # TODO: guard clause - require a municipality to be selected (via
    # session_state, set on the home page), then render a side-by-side chart
    # once municipality_service/turtle_service provide per-city data.
    st.info("Select a municipality to compare its trends against Melbourne Beach.")

    with st.expander("About this data"):
        st.write(
            "Nesting, shoreline, and beach-access figures come from the supplied "
            "Broward–Brevard county comparison dataset summary. See the "
            "Understand page for the underlying ordinance details and caveats."
        )
