# Use a Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy application code
COPY .. .

# Expose the API port
EXPOSE 5000

# Start Flask app
CMD ["python", "app.py"]
