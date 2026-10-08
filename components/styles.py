"""Shared design tokens and CSS snippets for the Understand/Educate/Recommend pages.

Centralizing these here keeps the page-level files focused on content and
avoids copy-pasting the same stylesheet across pages.
"""

# Shared card/typography classes reused by any page's content.
CARD_STYLES = """
.page-intro {
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
"""


def page_container_css(container_key: str) -> str:
    """CSS for the outer max-width/padding wrapper around a page's content.

    Each page wraps its body in `st.container(key=container_key)`; this
    returns the matching `.st-key-<container_key>` rule.
    """
    return f"""
    .st-key-{container_key} {{
        box-sizing: border-box;
        margin: 0 auto;
        max-width: 1280px;
        padding: 1.5rem clamp(1.25rem, 4vw, 3.5rem) 3rem;
        width: 100%;
    }}
    """


def page_styles(container_key: str) -> str:
    """Full <style> block (container wrapper + shared cards) for a page."""
    return f"<style>{page_container_css(container_key)}{CARD_STYLES}</style>"
