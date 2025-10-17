FROM python:3.11-slim
WORKDIR /app

# Copy app code into the image
COPY ../ /app/

# Install dependencies if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

CMD ["/bin/sh", "-c", "sleep 1 && exec bash"]
