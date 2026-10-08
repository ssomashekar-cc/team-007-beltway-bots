"""Educate page.

Visualizes sea turtle nesting activity and coastal data across Broward and
Brevard counties, complementing the policy/legal narrative on the Understand
page with charts and derived metrics instead of repeating it.
"""

import pandas as pd
import plotly.express as px
import streamlit as st

from components.styles import page_styles

st.markdown(page_styles("educate-content"), unsafe_allow_html=True)

with st.container(key="educate-content"):
    st.title("Educate")
    st.markdown(
        '<p class="page-intro">Visualizing how nesting density compares across '
        "Broward and Brevard counties—charts and trends to complement the "
        "policy and environmental snapshot on the Understand page.</p>",
        unsafe_allow_html=True,
    )

    # --- Turtle Metrics: nest density, a derived view not shown on Understand ---
    st.subheader("Nest Density: Comparing Coastline Pressure")

    nesting_df = pd.DataFrame(
        [
            {"County": "Broward", "2025 Nests": 3300, "Shoreline (mi)": 24.0},
            {"County": "Brevard", "2025 Nests": 53000, "Shoreline (mi)": 71.6},
        ]
    )
    nesting_df["Nests per Mile"] = (
        nesting_df["2025 Nests"] / nesting_df["Shoreline (mi)"]
    ).round(0)

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
        "5x the nest density per mile. See the Understand page for the "
        "underlying nest counts and shoreline figures. Figures are "
        "preliminary estimates and have not been independently verified."
    )

    # --- Historical activity: how nest management has differed over time -------
    st.subheader("Historical Nest Management")
    brevard_history, broward_history = st.columns(2)
    with brevard_history:
        st.markdown(
            """
            <div class="insight-card">
                <h3>Brevard: nests generally left in place</h3>
                <p>A darker overall lighting environment has historically let most
                nests stay where they're laid, rather than being relocated.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with broward_history:
        st.markdown(
            """
            <div class="insight-card">
                <h3>Broward: more historical relocation</h3>
                <p>Heavier urban lighting has historically meant more nest relocations
                and disoriented hatchlings. FWC has tightened relocation rules over
                time.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.caption(
        "Beach maintenance also differs: Broward's beaches see frequent renourishment "
        "and mechanical raking, typically requiring morning nest surveys and staked "
        "buffers beforehand. Brevard's renourishment projects are mostly managed for "
        "dune and shoreline protection."
    )

    # --- Tourism & Community Metrics (pending data integration) -----------------
    st.subheader("Tourism & Community Trends")
    st.info(
        "Visitor counts, tourism revenue, and census/population trend data "
        "haven't been integrated yet. These will be sourced from tourism "
        "boards, state tourism organizations, economic development agencies, "
        "and the U.S. Census Bureau."
    )

    # --- Comparison View ---------------------------------------------------------
    st.subheader("Comparison View: Target Municipality vs. Melbourne Beach")
    # TODO: guard clause - require a municipality to be selected (via
    # session_state, set on the home page), then render a side-by-side chart
    # once municipality_service/turtle_service provide per-city data.
    st.info("Select a municipality to compare its trends against Melbourne Beach.")
