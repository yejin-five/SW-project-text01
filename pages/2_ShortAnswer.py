import streamlit as st

# 주관식 문제 입력 화면
st.header('주관식 문제 :seedling:', divider='rainbow')

# 문제 설명
st.write("### 1. Streamlit 애플리케이션에서 데이터를 출력하기 위한 함수는 무엇인가요?")

# 스타일 정의
st.markdown("""
    <style>
        .input-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .input-container input {
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            width: 100%;
            max-width: 500px;
            font-size: 16px;
            margin-bottom: 10px;
        }
        .input-container button {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }
        .input-container button:hover {
            background-color: #45a049;
        }
        .feedback {
            margin-top: 20px;
            font-size: 16px;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# 사용자 입력 컨테이너
with st.container():
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    title = st.text_input("입력한 답", "정답을 입력하세요.")
    if st.button('제출'):
        st.session_state.user_answer = title
        st.markdown("<div class='feedback'>답변이 저장되었습니다.</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
