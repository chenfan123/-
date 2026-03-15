import streamlit as st
import time

# 获得一个标题
st.title("Hello World")

# write方法，可以在网页中渲染提供的内容
st.write("Hello World")

# 分隔符，用于分隔网页中的不同部分
st.divider()

# 聊天输入框
name = st.chat_input("输入你的问题")
st.write(name)

# 等待提示词
with st.spinner("user"):
    time.sleep(2)
    st.write("等待完成")
