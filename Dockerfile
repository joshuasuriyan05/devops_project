FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app
COPY templates/ ./templates
COPY static/ ./static

EXPOSE 8080
CMD ["python", "app/app.py"]
