# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install Git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy everything, including the .env file
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask application port
EXPOSE 3656

# Start the application
CMD ["python", "app.py"]
