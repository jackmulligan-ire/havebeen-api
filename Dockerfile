FROM python:3.10 as base

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY /app .

EXPOSE 8080

FROM base as primary

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

FROM base as debugger

RUN pip install debugpy

CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]