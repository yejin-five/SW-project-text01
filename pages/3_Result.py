import streamlit as st

# 시험 결과 헤더
st.header('시험 결과 :cherry_blossom:', divider='rainbow')

# 정답 설정
correct_answers = {
    'genre1': 'st.write',
    'genre2': 'st.line_chart',
    'subjective': 'hi'  # 주관식 정답
}

# 객관식 점수 계산
st.markdown("### :blossom: 객관식", unsafe_allow_html=True)

# 세션 상태에서 저장된 객관식 답변을 불러오기
if 'genre1' in st.session_state:
    user_answer1 = st.session_state.genre1
    st.write(f"1번 문항 저장된 답변: {user_answer1}")
else:
    user_answer1 = None
    st.write("1번 문항 저장된 답변이 없습니다.")

if 'genre2' in st.session_state:
    user_answer2 = st.session_state.genre2
    st.write(f"2번 문항 저장된 답변: {user_answer2}")
else:
    user_answer2 = None
    st.write("2번 문항 저장된 답변이 없습니다.")

# 객관식 점수 계산
objective_score = 0
if user_answer1 == correct_answers['genre1']:
    objective_score += 1
if user_answer2 == correct_answers['genre2']:
    objective_score += 1

# 객관식 점수 출력
st.markdown(f"""
    <div style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
        <h4 style="color:#fd8080; text-align: center;">객관식 점수: {objective_score} / 2</h4>
    </div>
""", unsafe_allow_html=True)

# 주관식 점수 계산
st.markdown("### :blossom: 주관식", unsafe_allow_html=True)

# 세션 상태에서 저장된 주관식 답변을 불러오기
if 'user_answer' in st.session_state:
    user_subjective_answer = st.session_state.user_answer
    st.write(f"주관식 문항 저장된 답변: {user_subjective_answer}")
else:
    user_subjective_answer = None
    st.write("주관식 문항 저장된 답변이 없습니다.")

# 주관식 점수 계산
subjective_score = 0
if user_subjective_answer and user_subjective_answer.strip().lower() == correct_answers['subjective'].lower():
    subjective_score += 1

# 주관식 점수 출력
st.markdown(f"""
    <div style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
        <h4 style="color:#fd8080; text-align: center;">주관식 점수: {subjective_score} / 1</h4>
    </div>
""", unsafe_allow_html=True)

# 총점 계산
total_score = objective_score + subjective_score

# 총점 출력
st.markdown(f"""
    <div style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
        <h4 style="color:#fd8080; text-align: center;">총점: {total_score} / 3</h4>
    </div>
""", unsafe_allow_html=True)

# 축하 메시지 표시
if total_score == 3:
    st.markdown("""
        <div style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9; text-align: center;">
            <h4 style="color:#32CD32;">축하합니다! 전부 정답입니다! 🎉</h4>
        </div>
    """, unsafe_allow_html=True)
