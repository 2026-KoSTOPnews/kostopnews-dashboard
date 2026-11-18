from datetime import date

import streamlit as st

def render_date_selector():
    st.html(
        """
        <div style="
            font-size: 1.8rem;
            font-weight: 700;
            line-height: 1.3;
            margin-top: 0.5rem;
        ">
            분석 날짜 선택
        </div>
        """
    )

    if "selected_date" not in st.session_state:
        st.session_state.selected_date = date.today()

    return st.date_input(
        " ",
        key="selected_date",
        label_visibility="collapsed",
    )