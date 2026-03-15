import streamlit as st
import time

if "count" not in st.session_state:
    st.session_state.count = 1

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("测试标题")
st.divider()

# 消息输入框
prompt = st.chat_input("输入你的问题")

# 1. 角色 2. 消息[{role: "user", content: "你好"}, {role: "assistant", content: "你好"}]

# 消息容器
if (prompt):
    # 记录用户消息
    st.session_state.messages.append({"role": "user", "content": prompt})

    for messgae in st.session_state.messages:
        st.chat_message(messgae["role"]).markdown(messgae["content"])
    with st.spinner("思考中..."):
        time.sleep(2)
        response = f"思考完成，答案是：{st.session_state.count}"
        st.session_state.messages.append(
            {"role": "assistant", "content": response})
        st.session_state.count += 1
        # 把ai回答渲染到页面
        st.chat_message("assistant").markdown(
            response)
