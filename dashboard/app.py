import streamlit as st

from api import get_companies, get_company_sentiment, get_company_keywords, get_company_word_cloud

from components.company_selector import render_company_selector
from components.sentiment import render_sentiment_chart
from components.news import render_news
from components.keywords import render_keywords_chart
from components.wordcloud import render_word_cloud
from components.wordcloud_section import render_wordcloud_section
from components.analysis_section import render_sentiment_section
from components.news_section import render_news_section
from components.date_selector import render_date_selector

st.set_page_config(
    page_title="News Analysis",
    page_icon="📰",
    layout="wide",
)

st.html(
    """
    <div style="
        font-size: 2.5rem;
        font-weight: 700;
        line-height: 1.5;
        margin-bottom: 1.5rem;
    ">
        📰 KoSTOPnews | 기업별 뉴스 분석
    </div>
    """
)

# --------------------------------------------------
# 기업 선택
# --------------------------------------------------
companies = get_companies()
company = render_company_selector(companies)

st.write("")

# --------------------------------------------------
# 날짜 선택
# --------------------------------------------------
selected_date = render_date_selector()

st.write("")
st.divider()

# --------------------------------------------------
# 기사 분석 결과
# --------------------------------------------------
render_sentiment_section(
    selected_date,
    company,
    get_company_sentiment,
    get_company_keywords,
    get_company_word_cloud,
    render_wordcloud_section,
    render_sentiment_chart,
    render_keywords_chart,
    render_word_cloud,
)

st.write("")
st.divider()

# --------------------------------------------------
# 뉴스
# --------------------------------------------------
render_news_section(
    selected_date,
    company,
    render_news,
)