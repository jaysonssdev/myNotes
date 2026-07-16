# This is the image that you get in docker hub
FROM alpine

# This is the java that you will install in the alpine
RUN apk add openjdk17

# This is to fix the path of javac to make it executable
ENV PATH=$PATH:/usr/lib/jvm/java-17-openjdk/bin/javac

# This is to set the working directory
WORKDIR /app

# Add a file to be copied from the host to the container
ADD HelloWorld.java HelloWorld.java

# Commands to execute the app
ENTRYPOINT javac HelloWorld.java && java HelloWorld
