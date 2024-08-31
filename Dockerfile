# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variable to avoid Python buffering
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "main.py"]
