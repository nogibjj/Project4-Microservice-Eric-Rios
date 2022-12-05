install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py mylib/*py 

lint:
	# pylint --disable=R,C --ignore-patterns=test_.*?py *.py dblib
	pylint --disable=R,C *.py mylib/*.py

test:
	python -m pytest -vv --cov=mylib --cov=main test_*.py


# build:
# 	#build container
	docker build -t deploy-fastapi .

# run:
# 	#run docker
# 	#docker run -p 127.0.0.1:8080:8080 c1a36ab4da9d

# deploy:
# 	#deploy
# 	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
# 	docker build -t fastapi-wiki .
# 	docker tag fastapi-wiki:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest
# 	docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest

all: install lint test format deploy