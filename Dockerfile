# Use premade runtime as a parent image
FROM 6783a438c8a7

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN python setup.py install

EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "server.py"]

