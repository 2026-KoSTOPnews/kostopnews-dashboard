import streamlit as st

def render_company_selector(companies):
    if not companies:
        st.warning("등록된 기업이 없습니다.")
        st.stop()

    st.html(
        """
        <div style="
            font-size: 1.8rem;
            font-weight: 700;
            line-height: 1.3;
            margin-top: 0.5rem;
        ">
            분석 기업 선택
        </div>
        """
    )

    # 최초 선택 기업 설정
    company_ids = [item["id"] for item in companies]

    if st.session_state.get("selected_company_id") not in company_ids:
        st.session_state.selected_company_id = companies[0]["id"]

    # 버튼 스타일
    st.markdown(
        """
        <style>
        div.stButton > button {
            border: 1.5px solid #222222;
            border-radius: 15px;
            font-size: 1.1rem;
            min-height: 3.2rem;
            transition: all 0.2s ease;
        }
        
        /* 선택되지 않은 버튼 */
        div.stButton > button[kind="secondary"] {
            background-color: #FFFFFF;
            color: #333333;
            border-color: #222222;
        }
        
        /* 선택된 버튼 */
        div.stButton > button[kind="primary"] {
            background-color: #FF4B4B !important;
            color: #FFFFFF !important;
            border-color: #FF4B4B !important;
            font-weight: 700 !important;
        }
        
        div.stButton > button[kind="primary"] p {
            font-weight: 700 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 기업 버튼 배치
    columns = st.columns(len(companies))

    for i, company_item in enumerate(companies):
        with columns[i]:
            is_selected = (
                st.session_state.selected_company_id
                == company_item["id"]
            )

            if st.button(
                company_item["name"],
                key=f"company_{company_item['id']}",
                use_container_width=True,
                type="primary" if is_selected else "secondary",
            ):
                st.session_state.selected_company_id = company_item["id"]
                st.rerun()

    return next(
        item for item in companies
        if item["id"] == st.session_state.selected_company_id
    )