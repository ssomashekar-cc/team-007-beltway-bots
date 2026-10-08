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
    .benchmark-callout {
        background: #eaf1e6;
        border-left: 5px solid #568267;
        border-radius: 0 12px 12px 0;
        color: #294d49;
        line-height: 1.6;
        margin: 1rem 0 1.5rem;
        padding: 1rem 1.25rem;
    }
    .benchmark-callout strong {
        color: #124447;
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
        "comparing Broward and Brevard to help residents, community advocates, "
        "local leaders, and coastal businesses understand the policy choices.</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="benchmark-callout">
            <strong>Brevard is the working gold-standard reference; Broward is the focus for action.</strong>
            Brevard's layered county, municipal, and federal approach informs proposed
            Broward policies intended to protect turtles while accommodating tourism.
            This is a model for comparison—not proof that policy alone explains nest
            counts or that tourism impacts have been measured.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("At a glance")
    metric_one, metric_two, metric_three = st.columns(3)
    metric_one.metric("Brevard nesting season", "May 1 – Oct 31")
    metric_two.metric("Brevard nests · 2025", "53,000")
    metric_three.metric("Broward nests · 2025", "3,300")
    st.caption(
        "The supplied overview describes Brevard's county ordinance as generally covering "
        "May–October; Broward city sources generally cover March–October. Nest estimates "
        "are approximate and are not adjusted for shoreline length or survey effort."
    )

    st.subheader("Broward recommendations, informed by Brevard's approach")
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
                <h3>Keep Broward's early-season protection</h3>
                <p>The reviewed Broward city provisions generally cover March through
                October, earlier than the May–October Brevard county season described
                in the overview. Keep the earlier start unless wildlife agencies advise
                otherwise.</p>
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

    st.subheader("Adapt the model to local conditions")
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
                <h3>Brevard · layered policy reference</h3>
                <p>County, municipal, and federal jurisdictions share the coast, with
                monitoring distributed among multiple permit holders. Its layered
                structure is a useful reference for Broward, whose beachfront rules are
                primarily city by city.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with st.expander("How to read this comparison"):
        st.write(
            "The Broward city summary is based on the supplied municipality-specific "
            "policy comparison. The broader Broward–Brevard overview includes "
            "general-knowledge statements and is not a verified statutory review. "
            "The nest totals do not show that policy differences caused different "
            "nest outcomes, and the supplied material does not measure tourism effects. "
            "“Not specified” does not mean an activity is permitted. Confirm current "
            "ordinances, permit conditions, and dates with the relevant municipality, "
            "FWC, or FDEP before using this information for decisions."
        )
