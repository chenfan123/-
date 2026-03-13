import ollama

client = ollama.Client(host="http://localhost:11434")
# print("已连接 Ollama:", client)
# 列举模型
# print("模型列表:", client.list())
# 显示模型信息
# print(client.show('qwen2.5:3b'))
# 显示那些模型正在运行
# print(client.ps())

response = client.chat(model="qwen2.5:3b", messages=[
                       {"role": "user", "content": "你好"}])
print(response)
