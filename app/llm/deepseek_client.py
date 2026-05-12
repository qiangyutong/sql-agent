

from dotenv import load_dotenv
from openai import OpenAI

from app.config import OPENAI_MODEL_URI, OPENAI_API_KEY

llm = OpenAI(
    base_url=OPENAI_MODEL_URI,
    api_key=OPENAI_API_KEY,
)

# response = llm.chat.completions.create(
#     model=os.getenv("OPENAI_MODEL"),
#     messages=[
#         {"role":"user","content":"你好"}
#     ]
# )

# print(response.choices)
# print(response.choices[0])
# print(response.choices[0].message)
# print(response.choices[0].message.content)