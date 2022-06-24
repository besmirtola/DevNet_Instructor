#!/bin/bash
FILE=./Dockerfile
if [ -f "$FILE" ]; then
    echo "$FILE exists."
    docker build -t my-apache2 .
    docker run -dit --name docker_app -p 8088:80 my-apache2
    docker ps -a
else 
    echo "$FILE does not exist."
    echo "Create $FILE , build the image and then run."
    echo "FROM httpd:2.4" >> Dockerfile
    echo "COPY index.html /usr/local/apache2/htdocs/" >> Dockerfile
    echo "EXPOSE 8088" >> Dockerfile

    docker build -t my-apache2 .
    docker run -t -d -p 8088:80 --name docker_app my-apache2
    docker ps -a
fi

