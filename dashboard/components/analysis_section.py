import streamlit as st

def render_sentiment_section(
    selected_date,
    company,
    get_company_sentiment,
    get_company_keywords,
    get_company_word_cloud,
    render_wordcloud_section,
    render_sentiment_chart,
    render_keywords_chart,
    render_word_cloud,
):
    st.html(
        """
        <div style="
            font-size: 1.8rem;
            font-weight: 700;
            line-height: 1.3;
            margin-top: 0.5rem;
        ">
            뉴스 분석 결과
        </div>
        """
    )

    # --------------------------------------------------
    # 감성 분석 및 주요 키워드 조회
    # --------------------------------------------------
    tab_daily, tab_weekly, tab_monthly = st.tabs(
        ["일간 분석", "주간 분석", "월간 분석"]
    )

    # --------------------------------------------------
    # 분석 데이터 조회
    # --------------------------------------------------
    sentiment = get_company_sentiment(
        company["id"],
        selected_date,
    )

    keywords = get_company_keywords(
        company["id"],
        selected_date,
    )

    # --------------------------------------------------
    # 일간 분석
    # --------------------------------------------------
    with tab_daily:
        render_sentiment_chart(
            "일간 감성 분석",
            sentiment["daily"],
        )

        st.write("")

        col1, col2 = st.columns([1, 1])

        with col1:
            render_keywords_chart(
                "일간 주요 키워드",
                keywords["daily"]["keywords"],
            )

        with col2:
            render_wordcloud_section(
                "일간 키워드 시각화",
                company,
                selected_date,
                "daily",
                get_company_word_cloud,
                render_word_cloud,
            )

    # --------------------------------------------------
    # 주간 분석
    # --------------------------------------------------
    with tab_weekly:
        render_sentiment_chart(
            "주간 감성 분석",
            sentiment["weekly"],
        )

        st.write("")

        col1, col2 = st.columns([1, 1])

        with col1:
            render_keywords_chart(
                "주간 주요 키워드",
                keywords["weekly"]["keywords"],
            )

        with col2:
            render_wordcloud_section(
                "주간 키워드 시각화",
                company,
                selected_date,
                "weekly",
                get_company_word_cloud,
                render_word_cloud,
            )

    # --------------------------------------------------
    # 월간 분석
    # --------------------------------------------------
    with tab_monthly:
        render_sentiment_chart(
            "월간 감성 분석",
            sentiment["monthly"],
        )

        st.write("")

        col1, col2 = st.columns([1, 1])

        with col1:
            render_keywords_chart(
                "월간 주요 키워드",
                keywords["monthly"]["keywords"],
            )

        with col2:
            render_wordcloud_section(
                "월간 키워드 시각화",
                company,
                selected_date,
                "monthly",
                get_company_word_cloud,
                render_word_cloud,
            )