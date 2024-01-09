# fb_recomendation_ranking_system
This is an implementation of the system behind the marketplace, which uses AI to recommend the most relevant listings based on a personalised search query.
In the Facebook Marketplace Search Ranking project, we are asked to develop and train a multimodal model that accepts images and text. The output of the model will generate embedding vectors that are helpful to make recommendations to buyers using their demographic information. Once the model is trained, we will have to deploy it by creating an API using FastAPI, containerising it using Docker, and uploading it to an EC2 instance. The API will contain all the models that we create and train, so any new request can be processed to make predictions on the cloud. To ensure that the model can be easily modified without building a new image again, the files corresponding to each model will be bound to the Docker image, so it allows us to update the models with retrained models even after deploying them.

- process and clean text and image datasets;
- design and train a multimodal model that combines images and text to generate embedding vectors to create a search index using Pytorch;
- create a pipeline to systematically clean new data and upsert it into a database;
- develop an API that encapsulates the models using FastAPI;
- deploy a container with the API using docker compose.

Milestones 1-2
The first and second milestones of the project consist in setting up GitHub, creating a repository for the project, an AWS account, and going over the technology that we are asked to reproduce.

Milestone 3
In milestone 3, we're required to clean both the tabular and the image datasets, which are made available to us as EC2 instances on AWS.
Tabular data cleaning

The tabular dataset contains information about the listing, including its price, location, and description. We are required to create a file named clean_tabular_data.py within our repository, which has to be populated with code to clean the tabular dataset. The dataset was in a EC2 instance on AWS, which is accessed by ssh from the local machine.


The image dataset comprises of a total of 12668 items. These do not have the same size, nor the same number of channels. We were therefore required to write code to make sure all images were consistent along these two dimensions.
The clean_images.pyfile in the repository contains the code I wrote to clean the image dataset. This implements a pipeline that applies the necessary cleaning to the image dataset by defining a function that takes two arguments: final_size (int), the size value in pixels of the resized image, and image (image), the image to be resized.





