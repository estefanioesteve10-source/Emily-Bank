FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python", "main.py"]
# ... (suas outras linhas)
ENV PYTHONUNBUFFERED=1
# ...
