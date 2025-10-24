# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy producer script
COPY Streaming_Producer.py .

# Install kafka-python
RUN pip install --no-cache-dir kafka-python

# Run the producer
CMD ["python", "Streaming_Producer.py"]
