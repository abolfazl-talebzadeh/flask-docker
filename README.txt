How to run docker compose:
c:\>docker-compose up --build -d

--build: for building containers and images which alreardy exists in the docker files
-d: activates the detached mode which enables the docker to be run on the background


these commands can be used to:

docker-compose down                             deactivates the docker-compose 

c:\>docker-compos ps                            see the list of running docker-compose containers

c:\>docker ps                                   see the docker containers 

c:\>docker images                               see docker images

c:\>docker rmi <image_name>                     delete images:

c:\>docker rm <container_name>                  delete containers

c:\>docker exec -it <container_name> /bin/bash  access the file system inside a container    