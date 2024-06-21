# Top Level
I built a deeplearning language translation API using FastAPI that takes in text on a route called translate and returns it on a route called results. This was powered by Google's t5. 
I then deployed it to the cloud using Docker and Google Cloud. 

# IDE
You should use an IDE to deploy. 

# Usage 
To run the server locally, run 'uvicorn main:app --reload'.

# Docker image

To build and test a docker image, run:
- 'docker build -t dlapi .' to build the container
- 'docker run -d --name dlapi -p 80:80 dlapi' to run the container
- 'docker ps' to view container information
- 'docker stop dlapi' to stop the container

# Google Cloud set up

