# Microsservices
Python microsservices - 

Reference:
https://realpython.com/python-microservices-grpc/

## Simple scheme:
![Alt text](docs/microservices.webp?raw=true "Scheme")

- Marketplace will be a very minimal web app that displays a list of books to the user.
- Recommendations will be a microservice that provides a list of books in which the user may be interested.

API - using gRPC - Google Remote Procedure Call - it could be better than Swagger and RAML.

 "[Performance] RPC framework is generally more efficient than using typical HTTP requests. gRPC is built on top of HTTP/2, which can make multiple requests in parallel on a long-lived connection in a thread-safe way..."

 "[Developer-Friendliness] Probably the most interesting reason why many people prefer gRPC over REST is that you can define your API in terms of functions, not HTTP verbs and resources. As an engineer, you’re used to thinking in terms of function calls, and this is exactly how gRPC APIs look."

 
# DOCKER

docker build . -f marketplace/Dockerfile -t marketplace
docker run -p 127.0.0.1:5000:5000/tcp marketplace

docker build . -f recommendations/Dockerfile -t recommendations
docker run -p 127.0.0.1:50051:50051/tcp recommendations