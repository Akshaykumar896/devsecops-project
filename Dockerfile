# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Run app
CMD ["python", "app.py"]
