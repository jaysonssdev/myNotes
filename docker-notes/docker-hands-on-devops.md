# Docker for Absolute Beginners – Hands-On DevOps

## Introduction

### What is Docker?
- is a set of platform as a service products that use **OS-level virtualization** to deliver software in packages called **containers**.
- a platform for building, running, and shipping applications.
- tool to create an **image which will have all the dependencies required** to run your tests/app.

### Why we need Docker?
- when we build the application in one system and try to run it in another system or machine, it might not work, because in real time the application will have many dependencies & configurations.
- **To overcome these issues we introduce docker.**
    - Where we just need to run some docker command and tell docker to run the application.
    - Then docker will automatically download all the dependencies & configuration and install the application and run in an isolated environment called **container**.

### What is Container?
- are isolated from one another and bundle their own software, libraries, and configuration files.
- they can communicate with each other through well-defined channels
- contains independent services which can be shipped to any cluster. Example: API Testing FW, UI Automation FW image, etc.
- **2 Types of Docker Container**
    - **linux container**
        - works on windows, mac, linux
        - size: few MBs only
    - **windows container**
        - works on windows only
        - size: in GBs

### What is Docker Image?
- includes everything needed **to run a piece of software** (code, runtime, libraries, dependencies)

### What is Docker file?
- is a **text file that contains a set of instructions** on how to build a Docker Image.
- think of it like a recipe or a set of steps needed to create a specific environment for running your application.

### Dockerfile > Docker Image > Docker Container
- **Docker File:** A text file that has instructions.
- **Docker Image:** A packaged environment with everything needed to run an application.
- **Docker Container:** A running instance of a docker image.

![alt text](images/docker-hands-on-devops/2026-07-14_13-53.png)

### What is Kubernetes?
- is **a system for managing containerized applications** across a cluster of nodes.
- in simple terms, you have a group of machines (e.g.VMs) and containerized applications (e.g. Dockerized applications), and Kubernetes will help you to easily manage those apps across those machines.

![alt text](images/docker-hands-on-devops/2026-07-14_14-14.png)

### Docker Terminology

![alt text](images/docker-hands-on-devops/2026-07-14_14-40.png)

<br>
<br>
<br>

## Crash Course

### Docker Flow Diagram
- - Using **Dockerfile** we can create an Image and push to docker Hub, where anyone can pull the image & create a container and execute the tests. 

![alt text](images/docker-hands-on-devops/2026-07-14_22-00.png)

- **Docker-compose.yml** will have all the instructions to the docker that from where to pull the images and on which network we have to run and communicate between images, etc.

![alt text](images/docker-hands-on-devops/2026-07-14_22-08.png)

<br>

### Docker Important Commands

![alt text](images/docker-hands-on-devops/2026-07-14_22-10.png)

#### Practical - Docker Pull
- Go to https://hub.docker.com/ then search for 'hello-world'
- Click the first result.
- Copy the command `docker pull hello-world`
- Go to your terminal:
```bash
# To pull a basic docker image
docker pull hello-world

# To check your current available images
docker images

# To create a container from the 'hello-world' image
docker run hello-world  

# To see all of your containers, even the stopped ones
docker ps -a

# Since the hello-world container is stopped, you can delete it by
docker system prune -a
```

#### Practical - Creating Ubuntu Linux Machine using Docker
- Run: `docker run -it ubuntu bash`, this will automatically pull the ubuntu image.
- After that, you will be automatically inside the ubuntu made by docker. You can run linux commands to test.
- Create a file or a new folder, `mkdir test`
- Run `exit` to exit the ubuntu (this will also stop its container)
- Now that you're back in your terminal, run `docker ps -a` to see the ubuntu container.
- Run again `docker run -it ubuntu bash`, notice that the 'test' folder that you created earlier is not there anymore. It is because **docker creates a fresh brand new container** whenever you run that command.

<br>

### What is Docker Port Mapping?
- Docker can also run virtual machine, which means **a machine inside a machine**.
- So to identify a 'Machine' and 'App' inside a machine, we need to map the **port**. If we will not map the port we can't identify an app hence can't execute.

![alt text](images/docker-hands-on-devops/2026-07-15_00-10.png)

- Example (Not related to the image above):
    - `docker run -p 8081:80 nginx` (-p means port)
    - this will map the **host(or external) port 8081** with **container(or internal) port 80** for nginx
    - You can run now this locally by `http://localhost:8081`

#### Practical - Port Mapping
- Go to https://hub.docker.com/ then search for 'nginx'
- Click the result 'nginx: Docker Official Image'
- Run this command: `docker run -p 8080:80 nginx` 

![alt text](images/docker-hands-on-devops/2026-07-15_12-45.png)

- In terminal, press `ctrl + c` to exit.

<br>

### Volume Mapping Concepts

- **WITHOUT Volume Mapping**: if we run anything inside the container then **results will also be published inside the container only** and we can't see the reports, etc.

- **WITH Volume Mapping**: we can **create a tunnel between host and container** so that we can share anything across.

- **Note**: Before going through volume mapping please check the docker settings. `Settings > Resources > File Sharing`, then change the directory path that will be used for volume mapping. Example: /User/MyName/workspace

![alt text](images/docker-hands-on-devops/2026-07-15_13-43.png)

- **Volume Mapping Syntax**: `docker run -it -v /Users/MyName/practice_volume_mapping:/TestResults ubuntu`
    - flags:
        - `-it` - interactive mode
        - `-v` - volume mapping
        - `/Users/MyName/practice_volume_mapping` - the path in your host machine
        - `/TestResults` - assign any folder name, this will be the volume mapping path that will be created in your container
        - `:` - separator of the local path and container path
        - `ubuntu` - container name

<br>

### Docker Network Concepts
- Let's say we have 2 running containers, nginx and ubuntu.

![alt text](images/docker-hands-on-devops/2026-07-15_15-39.png)

- **WITHOUT network**, both containers will be running in isolation and can't communicate with each other.

- **WITH network**, both containers can identify each other and can commnicate through this network.

![alt text](images/docker-hands-on-devops/2026-07-15_15-45.png)

#### Practical - WITHOUT network

```bash
# Pull 2 images:
docker pull nginx
docker pull alpine

# Run nginx in 'background mode' by using `-d` flag, and name your container using the `--name=` flag
docker run -d --name=my-nginx nginx

# Then run alpine in 'interactive mode' by using `-it` flag
docker run -it --name=my-alpine alpine

# Now that you're inside the alpine container, ping nginx
ping my-nginx
# you'll get "ping: bad address 'nginx'"
# because it can't connect, due to non-existing network

# exit alpine container
exit 

# Delete the containers that you created, since alpine is not running when you exited it
docker rm my-alpine
# You can't delete a container if it still running, so stop nginx first
docker stop my-nginx
docker rm my-nginx
```

#### Practical - WITH network

```bash
# Create first the network
docker network create my-network

# Run nginx in 'background mode' by using `-d` flag and use `--network` flag to use the network that you just created
docker run -d --network=my-network --name=my-nginx nginx

# Then run alpine in 'interactive mode' by using `-it` flag with the `--network` flag
docker run -it --network=my-network --name=my-alpine alpine

# Now that you're inside the alpine container, ping nginx
ping my-nginx
# Notice that you can ping nginx, which means you can connect to it by the network that you created
# press ctrl + c to stop pinging

# Connect to nginx
wget my-nginx # to get the 'index.html'
```

<br>
<br>
<br>

## Build & Run Docker Image using Dockerfile

### Setup Editor for building the Dockerfile
- Create a folder (example: simple_data) and open it using your editor (example: VS Code)
- Open terminal inside the your editor.
- For you to have an idea what we are building, run the following:
    - `docker run -it alpine`
    - Inside the alpine container, run `date`
    - This is what we are building, a simple application using docker image, that shows the current date.

### Creating a Simple Docker Image using Dockerfile

![alt text](images/docker-hands-on-devops/2026-07-15_19-21.png)

- Inside the simple_date folder, create a 'Dockerfile'
```Dockerfile
FROM alpine
ENTRYPOINT date 
```
- If you haven't logged in to your Docker Hub account yet, log in by running `docker login -u <your-username>`
- To build the docker image using the Dockerfile that you created within the same folder, run `docker build -t=<username>/<nameofyourimage> .`. Example: `docker build -t=jaysonssdev/getcurrentsystemdate .` **Note:** Dot (.) means the Dockerfile is in the same folder.
- Check your newly created image by running: `docker images`
- You can run it by running `docker run jaysonssdev/getcurrentsystemdate`

### Pushing Image to Docker Hub

![alt text](images/docker-hands-on-devops/2026-07-15_20-25.png)





<br>
<br>
<br>

## Build & Run Docker Image using docker-compose
