IMAGE_NAME := grpc-example
TAG        := python

build-docker-image:
	docker build -t $(IMAGE_NAME):$(TAG) -f Dockerfile .

build:| build-docker-image

start: 
	docker-compose -f docker-compose.yml up -d