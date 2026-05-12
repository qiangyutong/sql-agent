from dotenv import load_dotenv
import os

load_dotenv()

#AI 配置
OPENAI_MODEL = str(os.getenv("OPENAI_MODEL"))
TEMPERATURE = float(os.getenv("TEMPERATURE"))
OPENAI_MODEL_URI=str(os.getenv("OPENAI_MODEL_URI"))
OPENAI_API_KEY=str(os.getenv("OPENAI_API_KEY"))

#mysql_配置
MYSQL_HOST=os.getenv("MYSQL_HOST")  # 数据库主机地址
MYSQL_PORT=int(os.getenv("MYSQL_PORT")) # 端口，默认3306
MYSQL_USER=os.getenv("MYSQL_USER")  # 数据库用户名
MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD")  # 密码
MYSQL_DATABASE=os.getenv("MYSQL_DATABASE")  # 要操作的数据库名
MYSQL_CHARSET=os.getenv("MYSQL_CHARSET")  # 字符集