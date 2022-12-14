[![Python Application Test With Github Actions](https://github.com/nogibjj/Project4-Microservice-Eric-Rios/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/Project4-Microservice-Eric-Rios/actions/workflows/main.yml) [![Docker Image Sent to ECR and Built Via Code Build](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiR1FsL1ZaVForTmtMY3BiR2txZUtDNDh0UGFNVDkzcXM2alp4c0ZEc1Q0MGkzRU0wdFh3TFRnUTdCN3VRaG1icjBpTlVxeTlRME5UYjRJL0d6RGZtaW5NPSIsIml2UGFyYW1ldGVyU3BlYyI6IkR6amZIT1lTeTFpY2R3cysiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

# Activities to Cure Boredom by Eric Rios : A Microservice Hosted on AWS

## Overview

The objective of this project is to create a microservice and deploy it on the web as a small application. The user inputs the parameter on one of three pre-established queries and gets an activity to stave off the boredom. The outputs are based on getting activities by type, number of participants and price. If the user does not input an allowable value, a custom error message is printed, so that the user then inputs the value correctly.

## Steps and Tools

Flowchart

![image](https://user-images.githubusercontent.com/70504872/205868084-1c861f63-0d04-44e2-83ac-de4447802d4a.png)

### Scaffolding

A makefile, a requirements file, and the test files were created. They were all run by github actions as a measure of continuous integration. Something to flag was how the aws-cli was key to making this work, as the aws-cliv2 and aws packages caused authentication issues. 

### FastAPI and the Boredom API

The main python file called upon the functions derived in the logic.py file. They were then wrapped under the FastAPI to generate a quick web application. The API utilized to get the data for the app was the boredom api, found at https://www.boredapi.com/.

### Continuous Delivery

A docker image was built to containerize the app. Then it was sent to an AWS ECR repository. From there, it gets built through AWS Code Build. It is important to also flag that the AWS account's owner must add the AmazonEC2ContainerRegistryFullAccess to the permissions under the policy that manipulates or oversees that repository. Otherwise, the build won't complete. Once built, the app is deployed through AWS AppRunner, and it becomes immediately available to anyone. Something else that affects the permissions is creating a codebuild with elevated build privileges, a good way to avoid the "are the docker daemons running" error.

### Results:

Link to app: https://ijtqmzv63p.us-east-1.awsapprunner.com/docs

![image](https://user-images.githubusercontent.com/70504872/205870064-13e32c0e-fd51-443b-9adc-e080edbb2f56.png)


### Update December 13, 2022: 

I had an issue with aws credentials, where I forgot and changed my access keys because I needed them for another project. The apprunner link changed now. It all works.
