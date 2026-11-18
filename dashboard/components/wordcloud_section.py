import streamlit as st

def render_wordcloud_section(
    title,
    company,
    selected_date,
    period_type,
    get_company_word_cloud,
    render_word_cloud,
):
    st.html(
        f"""
        <div style="
            font-size: 1.5rem;
            font-weight: 700;
            line-height: 1.3;
            margin-top: 0.5rem;
        ">
            {title}
        </div>
        """
    )

    data = get_company_word_cloud(
        company["id"],
        selected_date,
        period_type=period_type,
        text_type="content",
    )

    render_word_cloud(data["words"])