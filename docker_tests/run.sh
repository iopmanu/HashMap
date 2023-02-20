docker pull python:3.8-alpine
cd ../
docker build -t unit_tests:latest .
docker run -d --name testing unit_tests:latest
