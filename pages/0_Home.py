"""Landing page for the coastal conservation app."""

import base64
from pathlib import Path

import streamlit as st

image_path = Path(__file__).resolve().parents[1] / "assets" / "sea-turtle-hero.jpg"
image_data = base64.b64encode(image_path.read_bytes()).decode("ascii")

st.markdown(
    f"""
    <style>
    .st-key-site-header {{
        background: transparent;
    }}
    .home-hero {{
        align-items: center;
        background-image:
            linear-gradient(90deg, rgb(5 39 42 / 83%) 0%, rgb(5 39 42 / 53%) 47%, rgb(5 39 42 / 8%) 100%),
            url("data:image/jpeg;base64,{image_data}");
        background-position: center 42%;
        background-size: cover;
        border-radius: 0 0 1.5rem 1.5rem;
        display: flex;
        min-height: 570px;
        margin-top: -5.7rem;
        overflow: hidden;
    }}
    .hero-copy {{
        color: #fff;
        max-width: 760px;
        padding: 9.5rem 6.5rem 5rem;
    }}
    .hero-kicker, .blurb-kicker {{
        color: #c2e5b2;
        font-size: 0.75rem;
        font-weight: 800;
        letter-spacing: 0.2em;
        margin: 0 0 1rem;
        text-transform: uppercase;
    }}
    .hero-copy h1 {{
        color: #fff;
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(2.8rem, 6vw, 5.7rem);
        font-weight: 500;
        letter-spacing: -0.045em;
        line-height: 0.98;
        margin: 0 0 1.25rem;
        max-width: 720px;
    }}
    .hero-copy p {{
        color: rgb(255 255 255 / 92%);
        font-size: 1.12rem;
        line-height: 1.7;
        margin: 0;
        max-width: 570px;
    }}
    .homepage-blurb {{
        margin: 0 auto;
        max-width: 880px;
        padding: 3.5rem 1.5rem 1rem;
        text-align: center;
    }}
    .blurb-kicker {{
        color: #55876a;
        margin-bottom: 0.6rem;
    }}
    .homepage-blurb p:last-child {{
        color: #375052;
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(1.2rem, 2.1vw, 1.65rem);
        line-height: 1.55;
        margin: 0 auto;
    }}
    .image-credit {{
        color: #f2f8f2;
        font-size: 0.7rem;
        margin: 0.9rem 0 0 1.4rem;
        opacity: 0.82;
    }}
    .image-credit a {{
        color: inherit;
    }}
    @media (max-width: 700px) {{
        .home-hero {{
            background-position: 56% center;
            min-height: 500px;
            margin-top: -4.8rem;
        }}
        .hero-copy {{
            padding: 9rem 1.5rem 3.5rem;
        }}
        .hero-copy p {{
            font-size: 1rem;
        }}
        .homepage-blurb {{
            padding: 2.5rem 0.75rem 0.5rem;
        }}
        .image-credit {{
            margin-left: 0;
        }}
    }}
    </style>
    <section class="home-hero" aria-label="Sea turtle swimming in the ocean">
        <div class="hero-copy">
            <p class="hero-kicker">For thriving coasts and wildlife</p>
            <h1>Healthy shores.<br>Hopeful futures.</h1>
            <p>Explore how local choices can help coastal communities and sea turtles thrive together.</p>
        </div>
    </section>
    <p class="image-credit">
        Photo: <a href="https://commons.wikimedia.org/wiki/File:A_Sea_Turtle_in_Hawaii.jpg"
        target="_blank" rel="noreferrer">Chloekwak / Wikimedia Commons</a>
        · <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noreferrer">CC BY-SA 4.0</a>
    </p>
    <section class="homepage-blurb">
        <p class="blurb-kicker">Coastal conservation starts here</p>
        <p>Every coastline has its own story. Understand your community, explore the trends shaping its shores, and find thoughtful ways to protect the places sea turtles call home.</p>
    </section>
    """,
    unsafe_allow_html=True,
)
