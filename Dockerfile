# Use the official lightweight Python image.
FROM python:3.9-slim

# Copy local code to the container image.
WORKDIR /app
COPY . .

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Run the web service on container startup.
CMD ["python", "app.py"]
