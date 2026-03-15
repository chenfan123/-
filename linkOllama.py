from ollama import Client
import httpx


client = Client(
    host="http://127.0.0.1:11434",
    transport=httpx.HTTPTransport(retries=0),
)

resp = client.generate(
    model="qwen2.5:7b",
    prompt="你好"
)

print(resp["response"])
