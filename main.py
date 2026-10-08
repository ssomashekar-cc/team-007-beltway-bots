"""App entrypoint.

Registers pages via st.Page/st.navigation. Once st.navigation() is called,
Streamlit stops auto-detecting pages/ by folder convention, so every page
must be explicitly listed below.

NOTE for home-page team: add your home page here, e.g.
    home_page = st.Page("pages/0_Home.py", title="Home", icon="🏠", default=True)
and include it as the first entry in the st.navigation([...]) list below so it
becomes the default landing page.
"""

import streamlit as st

understand_page = st.Page("pages/1_Understand.py", title="Understand", icon="🐢")
educate_page = st.Page("pages/2_Educate.py", title="Educate", icon="📊")
recommend_page = st.Page("pages/3_Recommend.py", title="Recommend", icon="💡")

pg = st.navigation(
    [
        # TODO(home-page branch): prepend home_page here and set default=True on it.
        understand_page,
        educate_page,
        recommend_page,
    ]
)

pg.run()
