import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Hello DXP!", page_icon="✨")

# 헤더
st.title("🐣  DXP PoC Mini App")
st.caption("귀엽고 작동만 잘하는 Streamlit 샘플")

# 인풋 → 즉시 반응
name = st.text_input("What's your name?", "종호")
clicked = st.button("Say hi!")

# 아웃풋
if clicked:
    st.success(f"안녕하세요, **{name}**! 🚀")
    st.write(f"현재 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 사이드바
st.sidebar.info("🔧 Powered by Streamlit")
