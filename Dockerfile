# Use premade runtime as a parent image
FROM tensorflow/tensorflow

RUN apt-get update && apt-get install -y libjpeg-dev protobuf-compiler

# ADD tensorflow-1.4.0-cp27-none-any.whl .

# RUN pip install tensorflow-1.4.0-cp27-none-any.whl

# Set the working directory to /app

RUN pip --no-cache-dir install \
        Pillow \
        Flask \
        tensorflow \
        six \
        matplotlib

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN python setup.py install

EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "server.py"]

