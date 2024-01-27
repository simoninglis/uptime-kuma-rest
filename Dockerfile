# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables for Uptime Kuma API credentials and base URL
# These can be overridden by passing --env flags to docker run
ENV UPTIME_KUMA_USERNAME=username_here
ENV UPTIME_KUMA_PASSWORD=password_here
ENV UPTIME_KUMA_BASE_URL=https://your-uptime-kuma-instance.com
ENV PORT=5000

# Run app.py when the container launches
CMD ["python", "app.py"]
