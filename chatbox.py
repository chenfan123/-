import ollama
import streamlit as st
import time

# ollama 需要获取客户端
client = ollama.Client(host="http://127.0.0.1:11434")

# 初始化消息记录
if "messages" not in st.session_state:
    st.session_state.messages = []

# 绘制界面 - 添加标题
st.title('聊天室')
# 添加分割线
st.divider()
# 用户输入问题
prompt = st.chat_input('请输入你的问题')
# 判断，如果用户输入了内容，则开始工作
if prompt:
    # 将用户提问添加到历史记录中
    st.session_state.messages.append({"role": "user", "content": prompt})
    for message in st.session_state.messages:
        st.chat_message(message["role"]).markdown(message["content"])

    with st.spinner("思考中..."):
        time.sleep(1)
        response = client.chat(model="qwen2.5:7b", messages=[
            {"role": "user", "content": prompt}])
        # 从response中取出来message和content两个key
        st.session_state.messages.append(
            {"role": "assistant", "content": response.message.content})
        # 在页面中渲染ai的回答
        st.chat_message("assistant").markdown(response.message.content)
