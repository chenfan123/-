import streamlit as st
import time

if "count" not in st.session_state:
    st.session_state.count = 1


st.title("测试标题")

st.divider()

# 消息输入框
prompt = st.chat_input("输入你的问题")

# 消息容器
if (prompt):
    # 角色：user\assistant
    st.chat_message("user").markdown(prompt)

    # ai的回答
    with st.spinner("思考中..."):
        time.sleep(2)
        st.chat_message("assistant").markdown(
            f"思考完成，答案是：{st.session_state.count}")
        st.session_state.count += 1
