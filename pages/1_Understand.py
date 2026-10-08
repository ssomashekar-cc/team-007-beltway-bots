"""Understand sea turtle protections across Broward and Brevard counties."""

import streamlit as st

st.markdown(
    """
    <style>
    .st-key-understand-content {
        box-sizing: border-box;
        margin: 0 auto;
        max-width: 1280px;
        padding: 1.5rem clamp(1.25rem, 4vw, 3.5rem) 3rem;
        width: 100%;
    }
    .understand-intro {
        color: #476164;
        font-size: 1.08rem;
        margin: -0.5rem 0 1.5rem;
        max-width: 850px;
    }
    .insight-card {
        background: #fff;
        border: 1px solid #e3eae4;
        border-radius: 14px;
        height: 100%;
        padding: 1.15rem 1.25rem;
    }
    .insight-card h3 {
        color: #124447;
        font-size: 1.08rem;
        margin: 0 0 0.55rem;
    }
    .insight-card p {
        color: #476164;
        font-size: 0.96rem;
        line-height: 1.55;
        margin: 0;
    }
    .county-card {
        background: #0c393b;
        border-radius: 14px;
        color: #fff;
        height: 100%;
        padding: 1.3rem 1.4rem;
    }
    .county-card h3 {
        color: #d1e7bc;
        font-size: 1.15rem;
        margin: 0 0 0.65rem;
    }
    .county-card p {
        color: #f1f6f1;
        font-size: 0.96rem;
        line-height: 1.6;
        margin: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container(key="understand-content"):
    st.title("Understand")
    st.markdown(
        '<p class="understand-intro">A practical snapshot of sea turtle protections '
        "along Florida's Broward and Brevard coasts—for residents, community advocates, "
        "local leaders, and coastal businesses.</p>",
        unsafe_allow_html=True,
    )

    st.subheader("At a glance")
    metric_one, metric_two, metric_three, metric_four = st.columns(4)
    metric_one.metric("Broward cities reviewed", "8")
    metric_two.metric("Broward nesting season", "Mar 1 – Oct 31")
    metric_three.metric("Brevard nests · 2025", "≈53k")
    metric_four.metric("Broward nests · 2025", "≈3.3k")
    st.caption(
        "Nest estimates are from the supplied county comparison dataset summary; "
        "they are not independently verified or adjusted for shoreline length or survey effort."
    )

    st.subheader("What the local rules emphasize")
    lighting, season, beach_use = st.columns(3)
    with lighting:
        st.markdown(
            """
            <div class="insight-card">
                <h3>Keep the beach dark</h3>
                <p>All eight Broward city sources describe lighting protections. Rules
                commonly address shielding, windows, parking areas, and public lights
                near nesting beaches.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with season:
        st.markdown(
            """
            <div class="insight-card">
                <h3>Protect a longer season</h3>
                <p>The reviewed Broward city provisions generally cover March through
                October. Melbourne Beach, the project benchmark, starts May 1 and
                defines nighttime as 9 p.m. to 5 a.m.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with beach_use:
        st.markdown(
            """
            <div class="insight-card">
                <h3>Beach activity rules vary</h3>
                <p>Fort Lauderdale, Hallandale Beach, and Hillsboro Beach explicitly
                restrict some nighttime vehicle use or fires. The supplied sources
                do not specify these rules for every city.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.subheader("Two counties, different local landscapes")
    broward, brevard = st.columns(2)
    with broward:
        st.markdown(
            """
            <div class="county-card">
                <h3>Broward · urban coastline</h3>
                <p>Most beachfront is within cities, so local lighting protections are
                primarily set city by city. The supplied comparison describes a
                coordinated countywide monitoring program and frequent beach
                maintenance activity.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with brevard:
        st.markdown(
            """
            <div class="county-card">
                <h3>Brevard · extensive nesting coast</h3>
                <p>County, municipal, and federal jurisdictions share the coast.
                Monitoring is distributed among multiple permit holders; the supplied
                dataset summary reports substantially more nests in 2025 than
                Broward.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with st.expander("How to read this comparison"):
        st.write(
            "The Broward city summary is based on the supplied municipality-specific "
            "policy comparison. The broader Broward–Brevard overview includes "
            "general-knowledge statements and is not a verified statutory review. "
            "“Not specified” does not mean an activity is permitted. Confirm current "
            "ordinances, permit conditions, and dates with the relevant municipality, "
            "FWC, or FDEP before using this information for decisions."
        )
