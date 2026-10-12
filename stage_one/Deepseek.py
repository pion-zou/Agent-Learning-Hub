import os
from openai import OpenAI

# client = OpenAI(
#     api_key=os.environ['DEEPSEEK_API_KEY'],
#     base_url="https://api.deepseek.com"
# )
#
# response = client.chat.completions.create(
#     model="deepseek-flash",
#     messages=[
#         {"role":"system","content":"你是一个有用的编程助手"},
#         {"role":"user","content":"Python学AI好吗?"}
#     ],
#     stream=False,
#     reasoning_effort="high",
#     extra_body={"thinking":{"type":"enabled"}}
# )
#
# print(response.choices[0].message.content)

import os
from openai import OpenAI

client = OpenAI(api_key=os.environ['DEEPSEEK_API_KEY'],base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role":"system","content":"你是一个小学老师"},
        {"role":"user","content":"福田最好的小学是哪一间"}
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking":{"type":"disabled"}}
)

print(response.choices[0].message.content)