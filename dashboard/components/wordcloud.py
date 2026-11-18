from pathlib import Path

import matplotlib.pyplot as plt
from wordcloud import WordCloud

import streamlit as st

FONT_PATH = (
    Path(__file__).resolve().parent.parent
    / "fonts"
    / "SDSamliphopangcheTTFBasic.ttf"
)

def render_word_cloud(words: list[dict]):
    if not words:
        st.info("조회된 키워드가 없습니다.")
        return

    word_frequencies = {
        item["word"]: item["count"]
        for item in words
        if item["word"] and item["count"] > 0
    }

    if not word_frequencies:
        st.info("시각화할 키워드가 없습니다.")
        return

    wordcloud = WordCloud(
        font_path=str(FONT_PATH),
        width=1000,
        height=500,
        background_color="white",
        max_words=100,
        colormap="viridis",
    ).generate_from_frequencies(word_frequencies)

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")

    st.pyplot(fig, width="content")
    plt.close(fig)