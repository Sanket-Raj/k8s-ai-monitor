# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependencies first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the agent logic
COPY analyzer.py .

# Run the analyzer unbuffered (so logs show up immediately in K8s)
CMD ["python", "-u", "analyzer.py"]