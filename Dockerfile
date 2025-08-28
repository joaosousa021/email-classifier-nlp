FROM python:3.11-slim

WORKDIR /app

ENV HF_HOME /app/.cache

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY download_models.py .
RUN python download_models.py

COPY . .

EXPOSE 7860

CMD ["gunicorn", "--workers", "1", "--threads", "2", "--timeout", "120", "--bind", "0.0.0.0:7860", "app:app"]