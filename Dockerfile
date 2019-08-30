FROM python:3.7-alpine

ENV NUM_FILES 10000

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

CMD ["python", "ulimit-checker.py"]
