# Use official Python image
FROM python:3.11-slim

WORKDIR /app

# Copy requirements and source code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask

EXPOSE 8080

CMD ["python", "server.py"]
