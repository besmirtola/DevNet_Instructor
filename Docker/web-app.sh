#!/bin/bash
FILE=./Dockerfile
if [ -f "$FILE" ]; then
    echo "$FILE exists."
    docker build -t sampleapp .
    docker run -t -d -p 8081:8081 --name docker_app sampleapp
    docker ps -a
else 
    echo "$FILE does not exist."
    echo "Create $FILE , build the image and then run."
    echo "FROM python" >> Dockerfile
    echo "RUN pip install flask" >> Dockerfile
    echo "COPY ./static /home/myapp/static/" >> Dockerfile
    echo "COPY ./templates /home/myapp/templates/" >> Dockerfile
    echo "COPY web_app_flask.py /home/myapp/" >> Dockerfile
    echo "EXPOSE 8081" >> Dockerfile
    echo "CMD python3 /home/myapp/web_app_flask.py" >> Dockerfile

    docker build -t sampleapp .
    docker run -t -d -p 8081:8081 --name docker_app sampleapp
    docker ps -a
fi


