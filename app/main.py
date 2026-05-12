import  json
from app.config import OPENAI_MODEL, TEMPERATURE
from app.llm.deepseek_client import llm
from app.prompts import repair_prompt
from app.prompts.repair_prompt import REPAIR_PROMPT
from app.prompts.sql_prompt import SYSTEM_PROMPT
from app.tools.sql_tool import sql_excute_tool

#用户问题
user_query = "查询所有用户"

# =========================
# AI 优化/完善代码
state = {
    "user_query": user_query,
    "sql": "",
    "error": "",
    "retry_count": 0,
    "result": None
}

# =========================

#生成sql
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user",
        "content":user_query
    }
]

response = llm.chat.completions.create(
    model=OPENAI_MODEL,
    messages=messages,
    temperature=TEMPERATURE,
)

content = response.choices[0].message.content

print("==================llm 返回内容================:" )
print(content)

# =========================
# JSON 解析保护 -------- AI 优化/完善代码
try:
    data = json.loads(content)
except Exception as e:
    print("JSON  解析失败")
    print(e)
    exit()   # 解析失败直接退出整个程序；不再往下走了

# =========================

#获取sql
state["sql"] = data["sql"]
state["sql"] = "SELECT * FROM user LIMIT 100"
# print(state["sql"])
re_conut = 0

# =========================
# SQL 安全校验----------AI 优化/完善代码

danger_sql = ["delete", "update", "drop", "truncate"]

for keyword in danger_sql:
    if keyword in state["sql"].lower():
        raise Exception(f"危险 SQL：{state['sql']}")
# =========================

while state["retry_count"]<3:
    print("\n=================当前SQL=================")
    print(state["sql"])
    result = sql_excute_tool(state["sql"])
    print("\n================result 内容 ================")
    print(result)
    #保存结果
    state["result"] =  result
    if  result["success"]:
        print("\n===============执行成功===============")
        # json.dump(result["data"],ensure_ascii=False, indent=2)
        print(json.dumps(result["data"],ensure_ascii=False, indent=2))
        break

    #失败的话
    state["error"] = result["error"]
    print("\n==============执行 SQL 失败============")
    print(state["error"])

    #开始修复 sql
    repair_messages = [
        {
            "role": "system",
            "content": REPAIR_PROMPT.format(
                user_query=state["user_query"],
                sql = state["sql"],
                error = state["error"]
            )
        }
    ]
    repair_response  = llm.chat.completions.create(
                model=OPENAI_MODEL,
                messages=repair_messages,
                temperature=TEMPERATURE,
    )
    repair_content = repair_response.choices[0].message.content
    print("\n========== 修复后的返回 ==========")
    print(repair_content)

    # 去掉 markdown
    repair_content = repair_content.replace("```json", "")
    repair_content = repair_content.replace("```", "")
    repair_content = repair_content.strip()
    print("\n========== 去掉 markdown的返回 ==========")
    print(repair_content)
    # =========================
    # JSON 解析保护 -------- AI 优化/完善代码
    try:
        data = json.loads(repair_content)
    except Exception as e:
        print("JSON  解析失败")
        print(e)
        exit()  # 解析失败直接退出整个程序；不再往下走了
    # =========================
    """ 报错：
    ========== 修复后的返回 ==========markdown 格式
    ```json
    {
      "sql": "SELECT * FROM users LIMIT 100",
      "reason": "原始SQL中表名'user'在数据库'agent_demo'中不存在；根据常见命名规范（复数形式）及错误提示，实际存在的用户表更可能是'users'。已将表名修正为'users'。"
    }
    ```
    JSON  解析失败"""

    state["sql"] = data["sql"]
    state["retry_count"] += 1

# =========================
# 最终失败 --------- ai 优化/完善代码
if not state["result"]["success"]:
    print("\n========== Agent 最终失败 ==========")
    print("超过最大重试次数")
# =========================

#         if result["success"]:
#             break
#
#         error_msg = result["error"]
#         print(error_msg)
#         repair_messages = [
#             {
#                 "role": "system",
#                 "content": REPAIR_PROMPT.format(
#                     user_query=user_query,
#                     sql = sql,
#                     error = error_msg
#                 )
#             }
#         ]
#         repair_response  = llm.chat.completions.create(
#             model=OPENAI_MODEL,
#             messages=repair_messages,
#             temperature=TEMPERATURE,
#         )
#         content = repair_response.choices[0].message.content
#         print(content)
#
#         data = json.loads(content)
#
#         sql = data["sql"]
#
#         retry_count += 1
#
#
#
# result = sql_excute_tool(sql)
#
# if not result["success"]:
#
#
#     while re_conut < 3:
#         result = sql_excute_tool(sql)
#         if result["success"]:
#             break
#
#         error_msg = result["error"]
#         print(error_msg)
#         repair_messages = [
#             {
#                 "role": "system",
#                 "content": REPAIR_PROMPT.format(
#                     user_query=user_query,
#                     sql = sql,
#                     error = error_msg
#                 )
#             }
#         ]
#         repair_response  = llm.chat.completions.create(
#             model=OPENAI_MODEL,
#             messages=repair_messages,
#             temperature=TEMPERATURE,
#         )
#         content = repair_response.choices[0].message.content
#         print(content)
#
#         data = json.loads(content)
#
#         sql = data["sql"]
#
#         retry_count += 1


