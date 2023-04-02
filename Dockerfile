# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Install the dependencies with --no-cache-dir so it wont download the flask app here  ~/.cache/pip
RUN pip install flask

# Copy the Flask project files into the container
COPY WorldOfGames/MainScores.py .
COPY Utils.py .

# Copy the Scores.txt file into the container
COPY /Scores.txt .

# Expose the port the app runs on
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "MainScores.py"]