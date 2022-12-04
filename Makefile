install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:	
	black *.py mylib/*py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py dblib
	#pylint --disable=R,C *.py

deploy:
	

all: install lint test format deploy