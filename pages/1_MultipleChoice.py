import streamlit as st

# 헤더 및 스타일
st.header('객관식 문제 :seedling:', divider='rainbow')

# 스타일 정의
st.markdown("""
    <style>
        .question-container {
            margin-bottom: 20px;
        }
        .question-container h3 {
            color: #4CAF50;
        }
        .radio-label {
            display: block;
            margin: 10px 0;
            font-size: 16px;
            color: #333;
        }
        .selected-answer {
            margin-top: 10px;
            font-size: 16px;
            color: #007ACC;
        }
        .stRadio {
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# 첫 번째 라디오 버튼
with st.container():
    st.markdown('<div class="question-container">', unsafe_allow_html=True)
    st.markdown("### 1. Streamlit 애플리케이션에서 데이터를 출력하기 위한 함수는 무엇인가요?", unsafe_allow_html=True)
    
    genre1 = st.radio(
        "",
        ["st.write", "st.write_stream", "Magic"],
        index=None,
        key='radio_key_1'
    )
    
    if genre1 != st.session_state.genre1:
        st.session_state.genre1 = genre1
    
    st.markdown(f'<div class="selected-answer">선택된 답: {genre1}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 두 번째 라디오 버튼
with st.container():
    st.markdown('<div class="question-container">', unsafe_allow_html=True)
    st.markdown("### 2. Streamlit 애플리케이션에서 시각화에 사용하는 함수는 무엇인가요?", unsafe_allow_html=True)
    
    genre2 = st.radio(
        "",
        ["st.line_chart", "st.bar_chart", "st.table"],
        index=None,
        key='radio_key_2'
    )
    
    if genre2 != st.session_state.genre2:
        st.session_state.genre2 = genre2

    st.markdown(f'<div class="selected-answer">선택된 답: {genre2}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
