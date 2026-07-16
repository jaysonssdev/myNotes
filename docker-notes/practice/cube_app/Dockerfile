FROM alpine:3.20

# Install python3 (pip is not needed for this script)
RUN apk add --no-cache python3

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY cube.py .

# The bracket syntax allows the container to accept arguments at runtime.
ENTRYPOINT ["python3", "cube.py"]
