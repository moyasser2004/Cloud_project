# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY script.py /app
COPY requirements.txt /app

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "script.py"]
