"""App entrypoint and shared page navigation."""

import streamlit as st

st.set_page_config(
    page_title="Coastal Conservation",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="collapsed",
)

home_page = st.Page("pages/0_Home.py", title="Home", default=True)
understand_page = st.Page("pages/1_Understand.py", title="Understand")
educate_page = st.Page("pages/2_Educate.py", title="Educate")
recommend_page = st.Page("pages/3_Recommend.py", title="Recommend")

pages = st.navigation(
    [
        home_page,
        understand_page,
        educate_page,
        recommend_page,
    ],
    position="hidden",
)

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: #f7f8f4;
    }
    header[data-testid="stHeader"] {
        background: transparent;
        pointer-events: none;
    }
    header[data-testid="stHeader"] [data-testid="stToolbar"] {
        display: none;
    }
    [data-testid="stMainBlockContainer"] {
        max-width: 100% !important;
        padding: 0.75rem 0 0 !important;
    }
    .st-key-site-header {
        background: #0c393b;
        border-radius: 1rem 1rem 0 0;
        position: relative;
        z-index: 2;
        padding: 0.75rem clamp(1rem, 5vw, 5rem);
    }
    .st-key-site-header [data-testid="stHorizontalBlock"] {
        align-items: center;
    }
    .st-key-brand-home-link [data-testid="stPageLink-NavLink"] {
        background: transparent !important;
        border-color: transparent !important;
        border-radius: 0 !important;
        justify-content: flex-start;
        padding: 0;
        text-decoration: none;
        width: 260px;
    }
    .st-key-brand-home-link [data-testid="stPageLink-NavLink"] p {
        color: #fff !important;
        font-family: Arial, sans-serif !important;
        font-size: 1.05rem !important;
        font-weight: 800 !important;
        letter-spacing: 0.16em !important;
        line-height: 1.2 !important;
        text-decoration: none !important;
        text-transform: uppercase !important;
        white-space: normal !important;
    }
    .st-key-brand-home-link [data-testid="stPageLink-NavLink"]:hover p {
        color: #fff !important;
        text-decoration: none !important;
    }
    .st-key-site-header [data-testid="stPageLink"] {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    .st-key-site-header [data-testid="stPageLink-NavLink"] {
        border: 1px solid transparent;
        border-radius: 999px;
        color: #fff;
        display: flex;
        justify-content: center;
        font-family: Arial, sans-serif;
        font-size: 1.2rem;
        font-weight: 800;
        letter-spacing: 0.16em;
        padding: 0.25rem 0.5rem;
        text-decoration: none;
        text-transform: uppercase;
        white-space: nowrap;
    }
    .st-key-site-header [data-testid="stPageLink-NavLink"] p {
        color: #fff !important;
        font-family: Arial, sans-serif !important;
        font-size: 1.2rem !important;
        font-weight: 800 !important;
        letter-spacing: 0.16em !important;
    }
    .st-key-site-header [data-testid="stPageLink-NavLink"]:hover {
        background: transparent;
        border-color: transparent;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container(key="site-header"):
    brand, nav = st.columns([1.3, 2.5], vertical_alignment="top")
    with brand:
        with st.container(key="brand-home-link"):
            st.page_link(home_page, label="Coastal Conservation")
    with nav:
        understand_link, educate_link, recommend_link = st.columns(3, vertical_alignment="top")
        with understand_link:
            st.page_link(understand_page, label="Understand", use_container_width=True)
        with educate_link:
            st.page_link(educate_page, label="Educate", use_container_width=True)
        with recommend_link:
            st.page_link(recommend_page, label="Recommend", use_container_width=True)

pages.run()
