
import pymysql

from app.config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, MYSQL_CHARSET
from app.prompts.sql_prompt import SYSTEM_PROMPT


def sql_excute_tool(sql):
    try:
        connection = pymysql.connect(
            host=MYSQL_HOST,  # 数据库主机地址
            port=MYSQL_PORT,  # 端口，默认3306
            user=MYSQL_USER,  # 数据库用户名
            password=MYSQL_PASSWORD,  # 密码
            database=MYSQL_DATABASE,  # 要操作的数据库名
            charset=MYSQL_CHARSET  # 字符集
        )
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        cursor.execute(sql)
        # 获取所有结果
        results = cursor.fetchall()
        connection.close()
        return {
            "success": True,
            "data": results
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
