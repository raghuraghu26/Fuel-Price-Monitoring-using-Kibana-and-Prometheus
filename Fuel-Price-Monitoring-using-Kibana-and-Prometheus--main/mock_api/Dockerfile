FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY mock_api.py .

EXPOSE 8000

CMD ["python", "mock_api.py"]