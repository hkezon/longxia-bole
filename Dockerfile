# 基于轻量级 Python 镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制依赖清单并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制核心执行代码
COPY . .

# 启动龙虾哨兵执行体
CMD ["python", "main.py"]
