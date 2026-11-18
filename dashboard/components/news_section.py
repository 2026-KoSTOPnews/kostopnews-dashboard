from datetime import date

import streamlit as st

def render_news_section(
    selected_date,
    company,
    render_news,
):
    st.html(
        """
        <div style="
            font-size: 1.5rem;
            font-weight: 700;
            line-height: 1.3;
            margin-bottom: 1rem;
        ">
            뉴스
        </div>
        """
    )

    # --------------------------------------------------
    # 뉴스
    # --------------------------------------------------
    render_news(
        company["id"],
        selected_date,
    )