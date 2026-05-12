REPAIR_PROMPT = """
你是SQL修复专家。

用户问题：
{user_query}

原始SQL：
{sql}

报错信息：
{error}

请修复SQL。

返回JSON：

{{
  "sql": "...",
  "reason": "..."
}}
"""