# Iris classification using Tensorflow Keras and Flask

- Training of a simple neural network model using TF Keras
- Deploying the model as an API using Flask
- Deploying the model as a website using Flask

# How to run (using Docker container)
1. Build a docker image by running `docker build --tag <image_name> .` in the same folder as the Dockerfile using terminal.
2. After docker image is built, run the docker container using `docker run --publish 8000:5000 <image_name>`
3. In your browser, open localhost:8000 and you will be able to see the app.

# Alternative method to run
1. Install the necessary python libraries in requirements.txt
2. Cd into the folder and run the Flask app using terminal: `python app.py`


# Acknowledgements / References

This project is part of an online tutorial by Pierian Training: https://nlbsg.udemy.com/course/complete-tensorflow-2-and-keras-deep-learning-bootcamp/learn/lecture/17377752#overview

