import streamlit as st

st.header('Streamlit에 대해 알아보기 :sunglasses:', divider='rainbow')

st.subheader("write and magic")
st.markdown(""" :star: st.write 란? """)

# st.write 설명
st.markdown("""
`st.write`는 Streamlit 애플리케이션에서 데이터를 출력하기 위한 함수입니다. 이 함수는 다음과 같은 기능을 제공합니다

1. **텍스트 출력**: 문자열을 화면에 간단히 출력합니다.
   
   > :rainbow: 예제 코드
   ```python
   st.write('Hello, world!')
   

   
2. **데이터프레임 출력**: Pandas 데이터프레임을 표 형태로 화면에 표시합니다.
   ```python
   import pandas as pd
   df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
   st.write(df)

""")

st.markdown(""" :star: st.write_stream 란? """)

# st.write_stream 설명
st.markdown("""

`st.write_stream`은 Streamlit에서 생성기(generator), 반복 가능한 객체(iterable), 또는 스트림-like 시퀀스를 실시간으로 스트리밍하는 함수입니다. 이 함수는 시퀀스를 순회하면서 각 청크를 앱에 출력합니다. 문자열 청크는 타자기 효과로 표시되고, 다른 데이터 유형은 st.write를 사용하여 표시됩니다.

 > :rainbow: 예제 코드

```python
import streamlit as st
import pandas as pd
import time
import random

# 문자열 생성기 함수
def generate_strings():
    for i in range(5):
        yield f'타자기 효과로 표시되는 문자열 청크 {i+1}\n'
        time.sleep(1)  # 1초 간격으로 문자열 생성

# 데이터프레임 생성기 함수
def generate_dataframe():
    df = pd.DataFrame({
        'A': [random.randint(1, 10) for _ in range(5)],
        'B': [random.randint(1, 10) for _ in range(5)]
    })
    yield df

# 문자열 스트리밍
st.write("문자열 스트리밍 시작!")
st.write_stream(generate_strings())

# 데이터프레임 스트리밍
st.write("데이터프레임 스트리밍 시작!")
st.write_stream(generate_dataframe())

""")



