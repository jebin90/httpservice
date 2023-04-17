PORT=8080
IMAGE_NAME=my-http-service
#GIT_HASH=$(shell git rev-parse HEAD)
#GIT_NAME=$(shell git remote -v | head -n1 | awk '{print $$2}')

all: build run

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -p $(PORT):$(PORT) $(IMAGE_NAME)
#docker run -it --rm -p $(PORT):$(PORT) -e PORT=$(PORT) -e GIT_HASH=$(GIT_HASH) -e GIT_NAME=$(GIT_NAME) $(IMAGE_NAME)