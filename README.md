# cloud-resume-challenge

This is a project making use of AWS to host my CV at <https://www.kylerloucks.click>

## AWS Architecture
![Diagram](https://user-images.githubusercontent.com/60449948/190263646-20b2e186-f92d-44cb-b654-be4c965a0575.png)

This project is a static website hosted on S3. It utilizes AWS S3 with AWS CloudFront to distribute the website at a global scale.
ACM is used to provide SSL certificates. The backend is written in python and utilizes AWS API Gateway and AWS Lambda to control the backend
by updating the Viewer Counter on the website. HTML, CSS, and JavaScript are used for the frontend.
It makes use of a DynamoDB database to store a counter for the number of visitors.

## CI/CD Pipeline
This project utilizes AWS CodePipeline & CodeBuild to automate the latest deployments made to this github repository.
